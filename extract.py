import cv2
from random import randint
import os
from tkinter import filedialog
# Read the video from specified path


def getPaths():
    fileName = filedialog.askopenfilename(filetypes=(("Videos", "*.mp4"), ("All files", "*.*")))
    dirName = filedialog.askdirectory()
    return fileName, dirName


def pullFrames(random_frames=50):
    video_path, folder_path = getPaths()
    cam = cv2.VideoCapture(video_path)
    number_of_frames = cam.get(cv2.CAP_PROP_FRAME_COUNT)
    successful_frames = 0
    if not os.path.exists(video_path):
        print("Video path not available for travel.")
        exit()
    if not os.path.exists(folder_path):
        print("Folder path not available for travel.")
    print(f"{number_of_frames} frames...")

    if random_frames >= number_of_frames:  # ensure we don't request more frames than available
        number_of_output_frames = number_of_frames-1
    else:
        number_of_output_frames = random_frames
    for i in range(number_of_output_frames):
        try:
            index = randint(0, number_of_frames-1)
            cam.set(1, index)
            success, frame = cam.read()
            name = folder_path + "\\frame" + str(index) + '.jpg'
            # writing the extracted images
            cv2.imwrite(name, frame)
            print(f'{i + 1}: Creating...' + name)
            successful_frames += 1
        except:
            print(f"ERROR saving frame {index}")
            continue
    print(f"Snagged {successful_frames}/{number_of_output_frames} frames! Have a great day captain.")
    # Release all space and windows once done
    cam.release()


pullFrames(60)
