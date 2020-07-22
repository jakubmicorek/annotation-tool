don't forget to source .venv3

python prepare_capture.py --input_folder <folder_to_captures>/<capture_folder>
e.g.
python prepare_capture.py --input_folder captures/01-background
will automatically create:
captures/01-background
  --annotation_data
    --video
      --01-background
          00000001.jpg
          00000002.jpg
          ....jpg
      frames_01-background.txt
      video_01-background.txt

If something fails, delete "annotation_data" folder within captures/01-background

The annotion tool requires the generated frames_<capture_folder>.txt and video_<capture_folder>.txt files
and the exportet frames as jpg from the annotiont_data folder.