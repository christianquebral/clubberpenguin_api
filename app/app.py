from decouple import config
from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api
from models import PlayerDetail

from resources.game import Games
from resources.playerauth import PlayerAuth
from resources.playerstate import PlayerStates
from resources.storeitem import StoreItems
from resources.purchase import Purchases
from custom import Leaderboard, Player, PlayerInventory, PlayerInventoryItems

import markdown
import os
import ssl


app = Flask(__name__)
CORS(app)
api = Api(app)


@app.route('/')
def index():
	with open(
		os.path.dirname(app.root_path) + '/README.md', 'r'
	) as readme_file:
		content = readme_file.read()
		return markdown.markdown(content)


api.add_resource(Player, "/player/<string:player_name>")
api.add_resource(PlayerAuth, "/player/auth")
api.add_resource(PlayerInventory, "/player/<string:player_name>/inventory")
api.add_resource(PlayerInventoryItems, "/player/<string:player_name>/inventory/items")
api.add_resource(PlayerStates, "/player/states")
api.add_resource(Games, "/games")
api.add_resource(Leaderboard, "/leaderboard")
api.add_resource(Purchases, "/store/purchase")
api.add_resource(StoreItems, "/store")

if config("ENV") == "PROD":
	ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
	ctx.load_cert_chain("./cert/fullchain.pem", "./cert/privkey.pem")
	app.run(host="0.0.0.0", port=80, debug=False, ssl_context=ctx)

else:
	app.run(host="0.0.0.0", port=80, debug=True)
