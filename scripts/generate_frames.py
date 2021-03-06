import subprocess
import json
import sys
import os

def get_seconds(seconds):
  # seconds = float(frame * fps)
  second = int(seconds % 60)

  return '{}:{}.{}'.format(str(int(seconds / 60)).zfill(2), str(second).zfill(2), str((seconds % 60) - second)[2:])

if __name__ == '__main__':
  data = None

  if len(sys.argv) < 4:
    print('not enough arguments')
    sys.exit()

  json_file = sys.argv[1]
  video_file = sys.argv[2]
  output = sys.argv[3]

  with open(json_file, 'r') as f:
    data = json.loads(f.read())
  
  timescale = int(data['timescale'])
  framerate = float(data['framerate'])

  i = 0
  for fragment in data['fragments']:
    if 'events' in fragment:
      start = int(fragment['start'])
      interval = int(fragment['interval'])

      tick = start

      j = 0
      for event in fragment['events']:
        seconds = float(float(tick) / float(timescale))
        # print('{} -> {} , {}'.format(tick, seconds, get_seconds(seconds)))
        # subprocess.call(['ffmpeg', '-i', 'testvideo.mp4', '-vf', 'select=gte(n,{})'.format() -frames:v 1 frame.png'])
        subprocess.call(['ffmpeg', '-i', video_file, '-ss', get_seconds(seconds), '-frames:v', '1', os.path.join(output, 'frame-{:04d}-{}-{:}.jpg'.format(i, j, seconds))])
        tick += interval
        j += 1
        break
    i += 1