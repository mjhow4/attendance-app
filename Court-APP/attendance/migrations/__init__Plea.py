import django.core.validators
from django.db import migrations, models
import localflavor.us.models




class Migration(migrations.Migration):
       
       initial = True 

       dependencies = [('Case')
       ]

       operations = [
           migrations.CreateModel(
               name='Plea',
               fields=[
                   ('date_requested',models.CharField(max_lenght=255,null=True)),
                    (Accepted_Deny))