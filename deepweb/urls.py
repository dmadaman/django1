
from django.conf.urls import url, include
from django.contrib import admin
from adduser import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^adduser/',views.get_name, name='get_name'),
    url(r'^greet/',views.greet, name='greet'),
]
