from flask import Flask
from flask_restful import Resource, Api
from models import PlayerDetail

from resources.game import Games
from resources.playerauth import PlayerAuth
from resources.playerstate import PlayerStates
from resources.storeitem import StoreItems
from resources.purchase import Purchases
from custom import Leaderboard, Player, PlayerInventory

app = Flask(__name__)
api = Api(app)

api.add_resource(Player, "/player/<string:player_name>")
api.add_resource(PlayerAuth, "/player/auth")
api.add_resource(PlayerInventory, "/player/<string:player_name>/inventory")
api.add_resource(PlayerStates, "/player/states")
api.add_resource(Games, "/games")
api.add_resource(Purchases, "/store/purchase")
api.add_resource(StoreItems, "/store")
api.add_resource(Leaderboard, "/leaderboard")

app.run(host="0.0.0.0", port=80, debug=True)
