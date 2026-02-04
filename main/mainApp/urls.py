from django.urls import path
from .views import chat_view

urlpatterns = [
    path("upload/", chat_view),
]
