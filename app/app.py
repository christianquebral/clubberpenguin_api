from flask import Flask
from flask_restful import Resource, Api
from models import PlayerDetail
from resources.playerauth import PlayerAuth

app = Flask(__name__)
api = Api(app)

api.add_resource(PlayerAuth, "/player/auth")

app.run(host="0.0.0.0", port=80, debug=True)
