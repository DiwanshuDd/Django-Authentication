from django . views .decorators import gzip
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
# from .models import Stream
# from django.utils import timezone
from datetime import datetime
import cv2
from django.views.generic import TemplateView
import threading
from django.views.decorators import gzip
   
from . forms import *
# from .forms import LoginForm, UserRegistrationForm
# from django.contrib.auth import views as  login
from django.contrib.auth import authenticate, login
import os
from django.urls import reverse_lazy
import cv2
# from django.views.decorators.http import require_POST
# from django.views.decorators.csrf import csrf_exempt
from django.http import StreamingHttpResponse

 

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponse,HttpResponseForbidden
from mainapp.camera import VideoCamera
from .models import Camera
from .models import Attendance
from .models import EmployeeAttendance
from ultralytics import YOLO
import cvzone
 
import threading
 
 

# Create your views here.
@login_required
 
# def dashboard(request):
#     return render(request,'registration/dashboard.html',{'section':'dashboard'})
def register(request):
    if request.method =='POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html',{'user_form':user_form})



# def webcam_view(request):
#     return render(request, 'registration\webcam.html')
            

class LoginView():
    form_class = LoginForm
    success_url = reverse_lazy('home/')
    template_name = 'registration/login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)

# def LoginView(request):
#     form = LoginForm
#     return render(request, "registration/login.html", {'form':form, 'data':"name"})
     

def signup_View(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')  # Redirect to the login page
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
# @gzip.gzip_page
def home(request):
    
    rtsp_url = "rtsp://security:MoreYeahs465@192.168.3.14"  # Replace this with your actual RTSP URL
    return render(request, 'registration/home.html', {'rtsp_url': rtsp_url})
    
     

     
     
    # cap = cv2.VideoCapture(rtsp_url)
    # while True:
    #     ret, frame = cap.read()
    #     if not ret:
    #         break
    #     _, jpeg = cv2.imencode('.jpg', frame)
    #     yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')

    # cap.release()
    

# def video_feed(request):
#     return StreamingHttpResponse(home(), content_type='multipart/x-mixed-replace; boundary=frame')
    # try:
    #     cam = VideoCamera()
    #     return StreamingHttpResponse(gen(cam), mimetype="multipart/x-mixed-replace;boundary=frame")
    # except:
    #     pass
    # print("this page is call from views")
    # return render(request,"registration/home.html",{})
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('registration/home.html')  # Redirect to the home page after successful login
        else:
            return HttpResponse("Invalid login credentials")
    
    return render(request, 'registration/login.html')
# class VideoCamera(object):
#     def __init__(self):
#         self.video = cv2.VideoCapture(0)
             
#         (self.grabbed, self.frame) = self.video.read()
#         threading.Thread(target=self.update, args=()).start()

#     def __del__(self):
#         self.video.release()

#     def get_frame(self):
#         image = self.frame
#         _, jpeg = cv2.imencode('.jpg', image)
#         return jpeg.tobytes()

#     def update(self):
#         while True:
#             (self.grabbed, self.frame) = self.video.read()
def stream(request):
    rtsp_link = "rtsp://security:MoreYeahs465@192.168.3.14"
    cap = cv2.VideoCapture(rtsp_link)

    def generate_frames():
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            ret, jpeg = cv2.imencode('.jpg', frame)
            frame_bytes = jpeg.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n\r\n')
    

    return StreamingHttpResponse(generate_frames(), content_type="multipart/x-mixed-replace;boundary=frame")


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
def generate_frames():
    rtsp_url = "rtsp://security:MoreYeahs465@192.168.3.14"
    cap = cv2.VideoCapture(rtsp_url)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        _, jpeg = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')

    cap.release()
    
     
def webcam_view(request):
      from django . views .decorators import gzip
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
# from .models import Stream
# from django.utils import timezone
import cv2
from django.views.generic import TemplateView
import threading
   
from . forms import *
# from .forms import LoginForm, UserRegistrationForm
# from django.contrib.auth import views as  login
from django.contrib.auth import authenticate, login
import os
from django.urls import reverse_lazy
import cv2
# from django.views.decorators.http import require_POST
# from django.views.decorators.csrf import csrf_exempt
from django.http import StreamingHttpResponse
import torch

 

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponse,HttpResponseForbidden
from mainapp.camera import VideoCamera
from .models import Camera
# from mainapp.utils import generate_frames 
 
import threading
 
 

# Create your views here.
@login_required
 
# def dashboard(request):
#     return render(request,'registration/dashboard.html',{'section':'dashboard'})
def register(request):
    if request.method =='POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html',{'user_form':user_form})



# def webcam_view(request):
#     return render(request, 'registration\webcam.html')
            

class LoginView():
    form_class = LoginForm
    success_url = reverse_lazy('home/')
    template_name = 'registration/login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)

# def LoginView(request):
#     form = LoginForm
#     return render(request, "registration/login.html", {'form':form, 'data':"name"})
     

