from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('app.urls')),
    path('admin/', admin.site.urls),
    path('__reload__/', include('django_browser_reload.urls')),
    path("auth/", include("django.contrib.auth.urls")),

]
