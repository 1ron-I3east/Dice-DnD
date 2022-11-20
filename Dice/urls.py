from django.urls import path
from . import views
urlpatterns = [
    path('', views.dice_view.as_view(), name="home"),

    
]
    # path('download/', views.download.download_file)