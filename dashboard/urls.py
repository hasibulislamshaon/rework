from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('',views.Ticket),
    path('about_ticket/',views.aboutTicket, name='about_ticket')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)