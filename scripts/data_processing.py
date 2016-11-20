import os
from subprocess import call
import json
from PIL import Image
import numpy as np

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


def crop_images(data, folder='/Users/mbornstein/Documents/projects/hackathon/frames'):
    i = 0

    output_folder = os.path.join(folder, 'faces')
    create_directory_if_missing(output_folder)

    for fragment in data['fragments']:
        if 'events' in fragment:
            event = fragment['events'][0]
            print('index', i, len(event), 'faces')

            filename = 'frame-{:d}-0.jpg'.format(i)
            im = Image.open(folder + '/' + filename)
            im_size = np.array(im.size)

            for j, face in enumerate(event):
                face_pos = np.array([face['x'], face['y']]) * im_size
                face_size = np.array([face['width'], face['height']]) * im_size

                upper_left = face_pos - face_size
                lower_right = (face_pos + face_size) + face_size

                new_im = im.crop((int(upper_left[0]), int(upper_left[1]),
                                  int(lower_right[0]), int(lower_right[1]))).resize((250, 250), Image.BICUBIC)

                n, ext = filename.split('.')

                new_filename = '{:s}/{:s}.{:d}.{:s}'.format(output_folder, n, j, ext)
                new_im.save(new_filename)

        i += 1


if __name__ == '__main__':
    d = json.loads(open('out_halloween.json', 'r').readlines()[0])
    starts = [e['start'] for e in d['fragments']]

    # with open('list.txt', 'w+') as f:
    #     for start in starts:
    #         f.write('{:0.3f}\n'.format(start / 90000))

    crop_images(d)
