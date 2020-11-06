import django.core.validators
from django.db import migrations, models
import localflavor.us.models




class Migration(migrations.Migration):
       
       initial = True 

       dependencies = [
           ('')
       ]
    
       operations = [
           migrations.CreateModel(
               name='Attorney',
               fields=[
                   ('user_name', models.CharField(max_lenght=255,null=True)),
                   ('user_type', models.CharField(max_lenght=255,null=True)),
               ],
           ),

       ],