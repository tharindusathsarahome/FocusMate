import argparse
from camera_functions import start_camera, resize_frame, detect_faces
from pomodoro_functions import play_alarm, stop_alarm, spent
import time
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-w", "--window", type=bool, default=False, help="Camera Window")
args = vars(ap.parse_args())

net = cv2.dnn.readNetFromCaffe("data/deploy.prototxt.txt", "data/res10_300x300_ssd_iter_140000.caffemodel")

vs = start_camera()
time.sleep(2.0)

round_completed = False
start_time = int(time.time())
timer_reset_start = 0

PomodoroTime = 1500
IntervalTime = 300

def capture_window():
    while True:
        frame = vs.read()
        frame = resize_frame(frame)
    
        detections, (h, w) = detect_faces(frame, net)

        for i in range(0, detections.shape[2]):
            confidence = detections[0, 0, i, 2]

            if confidence < 0.5:
                continue

            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
    
            text = "{:.2f}%".format(confidence * 100)
            y = startY - 10 if startY - 10 > 10 else startY + 10
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 0, 255), 2)
            cv2.putText(frame, text, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
    
        if (cv2.waitKey(30) & 0xff)==27:  break

    cv2.destroyAllWindows()
    vs.stop()

def availability():
    total_confidence = 0
    for _ in range(5):
        frame = vs.read()
        frame = resize_frame(frame)

        detections, _ = detect_faces(frame, net)

        for i in range(0, detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > 0.5:  total_confidence += confidence
        
        time.sleep(2)

    total_confidence = int(total_confidence * 20)
    print("Available" if total_confidence > 40 else "Not Available", total_confidence, "%")
    return 1 if total_confidence > 40 else 0

if args["window"]:
    capture_window()
else:
    while True:
        available = availability()
        if not round_completed and spent(PomodoroTime, start_time):
            round_completed = True
            start_time = int(time.time())
            play_alarm("data/Pomodoro.mp3")
            print("Round Completed")

        if round_completed and not available:
            stop_alarm()

        if round_completed and spent(IntervalTime, start_time):
            round_completed = False
            start_time = int(time.time())
            play_alarm("data/IntervalFinished.mp3")
            print("Round Again")

        if not round_completed and available:
            stop_alarm()
            timer_reset_start = 0

        if not round_completed and not available:
            if not timer_reset_start:
                timer_reset_start = int(time.time())
                print("Resetting Timer Started")
            elif int(time.time()) - timer_reset_start > IntervalTime:
                start_time = int(time.time())
                print("Timer Resetted !")

        time.sleep(10)
