from picamera import PiCamera
from time import sleep
from pathlib import Path
import imageio
import os


def fileNum():
    '''
    Function to get the next file number from the gifs directory

    Input: Void

    Return:
        int - next file number
    '''
    files = os.listdir('/home/pi/Documents/gifCamera/gifs')
    length = len(files)
    return length


if __name__ == "__main__":
    camera = PiCamera()

    for i in range(2):
        sleep(1)
        camera.capture('/home/pi/Documents/gifCamera/tempPic/test%s.jpg' % i)

    image_path = Path('tempPic')
    images = list(image_path.glob('*.jpg'))
    image_list = []
    for file_name in images:
        image_list.append(imageio.imread(file_name))

    fileIndex = fileNum()
    imageio.mimwrite(f'gifs/{fileIndex}.gif', image_list)
