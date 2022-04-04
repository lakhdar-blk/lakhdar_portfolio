import os
import sys
import site
from django.core.wsgi import get_wsgi_application

# add python site packages, you can use virtualenvs also
site.addsitedir("C:\Users\lakhdar.belkharroubi\Desktop\MyPortfolio\env")

# Add the app's directory to the PYTHONPATH 
sys.path.append('C:\Users\lakhdar.belkharroubi\Desktop\MyPortfolio\env\myportf') 
#sys.path.append('')  

os.environ['DJANGO_SETTINGS_MODULE'] = 'myportf.settings' 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myportf.settings")  
 
application = get_wsgi_application()