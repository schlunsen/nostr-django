from django.contrib import admin
from django.urls import path
from main import views
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings

router = routers.SimpleRouter()
router.register(r'users', views.Nip05UserViewSet)
router.register(r'cards', views.CardViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('.well-known/nostr.json', views.well_known),
    path('api/create/', views.create_registration),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += router.urls