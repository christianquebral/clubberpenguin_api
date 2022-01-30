import bcrypt
import requests

from datetime import datetime
from flask import request
from flask_restful import Resource

from utils import hash_password, check_password, require_key
from models import PlayerDetail
from session import Session


class PlayerAuth(Resource):
    @require_key
    def get(self):
        session = Session()

        try:
            player = request.args["playername"].upper()
            password = request.args["password"]

            query = session.query(PlayerDetail).filter_by(player_name=player)

            result = query.first()

            if result:
                if result.player_name == player and check_password(
                    password, result.password_hash
                ):
                    return {
                        "success": True,
                        "message": "Player logged in successfully",
                        "data": {"player_id": result.id},
                    }, 202
                else:
                    return {
                        "success": False,
                        "message": "Incorrect password",
                        "data": {},
                    }, 401
            else:
                return {
                    "success": False,
                    "message": "Player not found",
                    "data": {},
                }, 404
        finally:
            session.close()

    @require_key
    def post(self):
        session = Session()

        try:
            player = request.args["playername"].upper()
            password = request.args["password"]

            query = session.query(PlayerDetail).filter_by(player_name=player)

            result = query.first()

            if result:
                return {
                    "success": False,
                    "message": "Player name already exists",
                    "data": {},
                }, 409
            else:
                _hash = hash_password(password)
                session.add(
                    PlayerDetail(
                        player_name=player,
                        password_hash=_hash,
                        created_date=datetime.now(),
                    )
                )

                id_query = session.query(PlayerDetail).filter_by(player_name=player)
                id_result = id_query.first().id

                session.commit()

                return {
                    "success": True,
                    "message": "Player created",
                    "data": {"player_id": id_result},
                }, 201
        finally:
            session.close()
