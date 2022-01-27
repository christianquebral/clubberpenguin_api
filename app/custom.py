import requests

from datetime import datetime
from flask import request
from flask_restful import Resource
from sqlalchemy import text

from models import Purchase
from session import session


class Leaderboard(Resource):
    def get(self):
        result = session.execute(text("select * from dim_store_items"))

        for item in result:
            print(item)
