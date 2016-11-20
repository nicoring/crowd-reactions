#! /bin/bash

mkdir frames
for second in $(cat list.txt)
do
    ffmpeg -i $0 -ss $second -vframes 1 frames/$second.jpg
done
