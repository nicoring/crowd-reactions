from flask_restful import Resource, Api

class AdReaction(Resource):
  def get(self):
    return {'hello': 'world'}

class AdReactionList(Resource):
  def get(self):
    return {'hello': 'world'}
