import json
import os

from flask_restful import Resource, Api

data_dir = 'data/'

class AdReaction(Resource):
  def get(self, ad_id):
    res = ''
    filepath = data_dir + ad_id
    with open(filepath, 'r') as f:
      res = json.loads(f.read())

    return res

class AdReactionList(Resource):

  def files_in_data_dir(self):
    for fn in os.listdir(data_dir):
        if os.path.isfile(data_dir + fn) and fn.endswith('.json'):
            yield fn

  def get(self):
    return {'ads': list(self.files_in_data_dir())}
