import imp
from django.urls import path
from main_app.views import Home, SocialN, About, Contact, Publications, Degree_view, Exper
from django.conf.urls import handler404

urlpatterns = [
    path('', Home.as_view(), name="HOME"),
    path('social_networks/', SocialN.as_view(), name="SOCIAL"),
    path('about/', About.as_view(), name="ABOUT"),
    path('contact/', Contact.as_view(), name="CONTACT"),
    path('publications/', Publications.as_view(), name="PUBLICATIONS"),
    path('degrees/', Degree_view.as_view(), name="DEGREE"),
    path('exper/', Exper.as_view(), name="EXPER"),
]

handler404 = 'main_app.views.error_404'