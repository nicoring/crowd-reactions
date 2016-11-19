import json

from flask_restful import Resource, Api

class AdReaction(Resource):
  def get(self, ad_id, reaction_id):
    res = ''
    with open('out.json', 'r') as f:
      res = json.loads(f.read())
  
    return {
      'id': 1,
      'processing_result': res
    }

class AdReactionList(Resource):
  def get(self):
    return {'hello': 'world'}
