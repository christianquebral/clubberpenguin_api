import requests

from datetime import datetime
from flask import request
from flask_restful import Resource
from sqlalchemy import text

from models import Purchase
from session import Session


class Leaderboard(Resource):
    def get(self):
        session = Session()

        try:
            results = session.execute(text("SELECT * FROM v_leaderboard"))

            data = []

            for row in results:
                record = {
                    "player_rank": row[0],
                    "player_name": row[1],
                    "player_score": row[2],
                    "date_achieved": str(row[3]),
                }
                data.append(record)

            return {
                "success": True,
                "message": "Successfully retrieved leaderboard records",
                "data": data,
            }, 200
        finally:
            session.close()


class Player(Resource):
    def get(self, player_name):
        session = Session()

        try:
            query = session.execute(
                text(
                    "SELECT * FROM v_player_stats WHERE player_name = UPPER(:s)"
                ).params(s=player_name)
            )

            result = query.first()

            if result:
                data = {
                    "player_id": str(result[0]),
                    "player_name": result[1],
                    "high_score": result[2],
                    "total_score": str(result[3]),
                    "player_rank": str(result[4]),
                    "games_played": result[5],
                    "average_game_duration": str(result[6]),
                    "total_game_duration": str(result[7]),
                    "date_joined": str(result[8]),
                }

                return {
                    "success": True,
                    "message": f"Successfully retrieved data for {player_name}",
                    "data": data,
                }, 200

            else:
                return {
                    "success": False,
                    "message": f"Unable to find data for player {player_name}",
                    "data": {},
                }, 404
        finally:
            session.close()


class PlayerInventory(Resource):
    def get(self, player_name):
        session = Session()

        try:
            query = session.execute(
                text(
                    "SELECT * FROM v_player_inventory WHERE player_name = UPPER(:s)"
                ).params(s=player_name)
            )

            result = query.first()

            if result:
                data = {
                    "player_id": result[0],
                    "player_name": result[1],
                    "remaining_balance": int(result[2]),
                    "inventory": result[3],
                }

                return {
                    "success": True,
                    "message": f"Successfully retrieved inventory data for {player_name}",
                    "data": data,
                }, 200
            else:
                return {
                    "success": False,
                    "message": f"Unable to find inventory data for player {player_name}",
                    "data": {},
                }, 404
        finally:
            session.close()


class PlayerInventoryItems(Resource):
    def get(self, player_name):
        session = Session()

        try:
            query = session.execute(
                text(
                    "SELECT * FROM v_player_inventory_items WHERE player_name = UPPER(:s)"
                ).params(s=player_name)
            )

            result = query.all()

            if result:
                data = []
                for row in result:
                    record = {
                        "player_id": row[0],
                        "player_name": row[1],
                        "item_name": row[2],
                        "item_type": row[3],
                    }
                    data.append(record)

                return {
                    "success": True,
                    "message": f"Successfully retrieved inventory data for {player_name}",
                    "data": data,
                }, 200
            else:
                return {
                    "success": False,
                    "message": f"Unable to find inventory data for player {player_name}",
                    "data": {},
                }, 404
        finally:
            session.close()
