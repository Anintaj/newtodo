from . import views
from django.urls import path


app_name='todoapp'
urlpatterns = [
    path('', views.task, name='task'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvhome/',views.TasklistView.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.detailviewlist.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.taskupdateview.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.taskdeleteview.as_view(),name='cbvdelete')

]