def signup_View(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')  # Redirect to the login page
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
# @gzip.gzip_page
def home(request):
    
    rtsp_url = "rtsp://security:MoreYeahs465@192.168.3.14"  # Replace this with your actual RTSP URL
    return render(request, 'registration/home.html', {'rtsp_url': rtsp_url})
    
     

     
     
    # cap = cv2.VideoCapture(rtsp_url)
    # while True:
    #     ret, frame = cap.read()
    #     if not ret:
    #         break
    #     _, jpeg = cv2.imencode('.jpg', frame)
    #     yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')

    # cap.release()
    

# def video_feed(request):
#     return StreamingHttpResponse(home(), content_type='multipart/x-mixed-replace; boundary=frame')
    # try:
    #     cam = VideoCamera()
    #     return StreamingHttpResponse(gen(cam), mimetype="multipart/x-mixed-replace;boundary=frame")
    # except:
    #     pass
    # print("this page is call from views")
    # return render(request,"registration/home.html",{})
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('registration/home.html')  # Redirect to the home page after successful login
        else:
            return HttpResponse("Invalid login credentials")
    
    return render(request, 'registration/login.html')
# class VideoCamera(object):
#     def __init__(self):
#         self.video = cv2.VideoCapture(0)
             
#         (self.grabbed, self.frame) = self.video.read()
#         threading.Thread(target=self.update, args=()).start()

#     def __del__(self):
#         self.video.release()

#     def get_frame(self):
#         image = self.frame
#         _, jpeg = cv2.imencode('.jpg', image)
#         return jpeg.tobytes()

#     def update(self):
#         while True:
#             (self.grabbed, self.frame) = self.video.read()
def stream(request):
    rtsp_link = "rtsp://security:MoreYeahs465@192.168.3.14"
    cap = cv2.VideoCapture(rtsp_link)

    def generate_frames():
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            ret, jpeg = cv2.imencode('.jpg', frame)
            frame_bytes = jpeg.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n\r\n')
    

    return StreamingHttpResponse(generate_frames(), content_type="multipart/x-mixed-replace;boundary=frame")


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
def generate_frames():
    rtsp_url = "rtsp://security:MoreYeahs465@192.168.3.14"
    camera_url = "rtsp://security:MoreYeahs465@192.168.3.14"
    cap = cv2.VideoCapture(rtsp_url)
    camera = cv2.VideoCapture(camera_url)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        _, jpeg = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')

    cap.release()
 
@gzip.gzip_page
def webcam_stream(request):
     

    return StreamingHttpResponse(generate_frames(), content_type='multipart/x-mixed-replace; boundary=frame')
    
     
 
# def web(request):
#     return(request,"registration/hello.html",{})
def webcam_view(request):
    # Pass the RTSP URL to generate_frames function if needed
    # rtsp_url = 'your_rtsp_url'
    # frames = generate_frames(rtsp_url)
   return render(request, 'registration/webcam.html')

    
    
# def video_feed(request):
#     return render(request, "registration/webcam.html", {})
def services(request):
    return render(request, "registration/services.html",{})
def statistics(request):
    date = request.GET.get('date')

    # Filter attendance data for the given date
    attendance_data = EmployeeAttendance.objects.filter(check_in_time__date=date)

    # Process attendance data to count employees in different time ranges
    green_count = yellow_count = red_count = 0

    for attendance in attendance_data:
        check_in_time = attendance.check_in_time.time()
        if check_in_time < datetime.time(9, 30):
            green_count += 1
        elif datetime.time(9, 30) <= check_in_time < datetime.time(11, 30):
            yellow_count += 1
        else:
            red_count += 1

    return render(request, 'registration/statistics.html', {'green_count': green_count, 'yellow_count': yellow_count, 'red_count': red_count})
     

# from django.shortcuts import render

def stream_view(request):
    rtsp_url = "rtsp://security:MoreYeahs465@192.168.3.14"
    return render(request, 'registration/live.html', {'rtsp_url': rtsp_url})
# def generate_video_stream():
#     rtsp_url = "rtsp://security:MoreYeahs465@192.168.3.14"
#     cap = cv2.VideoCapture(rtsp_url)

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break
#         _, jpeg = cv2.imencode('.jpg', frame)
#         yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')

#     cap.release()
     

# def video_feed(request):
#     return StreamingHttpResponse(generate_video_stream(), content_type='multipart/x-mixed-replace; boundary=frame')
        
        

 
# def transmition(request):
#     try:
#         cam = VideoCamera()
#         return StreamingHttpResponse(gen(cam), mimetype="multipart/x-mixed-replace;boundary=frame")
#     except:
#         pass
    # return render(request, 'stream.html')


 


# class PlataformaView(TemplateView):
#     template_name = 'platforma.html'


# class StreamView(TemplateView):
#     template_name = 'home.html'

# @require_POST
# @csrf_exempt
# def start_stream(request):
#     """ This view is called when a stream starts.
#     """
#     stream = get_object_or_404(Stream, key=request.POST["name"])

#     # Ban streamers by setting them inactive
#     if not stream.user.is_active:
#         return HttpResponseForbidden("Inactive user")

#     # Don't allow the same stream to be published multiple times
#     if stream.started_at:
#         return HttpResponseForbidden("Already streaming")

#     stream.started_at = timezone.now()
#     stream.save()

#     # Redirect to the streamer's public username
#     return redirect(stream.user.username)


# @require_POST
# @csrf_exempt
# def stop_stream(request):
#     """ This view is called when a stream stops.
#     """
#     Stream.objects.filter(key=request.POST["name"]).update(started_at=None)
#     return HttpResponse("OK")
# def generate_frames(rtsp_url):
#     cap = cv2.VideoCapture(rtsp_url)
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break
#         yield frame
#     cap.release()

# # Example Django view
# from django.http import StreamingHttpResponse

# def strepam_rts(request):
#     rtsp_url = "rtsp://security:MoreYeahs465@192.168.3.14"
#     return StreamingHttpResponse(generate_frames(rtsp_url), content_type="multipart/x-mixed-replace; boundary=frame")
   
     
 
 
 


def web(request):
    return(request,"registration/hello.html",{})

    
    
# def video_feed(request):
#     return render(request, "registration/webcam.html", {})
 
def settings(request):
    return render(request, "registration/settings.html",{})

# from django.shortcuts import render

def stream_view(request):
    rtsp_url = "rtsp://security:MoreYeahs465@192.168.3.14"
    return render(request, 'registration/live.html', {'rtsp_url': rtsp_url})
def attendance_graph(request):
    attendance_data = Attendance.objects.all()  # You might want to filter this data
    context = {
        'attendance_data': attendance_data
    }
    return render(request, 'registration/statistics.html', context)
def gen_frames():
    camera_url = "rtsp://security:MoreYeahs465@192.168.3.14"
    cap = cv2.VideoCapture(camera_url)
    facemodel = torch.load(r"C:\Users\user\OneDrive - MoreYeahs IT Technologies Pvt Ltd\Desktop\django._T\project\Scripts\authentication\mainapp\yolov8n-face.pt")

    frame_skip = 4
    resize_width, resize_height = 1020, 720
    roi_x1, roi_y1, roi_x2, roi_y2 = 300, 100, 800, 600
    central_x = (roi_x1 + roi_x2) // 2
    central_y = (roi_y1 + roi_y2) // 2
    while True:
        for _ in range(frame_skip):
            cap.read()
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.resize(frame, (resize_width, resize_height))
        roi = frame[roi_y1:roi_y2, roi_x1:roi_x2]
        face_result = facemodel.predict(roi, conf=0.40)

        for info in face_result:
            parameters = info.boxes
            for box in parameters:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                h, w = y2 - y1, x2 - x1
                x1 += roi_x1
                y1 += roi_y1
                cvzone.cornerRect(frame, [x1, y1, w, h], l=9, rt=3)
        cv2.rectangle(frame, (roi_x1, roi_y1), (roi_x2, roi_y2), (0, 255, 0), 2)
        ret, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
def services(request):
    return render(request, "registration/services.html",{})
def video_feed(request):
    return StreamingHttpResponse(gen_frames(), content_type='multipart/x-mixed-replace; boundary=frame')
# def generate_video_stream():
#     rtsp_url = "rtsp://security:MoreYeahs465@192.168.3.14"
#     cap = cv2.VideoCapture(rtsp_url)

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break
#         _, jpeg = cv2.imencode('.jpg', frame)
#         yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')

#     cap.release()
     

# def video_feed(request):
#     return StreamingHttpResponse(generate_video_stream(), content_type='multipart/x-mixed-replace; boundary=frame')
        
        

 
# def transmition(request):
#     try:
#         cam = VideoCamera()
#         return StreamingHttpResponse(gen(cam), mimetype="multipart/x-mixed-replace;boundary=frame")
#     except:
#         pass
    # return render(request, 'stream.html')


 


# class PlataformaView(TemplateView):
#     template_name = 'platforma.html'


# class StreamView(TemplateView):
#     template_name = 'home.html'

# @require_POST
# @csrf_exempt
# def start_stream(request):
#     """ This view is called when a stream starts.
#     """
#     stream = get_object_or_404(Stream, key=request.POST["name"])

#     # Ban streamers by setting them inactive
#     if not stream.user.is_active:
#         return HttpResponseForbidden("Inactive user")

#     # Don't allow the same stream to be published multiple times
#     if stream.started_at:
#         return HttpResponseForbidden("Already streaming")

#     stream.started_at = timezone.now()
#     stream.save()

#     # Redirect to the streamer's public username
#     return redirect(stream.user.username)


# @require_POST
# @csrf_exempt
# def stop_stream(request):
#     """ This view is called when a stream stops.
#     """
#     Stream.objects.filter(key=request.POST["name"]).update(started_at=None)
#     return HttpResponse("OK")
# def generate_frames(rtsp_url):
#     cap = cv2.VideoCapture(rtsp_url)
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break
#         yield frame
#     cap.release()

# # Example Django view
# from django.http import StreamingHttpResponse

# def strepam_rts(request):
#     rtsp_url = "rtsp://security:MoreYeahs465@192.168.3.14"
#     return StreamingHttpResponse(generate_frames(rtsp_url), content_type="multipart/x-mixed-replace; boundary=frame"
 

   
     
 
 
 

