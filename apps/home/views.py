# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import cv2
import imutils
import time
import threading
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.http import StreamingHttpResponse


@login_required(login_url="/login/")
def index(request):
    
    
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

url=""

def video_feed():
    # Create a video capture object using the RTSP URL
    cap = cv2.VideoCapture("")
    try:
        while True:
            # Read the next frame from the video stream
            ret, frame = cap.read()
            if not ret:
                break

            # Convert the frame to a JPEG image
            ret, jpeg = cv2.imencode('.jpg', frame)
            frame = jpeg.tobytes()

            # Yield the frame in a HTTP response
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

        # Release the video capture object
        cap.release()
    except:
        return 0


# Define a view that returns a streaming HTTP response
@login_required(login_url="/login/")
def stream_video_uwtc(request):
    return StreamingHttpResponse(video_feed(), content_type='multipart/x-mixed-replace; boundary=frame')

def video_feed2():
    # Create a video capture object using the RTSP URL
    cap = cv2.VideoCapture("")

    while True:
        # Read the next frame from the video stream
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the frame to a JPEG image
        ret, jpeg = cv2.imencode('.jpg', frame)
        frame = jpeg.tobytes()

        # Yield the frame in a HTTP response
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    # Release the video capture object
    cap.release()


# Define a view that returns a streaming HTTP response
@login_required(login_url="/login/")
def stream_video_naxal(request):
    return StreamingHttpResponse(video_feed2(), content_type='multipart/x-mixed-replace; boundary=frame')

