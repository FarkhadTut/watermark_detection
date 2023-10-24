import cv2
import datetime

def split_video(video_file_path, output_dir_path, n_cuts):
    """Splits a video into n cuts.

    Args:
        video_file_path: The path to the video file.
        output_dir_path: The path to the directory where the output video clips will be saved.
        n_cuts: The number of cuts to make in the video.

    Returns:
        A list of paths to the output video clips.
    """

    # Open the video file.
    video = cv2.VideoCapture(video_file_path)

    # Get the video's frame rate and duration.
    fps = video.get(cv2.CAP_PROP_FPS)
    duration = video.get(cv2.CAP_PROP_FRAME_COUNT) / fps

    # Calculate the cut intervals.
    cut_intervals = [i * duration / n_cuts for i in range(1, n_cuts + 1)]

    # Create a list to store the paths to the output video clips.
    output_video_clip_paths = []

    # Iterate over the cut intervals and split the video at each interval.
    for i in range(len(cut_intervals) - 1):
        start_time = cut_intervals[i]
        end_time = cut_intervals[i + 1]

        # Create a video writer object for the output video clip.
        output_video_clip_path = os.path.join(output_dir_path, f"video_clip_{i}.mp4")
        output_video_writer = cv2.VideoWriter(output_video_clip_path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (video.get(cv2.CAP_PROP_FRAME_WIDTH), video.get(cv2.CAP_PROP_FRAME_HEIGHT)))

        # Seek to the start time of the cut interval.
        video.set(cv2.CAP_PROP_POS_MSEC, start_time * 1000)

        # Write the video frames in the cut interval to the output video clip.
        while True:
            ret, frame = video.read()
            if not ret or video.get(cv2.CAP_PROP_POS_MSEC) > end_time * 1000:
                break

            output_video_writer.write(frame)

        # Release the video writer object.
        output_video_writer.release()

        # Add the path to the output video clip to the list.
        output_video_clip_paths.append(output_video_clip_path)

    # Release the video capture object.
    video.release()

    return output_video_clip_paths

# Example usage:

video_file_path = "111.webm"
output_dir_path = "data/split_video"
n_cuts = 3

# Split the video into 3 cuts.
output_video_clip_paths = split_video(video_file_path, output_dir_path, n_cuts)

# Print the paths to the output video clips.
for output_video_clip_path in output_video_clip_paths:
    print(output_video_clip_path)
