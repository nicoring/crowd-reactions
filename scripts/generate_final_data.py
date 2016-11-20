import sys
import json

ad_id = sys.argv[1]
faces_emotions_file = sys.argv[2]
out_file = sys.argv[3]

def get_objs():
    with open(faces_emotions_file, 'r') as f:
        lines = ''.join(f.readlines())
        objects = json.loads(lines)
        counter = 1
        for obj in objects:
            emotions = obj['emotions']
            faces = obj['faces']
            count = len(faces)
            yield {
                'count': count,
                'timestamp': counter,
                'faces': faces,
                'emotions': emotions
            }
            counter += 1


final_dict = {
    "ad_id": ad_id,
    "data": list(get_objs())
}

json_string = json.dumps(final_dict)
with open(out_file, 'w+') as f:
    f.write(json_string)
