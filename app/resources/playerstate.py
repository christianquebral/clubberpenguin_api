import requests

from datetime import datetime
from flask import request
from flask_restful import Resource

from models import PlayerState
from session import session


class PlayerStates(Resource):
    def get(self):
        player_id = request.args["playerid"].upper()

        query = session.query(PlayerState).filter(PlayerState.player_id == player_id)

        if query.first():
            result = query.one()

            data = {
                "head_equipped": result.head_equipped,
                "torso_equipped": result.torso_equipped,
            }

            result = {
                "success": True,
                "message": "Retrieved player state",
                "data": data,
            }

            return result, 200

        else:
            return {
                "success": True,
                "message": "Player state not found",
                "data": {},
            }, 404

    def put(self):
        player_id = request.args["playerid"]
        player_name = request.args["playername"]
        head_equipped = request.args["headequipped"]
        torso_equipped = request.args["torsoequipped"]
        date = datetime.now()

        query = session.query(PlayerState).filter(PlayerState.player_id == player_id)

        if query.first():
            # state = query.one()
            # query.torso_equipped = torso_equipped
            # query.head_equipped = head_equipped
            # query.date_modified = date
            query.update(
                {
                    "torso_equipped": torso_equipped,
                    "head_equipped": head_equipped,
                    "date_modified": date,
                }
            )
            session.commit()

            return {"success": True, "message": "Player state updated", "data": {}}, 204

        else:
            session.add(
                PlayerState(
                    player_id=player_id,
                    player_name=player_name,
                    head_equipped=head_equipped,
                    torso_equipped=torso_equipped,
                    date_modified=date,
                )
            )

            session.commit()

            return {"success": True, "message": "Player state created", "data": {}}, 201
