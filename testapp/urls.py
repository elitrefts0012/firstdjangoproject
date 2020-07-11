from django.urls import path
from . import views


urlpatterns = [
    path('', views.Courses, name='home-page'),
    path('<int:course_id>/', views.detail, name='detail'),
    path('box', views.box, name='box'),
    path('box_game', views.box_game, name='box_game'),

]