from django.shortcuts import render
from django.http import StreamingHttpResponse, HttpResponse
from .script.GetHand import V_Camera2, to_gen2, hand_video
from .script.camera import VideoCamera, gen
from .script.mixed import V_Camera, to_gen
from products.models import Product
# Create your views here.


def home_view(request, *args, **kwargs):
    queryset = Product.objects.all()  # list of objects
    context = {
        "object_list": queryset,
        "times": 0
    }
    return render(request, "home.html", context)  # 從名為home.html模板中抓取此頁應有樣貌


def about_view(request, *args, **kwargs):
    return render(request, "about.html")


def threed_model_view(request):
    queryset = Product.objects.all()  # list of objects
    context = {
        "object_list": queryset,
        "times": 0
    }
    return render(request, "3D_model/3d_js.html", context)


def button(request):
    return render(request, 'get_hand_button.html')


# def get_hand(request):
#
#     return render(request, 'get_hand.html')
    # return HttpResponse(request, 'get_hand.html')


def get_hand(request):
    vid = StreamingHttpResponse(to_gen2(V_Camera2(), False), content_type='multipart/x-mixed-replace; boundary=frame')
    return vid


def hand_control(request):
    vid = StreamingHttpResponse(to_gen(V_Camera(), False), content_type='multipart/x-mixed-replace; boundary=frame')
    return vid


# ~~~~ outside ~~~~

def video_stream(request):
    vid = StreamingHttpResponse(gen(VideoCamera(), False), content_type='multipart/x-mixed-replace; boundary=frame')
    return vid


def mediapipe_view(request):
    return render(request, 'mediapipe.html')


# def video_input(request):
#     return render(request, 'med_hand.html')

