from django.urls import path

from . import views  # to import all of our views

# craete namespace

app_name = 'polls'
urlpatterns = [

    # 1st param empty quotes means /polls,2nd param connect it to the view which is index view where views.index is our index function in views.py
    path('', views.index, name='index'),
    path('result', views.index, name='index')  # means /polls/result
]
