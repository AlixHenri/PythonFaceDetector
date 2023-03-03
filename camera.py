#pip install opencv-python
#pip install mediapipe
import cv2
import mediapipe as mp

webcam = cv2.VideoCapture(0) 

solutionFaceDetection = mp.solutions.face_detection
recognizeFace = solutionFaceDetection.FaceDetection()
marking = mp.solutions.drawing_utils

while True:
    try:
        ret, frame = webcam.read()
        cv2.imshow('frame',frame)
    except:
        print('An unexpected error occurred while trying to executing the camera frame. Please try running the script again,')
        quit()
    
    faceList = recognizeFace.process(frame)

    if faceList.detections:
        for face in faceList.detections:
            marking.draw_detection(frame, face)
            
    cv2.imshow("Faces Detected", frame)

    if cv2.waitKey(1) == 27:#Use ESC to exit the camera window
        break
    
webcam.release()
cv2.destroyAllWindows()