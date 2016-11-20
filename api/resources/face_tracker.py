import requests
import json
import time
import sys

base_url = 'https://s3.eu-central-1.amazonaws.com/oxfordhack/'

class VideoFaceTracker:
    ms_key = "b51851fce23a44e3a1cf6dd2064c0853"

    def upload_video(self, url):
        url = 'https://api.projectoxford.ai/video/v1.0/trackface'
        headers = {
            'content-type': 'application/json',
            'Ocp-Apim-Subscription-Key': self.ms_key
        }
        data = {
            "url": "https://s3.eu-central-1.amazonaws.com/oxfordhack/testvideo.mp4"
        }

        r = requests.post(url, json=data, headers=headers)
        if r.status_code != 202:
            print(r.status_code)
            print(r.text)
            return False
        oid = r.headers['Operation-Location'].rsplit('/', 1)[1]
        print(oid)
        return oid

    def get_result(self, oid):
        url = 'https://api.projectoxford.ai/video/v1.0/operations/' + oid
        while (True):
            time.sleep(10)
            headers = {'Ocp-Apim-Subscription-Key': self.ms_key}
            r = requests.get(url, headers=headers)
            if r.status_code != 200:
                print(r.text)
                return False
            status = r.json()['status']
            if status == 'Failed':
                return False
            elif status == 'Succeeded':
                return r.json()['processingResult']
            else:
                print('Running')


    def track_faces(self, url):
        oid = self.upload_video(url)
        if not oid:
            print('Upload Failed')
        else:
            print('Uploaded')
            return self.get_result(oid)



if __name__ == "__main__":
    vft = VideoFaceTracker()
    # data = vft.track_faces('https://s3.eu-central-1.amazonaws.com/oxfordhack/testvideo.mp4')
    # data = vft.get_result('956d2821-bf95-40e5-96ee-a502c2befab2')
    if len(sys.argv) < 2:
        print('Provide filename of video as argument')
    else:
        # data = vft.track_faces(base_url + sys.argv[1])
        data = vft.get_result('28dde30c-5313-4158-860c-704266969145')
        if data:
            with open('out_booth.json', 'w+') as f:
                f.write(data)
            print(data)
        else:
            print('failed')
