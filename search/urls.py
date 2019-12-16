from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from django.contrib.staticfiles.urls import static

from search import views
from django.conf.urls import include
router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'products', views.ProductViewSet)


urlpatterns = [
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
    url(r'^api/prod/$',views.searchprod),
    url(r'^backend/', admin.site.urls),
]

