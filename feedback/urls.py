from django.urls import path
from . import views


urlpatterns = [
    path('', views.feedback_view, name='feedback_view'),
    path('feedback_received', views.feedback_received, name='feedback_received'),

]
