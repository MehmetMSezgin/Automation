import cv2

#create a variable , parameters file name/path or device index (most of devices it is 0 or -1)
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))    #this if dor saving the video
#this 640x480 you capture from WIDTH AND HEIGHT


while (True):
    ret, frame = cap.read()         #if frame is available this method will return true
    #ret is boolean variable , frame is avaiable or not
    if ret == True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        out.write(frame)                #out is instance of video writer

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)    #to make color grey
        cv2.imshow('frame', gray)    #if you want to capture is normal (not gray) so just change this variable to frame

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()