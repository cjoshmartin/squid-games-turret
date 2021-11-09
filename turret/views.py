from django.http import HttpResponse
from django.views.generic import TemplateView
import requests


# Create your views here.


class HomeView(TemplateView):
    template_name = "turret/index.html"


def video_feed(request):
    encodedImage = "https://cdn.memes.com/up/48152831613759157/i/1636247739238.jpg"
    request = requests.get(encodedImage)

    content = (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
     bytearray(request.content) + b'\r\n')

    response = HttpResponse(content, content_type="multipart/x-mixed-replace; boundary=frame")
    response['Content-Length'] = len(content)

    return response
