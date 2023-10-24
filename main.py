from model.model import predictor
from PIL import Image
from preprocess.video import separate_frames
import cv2
import sys
import os

def main(*args, **kwargs):
    videos_path = 'data/video/111.webm'
    frames_folder = 'data/frames'
    for i, (file, frame) in enumerate(separate_frames(video_path=videos_path, frames_folder=frames_folder)):
        is_watermarked = predictor.predict_image(Image.open(file))
        # is_watermarked = True
        print(f'Frame: {i} named {os.path.basename(file)}')
        if is_watermarked:
            file_watermarked = file.replace("/frames/", "/watermark/")
            print(f'WATERMARK FOUND on {i} frame named {os.path.basename(file_watermarked)}')
            cv2.imwrite(file_watermarked, frame)
            os.remove(file)
            if i > 100:
                sys.exit()
            

if __name__ == "__main__":
    main()