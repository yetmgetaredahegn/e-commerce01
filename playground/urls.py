from django.urls import path
from . import views

# URLConf
urlpatterns = [
    # path('hello/', views.say_hello).
    path('hello/', views.HelloView.as_view())
]
