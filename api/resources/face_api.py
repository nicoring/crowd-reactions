import requests
import os
import json

class FaceApi:
    url_face = 'https://api.projectoxford.ai/face/v1.0/detect' + \
          '?returnFaceId=false' + \
          '&returnFaceAttributes=age,gender,smile,glasses,facialHair'

    url_emotion = 'https://api.projectoxford.ai/emotion/v1.0/recognize'

    ms_key_face = "c55df0370573477296be9e427c385caa"
    ms_key_emotion = "041934c1ae02470db6f994897b68ebfd"

    def headers(self, key_name):
        key = self.ms_key_face if key_name == "face" else self.ms_key_emotion
        return {
            'content-type': 'application/octet-stream',
            'Ocp-Apim-Subscription-Key': key
        }

    def face_data(self, image):
        r = requests.post(self.url_face, headers=self.headers('face'), data=image)
        if r.status_code != 200:
            print(r.text)
            return
        res_json = r.json()
        print(res_json)
        for obj in res_json:
            # print(obj)
            yield obj['faceAttributes']

    def face_emotion(self, image):
        r = requests.post(self.url_emotion, headers=self.headers('emotion'), data=image)
        if r.status_code != 200:
            print(r.text)
            return
        res_json = r.json()
        print(res_json)
        for obj in res_json:
            yield obj['scores']

    def get_count(self, s):
        return

    def process_images(self, path):
        dirs = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
        dirs.sort()
        for d in dirs:
            emotions = []
            faces = []
            timestamp = d.split('/')[-1].split('_')[-1]
            for f in os.listdir(os.path.join(path, d)):
                if not f.startswith('.'):
                    image = open(os.path.join(path, d, f), 'rb').read()
                    faces += list(self.face_data(image))
                    emotions += list(self.face_emotion(image))
            yield {
                'timestamp': timestamp,
                'count': len(faces),
                'emotions': emotions,
                'faces': faces
            }

if __name__ == "__main__":
    path = '../../frames/faces/'

    fa = FaceApi()

    out = open('face.out.json', 'w')

    # image = open(filename, 'rb')
    # print(fa.face_data(image))
    # print(fa.face_emotion(image))
    # ['../../experiments/kopf.png', '../../experiments/kopf2.png']
    result = list(fa.process_images(path))

    final_dict = {
        "ad_id": 'subway',
        "data": list(result)
    }

    out.write(json.dumps(final_dict))
    out.close()
