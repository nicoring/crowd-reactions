import requests
import os

class FaceApi:
    url_face = 'https://api.projectoxford.ai/face/v1.0/detect' + \
          '?returnFaceId=false' + \
          '&r   eturnFaceAttributes=age,gender,smile,glasses,facialHair'

    url_emotion = 'https://api.projectoxford.ai/emotion/v1.0/recognize'

    ms_key_face = "672290280fcc4024a4ae02e61840d025"
    ms_key_emotion = "5c18809f900c4d07a9f7564f9bdda254"

    def headers(self, key_name):
        key = self.ms_key_face if key_name == "face" else self.ms_key_emotion
        return {
            'content-type': 'application/octet-stream',
            'Ocp-Apim-Subscription-Key': key
        }

    def face_data(self, image):
        r = requests.post(self.url_face, headers=self.headers('face'), data=image)
        if r.status_code != 200:
            return
        res_json = r.json()
        # print(res_json)
        for obj in res_json:
            print(obj)
            yield obj['faceAttributes']

    def face_emotion(self, image):
        r = requests.post(self.url_emotion,headers=self.headers('emotion'), data=image)
        if r.status_code != 200:
            return
        res_json = r.json()
        for obj in res_json:
            yield obj['scores']

    def process_images(self, filenames):
        for filename in filenames:
            image = open(filename, 'rb')
            faces = self.face_data(image)
            emotions = self.face_emotion(image)
            yield {
                'emotions': list(emotions),
                'faces': list(faces)
            }

if __name__ == "__main__":
    path = '../../experiments/faces/'
    filenames = [path + f for f in os.listdir(path) if not f.startswith('.') ]
    fa = FaceApi()
    # image = open(filename, 'rb')
    # print(fa.face_data(image))
    # print(fa.face_emotion(image))
    # ['../../experiments/kopf.png', '../../experiments/kopf2.png']
    print(list(fa.process_images(filenames)))
