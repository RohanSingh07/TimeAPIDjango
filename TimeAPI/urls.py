from django.urls import path
from .views import *

app_name = "TimeAPI"

urlpatterns = [
    path('',homepage,name="homepage"),
    path('getTimeStories',getTimeStories,name="getTimeStories")
]
