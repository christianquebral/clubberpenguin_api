import requests

from datetime import datetime
from flask import request
from flask_restful import Resource

from models import StoreItem
from session import Session


class StoreItems(Resource):
    def get(self):
        session = Session()

        try:
            query = session.query(StoreItem).order_by(StoreItem.item_price.asc())

            result = query.all()

            if result:
                data = []
                for row in result:
                    record = {
                        "item_id": row.id,
                        "item_name": row.item_name,
                        "item_price": row.item_price,
                        "item_type": row.item_type,
                    }
                    data.append(record)

                return {
                    "success": True,
                    "message": f"Successfully retrieved {len(data)} store items",
                    "data": data,
                }, 200
            else:
                return {
                    "success": False,
                    "message": "Unable to access store items",
                    "data": {},
                }, 404
        finally:
            session.close()

    # no post needed at this time - data will be inserted via DB
