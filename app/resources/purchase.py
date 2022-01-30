import requests

from datetime import datetime
from flask import request
from flask_restful import Resource

from models import Purchase
from session import Session


class Purchases(Resource):
    # get() not needed for this resource - only need to send purchases
    # to store table.

    def post(self):
        session = Session()

        try:
            player_id = request.args["playerid"]
            item_id = request.args["itemid"]
            created_date = str(datetime.now())

            session.add(
                Purchase(
                    player_id=player_id, item_id=item_id, created_date=created_date
                )
            )

            data = {
                "player_id": player_id,
                "item_id": item_id,
                "created_date": created_date,
            }

            session.commit()

            return {
                "success": True,
                "message": "Successfully processed purchase",
                "data": data,
            }, 201
        finally:
            session.close()
