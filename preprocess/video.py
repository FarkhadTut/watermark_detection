import cv2
import datetime
import os
import shutil 
import sys
import pathlib

def separate_frames(video_path, frames_folder):
    files = []
    cwd = os.getcwd()
    frames_folder = os.path.join(cwd, frames_folder)
    if not os.path.exists(frames_folder):
        os.makedirs(frames_folder)
    else:
        dir_path = pathlib.Path(frames_folder)
        shutil.rmtree(dir_path)
        os.makedirs(frames_folder)
    
    video = cv2.VideoCapture(video_path)
        # Get the video's frame rate.
    fps = video.get(cv2.CAP_PROP_FPS)

    # Start the video capture timer.

    while True:
        ret, frame = video.read()
        if not ret:
            break

        # Calculate the timestamp.
        timestamp = datetime.timedelta(seconds=video.get(cv2.CAP_PROP_POS_MSEC) / 1000)
        # Crop the frame into 4 equal pieces.
        height, width, channels = frame.shape
        half_height = height // 2
        half_width = width // 2

        # Crop the top left piece.
        top_left_crop = frame[:half_height, :half_width]

        # Crop the top right piece.
        top_right_crop = frame[:half_height, half_width:]

        # Crop the bottom left piece.
        bottom_left_crop = frame[half_height:, :half_width]

        # Crop the bottom right piece.
        bottom_right_crop = frame[half_height:, half_width:]

        # Save the cropped frames.
        for i in range(4):
            crop_num = i + 1
            filename = os.path.join(frames_folder, f"{timestamp}_{crop_num}.jpg")

            # Crop the frame based on the crop number.
            if crop_num == 1:
                cropped_frame = top_left_crop
            elif crop_num == 2:
                cropped_frame = top_right_crop
            elif crop_num == 3:
                cropped_frame = bottom_left_crop
            else:
                cropped_frame = bottom_right_crop

            # Save the cropped frame.
            cv2.imwrite(filename, cropped_frame)
            yield (filename, cropped_frame)

    video.release()
    
