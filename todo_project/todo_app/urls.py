from .import views
from django.urls import path
app_name='todo_app'
urlpatterns = [
       path('',views.first_fun,name='first_fun'),
       path('delete/<int:id>/',views.delete,name='delete'),
       path('update/<int:id>/',views.update,name='update'),
       path('cbvhome/',views.task_listview.as_view(),name='cbvhome'),
       path('cbvdetail/<int:pk>/',views.task_detailview.as_view(),name='cbvdeatil'),
       path('cbvupdate/<int:pk>/',views.task_updateview.as_view(),name='cbvupdate'),
       path('cbvdelete/<int:pk>/',views.task_deleteview.as_view(),name='cbvdelete'),
]