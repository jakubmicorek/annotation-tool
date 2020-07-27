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
    print("capture folders:", sorted(os.listdir("/".join(video_id[:-1]))))
    video_id = video_id[-1]
else:
    video_id = video_id[0]

print("video id:", video_id)
print("load video:", f"{args.input_folder}/{args.video_name}")
cap = cv2.VideoCapture(f'{args.input_folder}/{args.video_name}')

file_name = f'{args.input_folder}/{args.ouput_folder_name}/labeled_{video_id}.txt'
print(file_name)
with open(file_name, "r") as f:
    print(f.readline())
    label_lines = [line.strip().split(",") for line in f]
    labels = {int(line[4]): line[3] for line in label_lines}

print("labels:", labels)
frame_number = 0
old_label = None
color_roll_idx = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    k = cv2.waitKey(1)
    if k & 0xFF == ord('q') or k == 27:
        break

    resize_scale = 0.25
    resize_scale = 1
    frame = frame[:, 255:-305]  # crop to ROI
    frame = cv2.resize(frame, (0, 0), fx=resize_scale, fy=resize_scale)  # resize img
    # print(frame.shape)

    label = labels[frame_number] if frame_number in labels else "no label"
    color = np.eye(3)[color_roll_idx % 3] * 255 if frame_number in labels else (255, 255, 255)
    frame = cv2.putText(frame, f"{label} {frame_number}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color)

    cv2.imshow('frame', frame)

    if frame_number not in labels:
        print("unlabeled frame:", frame_number)
        cv2.waitKey(0)

    if old_label != label:
        # cv2.waitKey(0)
        color_roll_idx += 1

    cv2.waitKey(50)
    # if frame_number > 680:
    #     cv2.waitKey(200)
    # else:
    #     cv2.waitKey(1)
    # cv2.waitKey(2)
    # cv2.waitKey(1)
    frame_number += 1
    old_label = label

cap.release()
cv2.destroyAllWindows()
