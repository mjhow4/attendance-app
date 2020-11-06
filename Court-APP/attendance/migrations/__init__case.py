import django.core.validators
from django.db import migrations, models
import localflavor.us.models




class Migration(migrations.Migration):
       
       initial = True 

       dependencies = [
           ('Case')
       ]

       operations = [
           migrations.CreateModel(
               name='Case',
               fields=[
                   ('file_number', models.CharField(blank=True, max_length=255, null=True)),
                   ('attorney', models.CharField(max_lenght=255,null=True, blank=True)),
                   ('court_date', models.CharField(max_lenght= 255,null=True, blank=True)),
                   ('court_session', models.CharField(max_lenght= 255,null=True, blank=True)),
                   ('plea_request', models.CharField (max_length= 255, null=True, blank=True)),
               ],   
           ),
       ]