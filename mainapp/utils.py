# import cv2
# from django.http import StreamingHttpResponse

# def generate_frames(rtsp_url):
#     cap = cv2.VideoCapture(rtsp_url)
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break
#         _, jpeg = cv2.imencode('.jpg', frame)
#         yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')
#     cap.release()
# def webcam_view(request):
#     return StreamingHttpResponse(generate_frames(), content_type='multipart/x-mixed-replace; boundary=frame')
