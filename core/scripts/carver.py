from moviepy.editor import VideoFileClip
from progress.spinner import Spinner
from os import mkdir, path, system
import shutil
from numpy import arange


def carver(video_file, fps):
    video_clip = VideoFileClip(video_file)
    filename = "not_processed"
    image_folder = 'processed'
    try:
        shutil.rmtree("not_processed/")
        shutil.rmtree('processed/')
    except FileNotFoundError:
        mkdir(image_folder)
        mkdir(filename)
    saving_frames_per_second = min(video_clip.fps, fps)
    # если SAVING_FRAMES_PER_SECOND установлен в 0, шаг равен 1 / fps, иначе 1 / SAVING_FRAMES_PER_SECOND
    step = 1 / video_clip.fps if saving_frames_per_second == 0 else 1 / saving_frames_per_second
    spinner = Spinner('Extracting frames... ')
    for index, current_duration in enumerate(arange(0, video_clip.duration, step)):
        frame_filename = path.join(filename, f"{index}.jpg")
        video_clip.save_frame(frame_filename, current_duration)
        if index % 20 == 0:
            spinner.next()
    spinner.finish()