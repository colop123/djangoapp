from django.conf.urls import include, url
from django.contrib import admin
from blog import urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
]
