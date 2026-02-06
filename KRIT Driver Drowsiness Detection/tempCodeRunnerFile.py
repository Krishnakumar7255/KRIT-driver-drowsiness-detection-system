import cv2
import mediapipe as mp
import serial
import time
import math

# -------------------- Arduino Setup --------------------
try:
    arduino = serial.Serial('COM7', 9600, timeout=1)
    time.sleep(2)  # allow Arduino to reset
except Exception as e:
    print("⚠️ Could not connect to Arduino:", e)
    arduino = None

# -------------------- Mediapipe Setup --------------------
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("⚠️ Camera not accessible")
    exit()

# -------------------- Constants --------------------
LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]
EAR_THRESH = 0.25        # Eye Aspect Ratio threshold
PERSIST_MS = 1000        # Minimum duration (ms) to confirm closed eyes
closed_since = None

# -------------------- Helper Functions --------------------
def euclidean(p1, p2, w, h):
    """Distance between two normalized landmarks scaled to image size."""
    return math.sqrt((p1.x*w - p2.x*w)**2 + (p1.y*h - p2.y*h)**2)

def ear(landmarks, idx, w, h):
    """Calculate Eye Aspect Ratio (EAR) using 6 landmarks."""
    v1 = euclidean(landmarks[idx[1]], landmarks[idx[5]], w, h)
    v2 = euclidean(landmarks[idx[2]], landmarks[idx[4]], w, h)
    h1 = euclidean(landmarks[idx[0]], landmarks[idx[3]], w, h)
    return (v1 + v2) / (2.0 * h1)

def detect_eye_state(landmarks, w, h):
    """Return 'O' (open) or 'C' (closed) based on EAR of both eyes."""
    global closed_since
    left_val = ear(landmarks, LEFT_EYE, w, h)
    right_val = ear(landmarks, RIGHT_EYE, w, h)
    avg_val = (left_val + right_val) / 2

    if avg_val < EAR_THRESH:
        if closed_since is None:
            closed_since = time.time()
        if (time.time() - closed_since) * 1000 >= PERSIST_MS:
            return 'C'
    else:
        closed_since = None
    return 'O'

def send_to_arduino(state):
    """Send state to Arduino if connected."""
    if arduino:
        try:
            arduino.write(state.encode())
        except Exception as e:
            print("⚠️ Error writing to Arduino:", e)

# -------------------- Main Loop --------------------
while True:
    ret, frame = cap.read()
    if not ret:
        print("⚠️ Frame capture failed")
        break

    h, w = frame.shape[:2]
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    res = face_mesh.process(rgb)

    if res.multi_face_landmarks:
        lms = res.multi_face_landmarks[0].landmark
        state = detect_eye_state(lms, w, h)

        # Draw eye landmarks for debugging
        for idx in LEFT_EYE + RIGHT_EYE:
            x, y = int(lms[idx].x * w), int(lms[idx].y * h)
            cv2.circle(frame, (x, y), 2, (255, 0, 0), -1)
    else:
        state = 'N'  # No face detected

    send_to_arduino(state)

    # Display state on screen
    if state == 'O':
        text, color = "OPEN", (0, 255, 0)
    elif state == 'C':
        text, color = "CLOSED", (0, 0, 255)
    else:
        text, color = "NO FACE", (255, 255, 0)

    cv2.putText(frame, text, (30, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    cv2.imshow('Driver Monitor', frame)

    # Exit on ESC key
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()