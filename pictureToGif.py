from picamera import PiCamera
from time import sleep
from pathlib import Path
import imageio
import os


def fileNum():
    '''
    Function to get the next file number from the gifs directory

    Input: 
        void

    Return:
        int - next file number
    '''
    files = os.listdir('/home/pi/Documents/gifCamera/gifs')
    length = len(files)
    return length


if __name__ == "__main__":
    # Creating a PiCamera instance. Follow 
    # https://projects.raspberrypi.org/en/projects/getting-started-with-picamera
    # to set up camera on a Raspberry Pi
    camera = PiCamera()

    # Temp pictures
    for i in range(2):
        sleep(1)
        camera.capture('/home/pi/Documents/gifCamera/tempPic/test%s.jpg' % i)

    # Images are temporarily stored in tempPic directory
    image_path = Path('tempPic')

    # Getting all images and adding them to a list for the imageio conversion
    images = list(image_path.glob('*.jpg'))
    image_list = []
    for file_name in images:
        image_list.append(imageio.imread(file_name))

    fileIndex = fileNum()
    imageio.mimwrite(f'gifs/{fileIndex}.gif', image_list)
