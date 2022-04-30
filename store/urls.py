from django.urls import path
from . views import listing_view

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('listing/', listing_view, name='listing')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)