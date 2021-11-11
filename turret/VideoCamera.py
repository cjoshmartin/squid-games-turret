import cv2
import threading

import face_recognition
import imutils

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = imutils.resize(self.frame, height=400)
        boxes = face_recognition.face_locations(image)
        encodings = face_recognition.face_encodings(image, boxes)

        bounding_box_color = (0, 0, 255)

        for (top, right, bottom, left) in boxes:
            # draw the predicted face name on the image - color is in BGR
            cv2.rectangle(image, (left, top), (right, bottom),
                          bounding_box_color, 2)
            y = top - 15 if top - 15 > 15 else top + 15
            cv2.putText(image, "Player", (left, y), cv2.FONT_HERSHEY_SIMPLEX,
                        .8, bounding_box_color, 2)

        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

