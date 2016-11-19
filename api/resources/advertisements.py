import random

from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource

from db import Db

def random_ad(ad_id=None):
  ad_id = ad_id or random.randint(1, 500),
  return {
    'id': ad_id,
    'title': 'Random Ad #{}'.format(ad_id),
    'type': random.choice(('image', 'video')),
    'resource_url': 'https://hpi.de/fileadmin/user_upload/fachgebiete/plattner/teaching/MasterProject/2013/mpws2013hp-poster.png'
  }

class Advertisement:
  def __init__(self):
    self.id = None
    self.title = ''
    self.type = 'image'
    self.resource_url = ''

  @staticmethod
  def from_json(data):
    ad = Advertisement()
    print(data)
    ad.id = int(data.get('id', 0))
    
    for k in Advertisement.json_keys:
      # print(data.get(k)
      setattr(ad, k, data.get(k) or '')
    return ad

  def to_json(self):
    data = { 'id': self.id }
    for k in Advertisement.json_keys:
      data[k] = getattr(self, k)
    return data

Advertisement.json_keys = ['title', 'type', 'resource_url']

class AdvertisementRes(Resource):
  def get(self, ad_id):
    return random_ad(ad_id)

class AdvertisementList(Resource):
  def get(self):
    db = Db()
    # n = random.randint(5, 10)
    # return {'advertisements': [random_ad() for i in range(n)]}
    ads = db.get_advertisements()
    return {'advertisements': [ad.to_json() for ad in ads]}

  def post(self):
    parser = reqparse.RequestParser()

    for k in Advertisement.json_keys:
      parser.add_argument(k)
    args = parser.parse_args()

    db = Db()

    new_ad = Advertisement.from_json(args)

    new_ad = db.add_advertisement(new_ad)

    return new_ad.to_json()
