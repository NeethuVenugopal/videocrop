# Video Crop Tool

This tool allows you to crop a video by selecting a specific region of interest (ROI) in the video frames. The tool provides a graphical user interface (GUI) for selecting the ROI and saves the cropped video as an output file.

## Instructions

1. Download the `dist` folder from the repository.
2. Run the `videocrop.exe` executable file located inside the `dist` folder.

## Usage

1. Upon running the tool, a file dialog will appear.
2. Select the video file you want to crop.
3. A window will open displaying the first frame of the video.
4. Click and drag the mouse to select the region of interest (ROI) in the frame.
5. Release the mouse button to confirm the selection.
6. To reset the selection, press the 'r' key.
7. Press the 'c' key to confirm the ROI and proceed with cropping.
8. The cropped video will be saved in the same directory as the original video with the filename `original_filename_out.m4v`.
9. The cropped video will be displayed while cropping, and you can press the 'Esc' key to stop the cropping process and close the tool.

Note: The tool uses the H.264 codec for the output video, which may not be supported by all systems. 

## Requirements for running python code

- Python 3.x
- OpenCV
- tkinter
