import os
from subprocess import call
import json


def clean_directory(directory):
    files = os.listdir(directory)
    for f in files:
        os.remove(directory + f)


def create_directory_if_missing(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def extract_keyframes(filename, framerate, output_dir='ffmpeg_out/'):
    assert(os.path.isfile(filename)), 'Could not open file ' + filename
    create_directory_if_missing(output_dir)
    clean_directory(output_dir)
    call(['ffmpeg', '-n', '-nostdin', '-i', filename, '-r', str(framerate), '-qscale:v', '2', '-nostats' , '-loglevel', '0', output_dir+'%3d.jpg'])
    keyframes = sorted(os.listdir(output_dir))
    return [output_dir + frame for frame in keyframes]


if __name__ == '__main__':
    d = json.loads(open('../out.json', 'r').readlines()[0])
    starts = [e['start'] for e in d['fragments']]
    with open('list.txt', 'w+') as f:
        for start in starts:
            f.write('{:0.3f}\n'.format(start / 90000))
