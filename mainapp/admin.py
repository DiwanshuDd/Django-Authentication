from django.contrib import admin
from .models import Stream, MyExistingModel, LoginLog, PasswordResetRequest, Camera, Video, Employee, Attendance

@admin.register(Stream)
class StreamAdmin(admin.ModelAdmin):
    list_display = ('user', 'started_at', 'is_live')
    # You can customize further admin options like list_filter, search_fields, etc.

@admin.register(MyExistingModel)
class MyExistingModelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    # Add more admin options if needed

@admin.register(LoginLog)
class LoginLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'login_time')
    # Add more admin options if needed

@admin.register(PasswordResetRequest)
class PasswordResetRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'requested_at')
    # Add more admin options if needed

@admin.register(Camera)
class CameraAdmin(admin.ModelAdmin):
    list_display = ('name',)
    # Add more admin options if needed

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title',)
    # Add more admin options if needed

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    # Add more admin options if needed

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'is_present')
    # Add more admin options if needed


# Register your models here.
