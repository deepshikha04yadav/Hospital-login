# from django.contrib import admin
# from django.urls import path, include
# from . import views

# urlpatterns = [
#     path('', views.home, name="home"),
# ]

# from django.conf import settings
# from django.conf.urls.static import static


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from .views import *

urlpatterns = [
    path('', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('patient-dashboard/', patient_dashboard, name='patient_dashboard'),
    path('doctor-dashboard/', doctor_dashboard, name='doctor_dashboard'),
]
