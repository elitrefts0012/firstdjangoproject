from django.urls import path
from . import views


urlpatterns = [
    path('', views.projects, name='projects'),
    path('courses', views.Courses, name='course_list'),
    path('<int:course_id>/', views.detail, name='detail'),
    path('box', views.box, name='box'),
    path('box_game', views.box_game, name='box_game'),
    path('tank_game', views.tank_game, name='tank_game'),
]