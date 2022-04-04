import imp
from django.contrib import admin

from .models import ContactMessage, Publication, Degree, Exper

admin.site.register(ContactMessage)
admin.site.register(Publication)
admin.site.register(Degree)
admin.site.register(Exper)
