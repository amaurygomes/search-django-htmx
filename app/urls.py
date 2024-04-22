from django.urls import path
from . import views
from . import htmx_views

urlpatterns = [
    path("", views.index, name="index"),
    path('login/', views.login, name='login'),
    path('about/', views.about, name='about'),
    path('import_csv/', views.import_csv, name='import_csv'),
    path('questions_add', views.questions_add, name='questions_add'),
    path('questions/', views.list_questions, name='list_questions'),
    path('questions/delete/<int:question_id>/', views.delete_question, name='delete_question'),
    
    
]


# Urls para requests HTMX 
htmx_urlpatterns = [
    path('search_input/', htmx_views.search_input, name='search_input'),
    path('search_clear/', htmx_views.search_clear, name='search_clear'),
    path('submit_question/', htmx_views.submit_question, name='submit_question'),
    path('upload_csv/', htmx_views.upload_csv, name='upload_csv'),
    

]

urlpatterns += htmx_urlpatterns