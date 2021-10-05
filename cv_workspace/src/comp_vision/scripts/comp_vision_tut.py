#!/usr/bin/python
import cv2
import numpy as np
import sys

cap = cv2.VideoCapture("iceBall.mov") #0 argument access which webcam, 0 being first index
# or put the file name in the argument if you want it to open a video

while True:
    ret, frame = cap.read() #returns ret bool True if it works properly, frame the numpy array if the frame

    width = int(cap.get(3)) #get(3) gets the width of a frame
    height = int(cap.get(4)) #4 gets the height

    image = np.zeros(frame.shape, np.uint8) #create an image of black pixels the same size as the frame

    smallerFrame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5) #shrink the frame size by half

    image[:height//2, :width//2] = smallerFrame #Make the top left hand corner equal to the smaller frame
    #review numpy slicing
    image[height//2:, :width//2] = smallerFrame #bottom left, height starts at half and goes to end, width starts at zero and goes to half

    image[:height//2, width//2:] = cv2.rotate(smallerFrame, cv2.cv2.ROTATE_90_CLOCKWISE) #top right, rotated

    image[height//2:, width//2:] = cv2.rotate(smallerFrame, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE) #bottom right, rotated
    # BIGNOTE: I was able to rotate 90 degrees due to the 4 quarters having the same height and width values as in height = width
    # If that wasn't the case I wouldn't be able to rotate it 90 degrees but I could do it 180 degrees


    try:
        cv2.imshow('frame', image) #("name", variable)
    except:
        print("Video Ended")
        sys.exit()

    if cv2.waitKey(1) == ord('q'): #waitkey waits 1 milisec, if key is press returns the character or ord val of the key if q it quits
        break

cap.release()
cv2.destroyAllWindows() #allways end program with this
#TODO Watch episode 4

