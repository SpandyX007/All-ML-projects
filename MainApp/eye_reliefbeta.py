import cv2
import mediapipe as mp
import time
import pyttsx3
import winsound

# cam=cv2.VideoCapture(0)
# face_mesh=mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
# engine = pyttsx3.init()
# start_time:int=int(time.time())
# # engine.say("It has been 5 seconds you are looking at the screen")

# # engine.runAndWait()

# while True:
#     _,frame=cam.read()
#     rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
#     output=face_mesh.process(rgb_frame)
#     frame_h,frame_w,_=frame.shape
#     landmark_points=output.multi_face_landmarks
#     # landmark_eye=landmarks[474:478]    #thorws error if no face is detected
#     # print(landmark_eye)
#     if landmark_points:
#         landmarks =landmark_points[0].landmark
#         for id, landmark in enumerate(landmarks[474:478]):
#             x=int(landmark.x*frame_w)
#             y=int(landmark.y*frame_h)
#             cv2.circle(frame,(x,y),3,(0,255,0))
#             if id==1:
#                 end_time:int=int(time.time())
#                 #couter for start and end timer
#                 # print("start time= ",start_time,"end_time= ",end_time)
#                 if end_time-start_time==12:
#                     # engine.say("It has been 12 seconds you are looking at the screen! Take a rest, look at some distant object for atleast 20 seconds")
#                     start_time=end_time
#         left=[landmarks[145],landmarks[159]]
#         for landmark in left:
#             x=int(landmark.x*frame_w)
#             y=int(landmark.y*frame_h)
#             cv2.circle(frame,(x,y),3,(0,255,255))
#         if (left[0].y-left[1].y)<0.009:
#             print("eyes closed")
#     engine.runAndWait()
#     cv2.imshow("Face tracker",frame)
#     cv2.waitKey(1)


def instantcapture():
    #calculate the fresh image of the face
    face_mesh=mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
    _,frame=cam.read()
    rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output=face_mesh.process(rgb_frame)
    landmark_points=output.multi_face_landmarks
    return landmark_points

def speak(line:str):
    engine.say(line)
    engine.runAndWait()


cam=cv2.VideoCapture(0)
face_mesh=mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
engine = pyttsx3.init()

start_time:int=int(time.time())
# engine.say("It has been 5 seconds you are looking at the screen")

while True:
    _,frame=cam.read()
    rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output=face_mesh.process(rgb_frame)
    frame_h,frame_w,_=frame.shape
    landmark_points=output.multi_face_landmarks
    print(landmark_points)
    if landmark_points!=None:
        end_time:int=int(time.time())
        if end_time-start_time==10*60:
            speak("It has been 10 minutes  you are looking at the screen continuously! Take a rest, look at some distant object for atleast 20 seconds")
            time.sleep(20) 
            landmark_points=instantcapture()
            # landmark_points=output.multi_face_landmarks
            # print("before while: ")
            # print(landmark_points)
            while(landmark_points!=None):
                speak("You are still looking at the screen! Please get your eyes off the screen for a while")
                time.sleep(10)
                #calculate the fresh image of the face
                # face_mesh=mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
                # _,frame=cam.read()
                # rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                # output=face_mesh.process(rgb_frame)
                # landmark_points=output.multi_face_landmarks
                landmark_points=instantcapture()
                # print("inside while: ")
                # print(landmark_points)
            else:
                # speak("Resume your work")
                start_time=end_time
    else:
        # winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)
        start_time:int=int(time.time())
    print("Starttime= ",start_time)
    print("Endtime= ",end_time)
    cv2.imshow("Face tracker",frame)
    cv2.waitKey(1)