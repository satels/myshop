from django.conf.urls import url, include
from django.contrib import admin
from ebay.views import complete

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^complete/', complete, name='myshope-complete'),
]
