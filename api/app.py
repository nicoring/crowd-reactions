from flask import Flask
from flask_restful import Resource, Api

from resources import advertisements, reactions

app = Flask(__name__)
api = Api(app)

api.add_resource(advertisements.AdvertisementList, '/advertisements')
api.add_resource(advertisements.Advertisement, '/advertisements/<ad_id>')
api.add_resource(reactions.AdReactionList, '/advertisements/<ad_id>/reactions')
api.add_resource(reactions.AdReaction, '/advertisements/<ad_id>/reactions/<reaction_id>')

if __name__ == '__main__':
  app.run(debug=True)
