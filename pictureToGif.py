from picamera import PiCamera
from time import sleep
from pathlib import Path
import imageio
import os
from gpiozero import Button
from signal import pause

def fileNum():
    '''
    Function to get the next file number from the gifs directory

    Parameters: 
        void

    Returns:
        int - next file number
    '''
    files = os.listdir('/home/pi/Documents/gifCamera/gifs')
    length = len(files)
    return length

def picCapture():
    '''
    Function to capture pictures using the PiCam module

    Parameters:
        Void
    
    Returns:
        Void
    '''
    print("Taking pictures")

    # Temp pictures, will change when 4 cameras are installed.
    for i in range(2):
        sleep(1)
        camera.capture('/home/pi/Documents/gifCamera/tempPic/test%s.jpg' % i)
    
    # Once pictures are captured, call the gifCreate function
    gifCreate()

def gifCreate():
    '''
    Function to take jpg images and converts them into a gif animation

    Parameters:
        Void

    Returns:
        Void
    '''
    print("Creating gif")
    # Images are temporarily stored in tempPic directory
    image_path = Path('tempPic')

    # Getting all images and adding them to a list for the imageio conversion
    images = list(image_path.glob('*.jpg'))
    image_list = []
    for file_name in images:
        image_list.append(imageio.imread(file_name))

    fileIndex = fileNum()
    imageio.mimwrite(f'gifs/{fileIndex}.gif', image_list)
    print("Gif created")

if __name__ == "__main__":
    # Assinging the GPIO pin that the button is connected to
    button = Button(2)

    # Creating a PiCamera instance. Follow 
    # https://projects.raspberrypi.org/en/projects/getting-started-with-picamera
    # to set up camera on a Raspberry Pi
    camera = PiCamera()

    # When the button is pressed, pictures are captured and a gif is created
    button.when_pressed = picCapture

    # Program paused waiting for the next signal
    pause()
