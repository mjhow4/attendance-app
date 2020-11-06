import django.core.validators
from django.db import migrations, models
import localflavor.us.models

class Migration(migrations.Migration):
       
       initial = True 

       dependencies = [
           ('Case','Plea','Attorney')
       ]

       operations = [
           migrations.CreateModel(
               name='Attorney',
               fields=[
                   ('attorney_name', models.Charfield(max_length=255, null=True)),
                   ('attorney_name', models.ForeignKey(Attorney,on_delete=models.CASCADE, null=True, related_name="notes")),
               ],
           ),

       ],



    