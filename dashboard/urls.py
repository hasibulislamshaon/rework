from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('',views.Ticket,name="Home page"),
    path('about/<slug:slug>/<int:id>',views.aboutTicket,name="about_ticket")
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)