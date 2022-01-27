import requests

from datetime import datetime
from flask import request
from flask_restful import Resource

from models import Game, PlayerDetail
from session import session


class Games(Resource):
    def get(self):
        query = (
            session.query(Game)
            .join(PlayerDetail)
            .order_by(Game.created_date.desc())
            .limit(50)
        )

        result = query.all()

        if result:
            data = []
            for row in result:
                record = {
                    "game_id": row.id,
                    "player_id": row.player_id,
                    "player_name": row.player.player_name,
                    "player_score": row.player_score,
                    "created_date": str(row.created_date),
                }
                data.append(record)

            return {
                "success": True,
                "message": "Successfully retrieved last 50 rows of game data",
                "data": data,
            }, 200

        else:
            return {
                "success": False,
                "message": "Unable to access game data",
                "data": {},
            }, 400

    def post(self):
        player_id = request.args["playerid"]
        player_score = request.args["playerscore"]
        game_time = request.args["gametime"]
        created_date = datetime.now()

        session.add(
            Game(
                player_id=player_id,
                player_score=player_score,
                game_time=game_time,
                created_date=created_date,
            )
        )
        session.commit()

        data = {
            "player_id": player_id,
            "player_score": player_score,
            "game_time": game_time,
            "created_date:": str(created_date),
        }

        return {
            "success": True,
            "message": "Successfully posted game data",
            "data": data,
        }, 201
