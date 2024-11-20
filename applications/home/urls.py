from django.urls import path
from. import views

urlpatterns = [
    path('home/', view,IndexView.as_view()),
]