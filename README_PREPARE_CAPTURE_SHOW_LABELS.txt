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

Annotate with coin_annotation_tool.html
Save labeled file as labeled_<capture_folder>.txt (e.g. labeled_01-background.txt) and place into the
"annotation_data" folder created by prepare_capture.py

run python show_labels.py --input_folder captures/01-background
This program automatically reads a labeled_<capture_folder>.txt file and visualizes the label