# importing libararies
import cv2
from datetime import datetime

def record():
    # define video capture object
    cap = cv2.VideoCapture(0)

    # define the codec and create videowriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    store = cv2.VideoWriter(f'recording/{datetime.now().strftime("%H-%M-%S")}.avi', fourcc, 20.0, (640, 480))

    # loop runs if capturing has been initialized
    while True:

        # capture the video frame 
        # by frame
        # ret checks return at each frame 
        ret, frame = cap.read()

        # using cv2.putText() method
        cv2.putText(frame,f'{datetime.now().strftime("%D-%H-%M-%S")}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 0, 255), 2)

        # output the frame
        store.write(frame)

        # display the resulting frame
        cv2.imshow('Webcam', frame)

        # the 'q' button is set as the 
        # quitting button 
        if cv2.waitKey(1) & 0xFF == ord('q'):
            
            break

    # after the loop release the cap object
    cap.release()
    # destroy all the windows
    cv2.destroyAllWindows()