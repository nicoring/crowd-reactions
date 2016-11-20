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


tmp = [
    '8.341666666666667',
    '10.5105',
    '14.347666666666667',
    '17.183833333333332',
    '19.853166666666667',
    '19.886533333333333',
    '19.9199',
    '19.953266666666668',
    '19.986633333333334',
    '20.02',
    '20.053366666666665',
    '20.086733333333335',
    '20.1201',
    '20.153466666666667',
    '20.186833333333333',
    '20.2202',
    '20.253566666666668',
    '20.286933333333334',
    '20.3203',
    '20.687333333333335',
    '20.7207',
    '20.754066666666667',
    '20.787433333333333',
    '20.8208',
    '20.854166666666668',
    '20.887533333333334',
    '20.9209',
    '20.954266666666665',
    '20.987633333333335',
    '21.021',
    '21.054366666666667',
    '21.087733333333333',
    '21.1211',
    '21.154466666666668',
    '21.187833333333334',
    '21.2212',
    '21.254566666666665',
    '21.287933333333335',
    '21.3213',
    '21.354666666666667',
    '21.388033333333333',
    '21.4214',
    '21.454766666666668',
    '21.488133333333334',
    '21.5215',
    '21.554866666666666',
    '21.588233333333335',
    '21.6216',
    '21.654966666666667',
    '28.5285',
    '30.5305',
    '32.5325',
    '32.565866666666665',
    '32.59923333333333',
    '32.6326',
    '32.66596666666667',
    '32.699333333333335',
    '32.7327',
    '32.76606666666667',
    '32.79943333333333',
    '32.8328',
    '32.866166666666665',
    '32.89953333333333',
    '36.87016666666667',
    '36.903533333333336',
    '36.9369',
    '36.97026666666667',
    '37.00363333333333',
    '37.037',
    '37.070366666666665',
    '37.10373333333333',
    '37.1371',
    '37.17046666666667',
    '37.203833333333336',
    '37.2372',
    '37.27056666666667',
    '37.30393333333333',
    '37.3373',
    '37.370666666666665',
    '37.40403333333333',
    '37.4374',
    '37.47076666666667',
    '37.504133333333336',
    '37.5375',
    '37.57086666666667',
    '37.60423333333333',
    '37.6376',
    '37.670966666666665',
    '41.708333333333336',
    '44.878166666666665',
    '48.5485',
    '50.5505',
    '50.583866666666665',
    '50.61723333333333',
    '50.6506',
    '50.68396666666667',
    '50.717333333333336',
    '50.7507',
    '50.78406666666667',
    '50.817433333333334',
    '50.8508',
    '50.884166666666665',
    '50.91753333333333',
    '54.88816666666666',
    '56.890166666666666',
    '59.893166666666666',
    '61.89516666666667',
    '63.897166666666664',
    '66.90016666666666',
    '69.23583333333333',
    '71.23783333333333',
    '73.40666666666667',
    '73.44003333333333',
    '73.4734',
    '73.50676666666666',
    '73.54013333333333',
    '73.5735',
    '73.60686666666666',
    '73.64023333333333',
    '73.6736',
    '73.70696666666667',
    '73.74033333333334',
    '73.7737',
    '73.80706666666667',
    '73.84043333333334',
    '73.8738'
]

def crop_images(data, folder='/Users/mbornstein/Documents/projects/hackathon/frames'):
    i = 0

    output_folder = os.path.join(folder, 'faces')
    create_directory_if_missing(output_folder)

    time_slice = 0
    for fragment in data['fragments']:
        if 'events' in fragment:
            event = fragment['events'][0]
            print('index', i, len(event), 'faces')

            filename = 'frame-{:d}-0.jpg'.format(i)
            im = Image.open(folder + '/' + filename)
            im_size = np.array(im.size)

            frame_out_folder = os.path.join(output_folder, 'frame_{:04d}_{:s}'.format(i, tmp[time_slice]))
            time_slice += 1
            create_directory_if_missing(frame_out_folder)

            for j, face in enumerate(event):
                face_pos = np.array([face['x'], face['y']]) * im_size
                face_size = np.array([face['width'], face['height']]) * im_size

                upper_left = face_pos - face_size
                lower_right = (face_pos + face_size) + face_size

                new_im = im.crop((int(upper_left[0]), int(upper_left[1]),
                                  int(lower_right[0]), int(lower_right[1]))).resize((250, 250), Image.BICUBIC)

                n, ext = filename.split('.')

                new_filename = '{:s}/face_{:02d}.jpg'.format(frame_out_folder, j)
                new_im.save(new_filename)

        i += 1


if __name__ == '__main__':
    d = json.loads(open('out_halloween.json', 'r').readlines()[0])
    starts = [e['start'] for e in d['fragments']]

    # with open('list.txt', 'w+') as f:
    #     for start in starts:
    #         f.write('{:0.3f}\n'.format(start / 90000))

    crop_images(d)
