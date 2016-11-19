import random

from flask_restful import Resource, Api


def random_ad(ad_id=None):
  ad_id = ad_id or random.randint(1, 500),
  return {
    'id': ad_id,
    'title': 'Random Ad #{}'.format(ad_id),
    'type': random.choice(('image', 'video')),
    'resource_url': 'https://hpi.de/fileadmin/user_upload/fachgebiete/plattner/teaching/MasterProject/2013/mpws2013hp-poster.png'
  }

class Advertisement(Resource):
  def get(self, ad_id):
    return random_ad(ad_id)

class AdvertisementList(Resource):
  def get(self):
    n = random.randint(5, 10)
    return {'advertisements': [random_ad() for i in range(n)]}
