import time

import imutils
import requests
import cv2

from django.http import HttpResponse
from django.views.generic import TemplateView
from imutils.video import VideoStream


class HomeView(TemplateView):
    template_name = "turret/index.html"


def video_feed(request):
    vs = VideoStream(src=0, framerate=10).start()
    time.sleep(2.0)

    frame = vs.read()
    frame = imutils.resize(frame, width=500)
    outputFrame = frame.copy()

    # encode the frame in JPEG format
    (flag, encodedImage) = cv2.imencode(".jpg", outputFrame)

    content = (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
               bytearray(encodedImage) + b'\r\n')

    vs.stop()
    response = HttpResponse(content, content_type="multipart/x-mixed-replace; boundary=frame")
    response['Content-Length'] = len(content)

    return response
