from django.contrib import admin
from django.urls import path
from main import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users', views.Nip05UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('.well-known/nostr.json', views.well_known),
    path('api/create/', views.create_registration),
]

urlpatterns += router.urls