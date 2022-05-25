import numpy as np
import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh
import time

position = {
    "LEFT_EYE":[33, 7, 163, 144, 145, 153, 154, 155, 133, 246, 161, 160, 159, 158, 157, 173],
    "RIGHT_EYE": [263, 249, 390, 373, 374, 380, 381, 382, 362, 466, 388, 387, 386, 385, 384, 398]
}

import os
img_name = ""
for file in os.listdir("upload_img/input/A"):                                               # <-- FIND IMAGE NAME
    if file.endswith("png") or file.endswith("jpg"):
        img_name = file

drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
with mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1, min_detection_confidence=0.5) as face_mesh:
    image = cv2.imread("upload_img/input/A/" + img_name)                                    # <-- READING IMAGE HERE
    height, width = (256, 256)                                                              # <-- IMAGE SIZE
    results = face_mesh.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    if not results.multi_face_landmarks:
        print("Continue")
    annotated_image = image.copy()
    for face_landmarks in results.multi_face_landmarks:
        # get the left eye position
        left_eye = np.array(face_landmarks.landmark)[position["LEFT_EYE"]]
        max_x = left_eye[0].x
        min_x = left_eye[0].x
        max_y = left_eye[0].y
        min_y = left_eye[0].y
        for pt in left_eye[1:]:
            if pt.x < min_x:
                min_x = pt.x
            if pt.x > max_x:
                max_x = pt.x
            if pt.y < min_y:
                min_y = pt.y
            if pt.y > max_y:
                max_y = pt.y
        
        left_eye_center = round(np.mean([min_x, max_x]) * width), round(np.mean([min_y, max_y]) * height)
        
        # get the right eye position
        right_eye = np.array(face_landmarks.landmark)[position["RIGHT_EYE"]]
        max_x = right_eye[0].x
        min_x = right_eye[0].x
        max_y = right_eye[0].y
        min_y = right_eye[0].y
        for pt in right_eye[1:]:
            if pt.x < min_x:
                min_x = pt.x
            if pt.x > max_x:
                max_x = pt.x
            if pt.y < min_y:
                min_y = pt.y
            if pt.y > max_y:
                max_y = pt.y
        
        right_eye_center = round(np.mean([min_x, max_x]) * width), round(np.mean([min_y, max_y]) * height)
        
        # append the left and right eye location into the eye_test.txt
        file = "logs/eyemovement/eye_test.txt"                                                  # <-- EYE_TEST.TXT LOCATION
        with open(file, "w") as eye_test:
            eye_test.write(f"{img_name[:-4]} {int(left_eye_center[0])} {int(left_eye_center[1])} {int(right_eye_center[0])} {int(right_eye_center[1])}\n")