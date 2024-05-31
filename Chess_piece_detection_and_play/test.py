import cv2

# URL of the video feed from the IP camera app
# video_url = 'http://192.168.1.135:4747/video'
video_url = 'http://10.13.0.63:4747/video' #ta3 fac
# Open a connection to the video feed

cap=cv2.VideoCapture(video_url)
flag,img=cap.read()
cv2.imshow('Phone Camera', img)
print("Press any key for the next frame : ")
while True:
    # Read a frame from the video feed
    flag,img=cap.read()
    # If frame reading was successful, display the frame
    if cv2.waitKey(1) == 13:
        print("Press any key for the next frame : ")
        if flag:
            cv2.imshow('Phone Camera', img)
        else:
            print("Error: Could not read frame")
            break

    # Exit loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
