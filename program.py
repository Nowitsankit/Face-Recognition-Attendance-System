import face_recognition
import cv2
import numpy as np
import csv
import os
from datetime import datetime

# Initialize video capture
video_capture = cv2.VideoCapture(0)

# Load known image and get face encoding for Ankit
try:
    jobs_image = face_recognition.load_image_file("image/ankit.jpg")
    jobs_encoding = face_recognition.face_encodings(jobs_image)[0]
except (IndexError, FileNotFoundError) as e:
    print(f"Error loading image or encoding faces: {e}")
    exit()

# Store the known face encoding
known_face_encoding = [jobs_encoding]
known_face_names = ["Ankit"]

# Initialize variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
seen_names = set()

# CSV setup
csv_filename = "attendance.csv"
if not os.path.isfile(csv_filename):
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Timestamp"])

try:
    while True:
        ret, frame = video_capture.read()

        if process_this_frame:
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_frame = small_frame[:, :, ::-1]

            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encoding, face_encoding)
                name = "Unknown"

                if True in matches:
                    match_index = matches.index(True)
                    name = known_face_names[match_index]

                if name != "Unknown" and name not in seen_names:
                    seen_names.add(name)
                    with open(csv_filename, mode='a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([name, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])

                face_names.append(name)

        process_this_frame = not process_this_frame

        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    video_capture.release()
    cv2.destroyAllWindows()
