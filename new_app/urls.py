from django.urls import path

from new_app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('todo',views.todo,name='Todo'),
    path('data',views.views_todo,name='views_todo'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update')

]