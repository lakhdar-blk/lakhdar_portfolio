from email import message
import imp
from re import I
from django.db import connection
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from django.views import View

#from .models import ContactMessage, Publication
from main_app import models

from django.core.mail import send_mail

from django.conf import settings

from django.core.paginator import Paginator


from django.template import RequestContext



class Home(View):

    def get(self, request):

        return render(request, 'home.html')


class SocialN(View):

    def get(self, request):

        return render(request, 'social_networks.html')


class About(View):

    def get(self, request):

        return render(request, 'about.html')


class Contact(View):

    def get(self, request):

        return render(request, 'contact.html')

    def post(self, request):
        
        email   = request.POST['email']
        name    = request.POST['name']
        message = request.POST['message']
        reason  = request.POST['reason']

        new_contact = models.ContactMessage.objects.create(email=email, full_name=name, reason=reason, message=message)

        if(new_contact):
                sent_status = True

        send_mail(reason, "Mail from "+email+", \n"+message, settings.DEFAULT_FROM_EMAIL, ['mnsfcb@gmail.com'])


        
        data = {
            'sentv': sent_status,
        }

        return render(request, 'contact.html', data)


class Publications(View):

    def get(self, request):

        publications = models.Publication.objects.all().order_by("-id")
        paginator = Paginator(publications, 3)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        data = {
            'publications': publications,
            'page_obj': page_obj
        }
        
        return render(request, 'publications.html', data)


class Degree_view(View):

    def get(self, request):

        degrees = models.Degree.objects.all()
        
        paginator = Paginator(degrees, 3)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        data = {
            'degrees': degrees,
            'page_obj': page_obj
        }


        return render(request, 'degrees.html', data)

class Exper(View):

    def get(self, request):

        experiences = models.Exper.objects.all()

        paginator = Paginator(experiences, 3)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        data = {
            
            'page_obj': page_obj
        }

        return render(request, 'exper.html', data)



def error_404(request, exception):
    return render(request, '404.html')

