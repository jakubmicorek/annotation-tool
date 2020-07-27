import os

root = "captures/"
for folder in sorted(os.listdir(root)):
    os.system(f"python prepare_capture.py --input_folder {root}{folder}")
