\# Face Recognition Attendance System



A Python-based real-time attendance system that uses computer vision and facial recognition to identify registered users through a webcam and automatically record attendance.



\## Features



\- Real-time face detection using OpenCV

\- Face recognition using the `face\_recognition` library

\- Webcam-based attendance tracking

\- Automatic attendance logging

\- Timestamped attendance records

\- Prevents duplicate attendance entries during a single execution

\- Unknown face detection



\## Technology Stack



\- Python

\- OpenCV

\- face\_recognition

\- NumPy

\- CSV

\- DateTime



\## How It Works



1\. The application starts the computer's webcam.

2\. A registered reference image is loaded.

3\. The reference image is converted into a facial encoding.

4\. Webcam frames are resized for faster processing.

5\. Faces are detected from the webcam frames.

6\. Detected faces are converted into facial encodings.

7\. The encodings are compared with the registered user's encoding.

8\. If a match is found, the user's name is displayed.

9\. Attendance is recorded with the current timestamp.

10\. Duplicate attendance is prevented during the same execution.

11\. Press `Q` to close the application.



\## Project Structure



```text

Face-Recognition-Attendance-System/

├── program.py

├── requirements.txt

├── .gitignore

├── README.md

└── image/

&#x20;   └── .gitkeep

