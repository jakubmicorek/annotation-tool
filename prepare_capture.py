import cv2
import numpy as np
import glob
import os
import argparse

parser = argparse.ArgumentParser(description='prepare captures for annotation')
parser.add_argument('--input_folder', help='the input folder', required=True)
parser.add_argument('--video_name', help='the top view video name ... e.g. view2-color.mp4', default="view2-color.mp4")
parser.add_argument('--ouput_folder_name', help='annotation data folder name. default: annotation_data', default="annotation_data")
args = parser.parse_args()

print(args.input_folder)
video_id = args.input_folder.split("/")
if len(video_id) > 1:
    video_id = video_id[-1]
else:
    video_id = video_id[0]

print("video id:", video_id)
print("load video:", f"{args.input_folder}/{args.video_name}")
cap = cv2.VideoCapture(f'{args.input_folder}/{args.video_name}')

if args.ouput_folder_name not in os.listdir(f'{args.input_folder}'):
    os.mkdir(f'{args.input_folder}/{args.ouput_folder_name}')
if "video" not in os.listdir(f'{args.input_folder}/{args.ouput_folder_name}'):
    os.mkdir(f'{args.input_folder}/{args.ouput_folder_name}/video')
    os.mkdir(f'{args.input_folder}/{args.ouput_folder_name}/video/{video_id}')
    with open(f'{args.input_folder}/{args.ouput_folder_name}/video_{video_id}.txt', "w") as f:
        f.write("URLID,URL\n")
        f.write(f"{video_id},{video_id}\n")

with open(f'{args.input_folder}/{args.ouput_folder_name}/frames_{video_id}.txt', "w") as f:
    f.write("URLID,Frame,Time\n")

    frame_number = 0
    while cap.isOpened():
        print("export frame:", frame_number)
        ret, frame = cap.read()
        if not ret:
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # cv2.imshow('frame', frame)

        frame_name = str(frame_number).zfill(12)
        frame_name = f"{frame_name}.jpg"

        frame = frame[:, 255:-305]  # crop to ROI
        # frame = cv2.resize(frame, (480, 480))  # resize img
        frame = cv2.resize(frame, (224, 224))  # resize img

        cv2.imwrite(f'{args.input_folder}/{args.ouput_folder_name}/video/{video_id}/{frame_name}', frame)
        f.write(f"{video_id},{frame_name},{frame_number}\n")

        frame_number += 1

cap.release()
cv2.destroyAllWindows()
