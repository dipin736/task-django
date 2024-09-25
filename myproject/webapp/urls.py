from django.urls import path
from webapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('submit/', views.submit_form, name='submit_form'),
    path('submissions/', views.submissions, name='submissions'),  
]
