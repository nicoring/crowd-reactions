from flask import Flask
from flask_restful import Resource, Api

from resources import advertisements, reactions
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

api = Api(app)

# api.add_resource(advertisements.AdvertisementList, '/advertisements')
# api.add_resource(advertisements.AdvertisementRes, '/advertisements/<ad_id>')
api.add_resource(reactions.AdReactionList, '/ads')
api.add_resource(reactions.AdReaction, '/ads/<ad_id>')

if __name__ == '__main__':
  app.run(debug=True, use_debugger=True, port=5000)
