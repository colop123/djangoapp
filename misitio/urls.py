from django.conf.urls import include, url
from django.contrib import admin
from blog import urls

urlpatterns = [

    ur(r'', include('blog.urls'))
    url(r'^admin/', include(admin.site.urls)),
]
