from django.views.decorators import gzip
from django.http import StreamingHttpResponse
from django.views.generic import TemplateView

from turret.VideoCamera import VideoCamera


class HomeView(TemplateView):
    template_name = "turret/index.html"


def generate_frames(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@gzip.gzip_page
def video_feed(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(generate_frames(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:  # This is bad! replace it with proper handling
        pass
