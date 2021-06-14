from django.urls import path

from . import views  # to import all of our views

# craete namespace

app_name = 'polls'
urlpatterns = [

    # 1st param empty quotes means /polls,2nd param connect it to the view which is index view where views.index is our index function in views.py
    path('', views.index, name='index'),

    # path('results', views.detail, name='detail'),  # means /polls/result

    # means /polls/1 where 1 is question id
    # here name is url_name or pattern name
    #path('<int:question_id>', views.detail, name='detail'),
    path('<int:question_id>/', views.detail, name='detail'),


    # means /polls/1/results where 1 is question id
    path('<int:question_id>/results', views.results, name='results'),

    path('<int:question_id>/results', views.results, name='blogs'),

    path('<int:question_id>/vote/', views.vote, name='vote')
]
#Change for fun!