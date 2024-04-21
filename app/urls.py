from django.urls import path
from . import views
from . import htmx_views

urlpatterns = [
    path("", views.index, name="index"),
    path('login/', views.login, name='login'),
    path('about/', views.about, name='about'),
    path('questions_add', views.questions_add, name='questions_add'),
    
]


# Urls para requests HTMX 
htmx_urlpatterns = [
    path('search_input/', htmx_views.search_input, name='search_input'),
    path('search_clear/', htmx_views.search_clear, name='search_clear'),
    path('submit_question/', htmx_views.submit_question, name='submit_question'),
    

]

urlpatterns += htmx_urlpatterns