from django.db import models



class Case(model.Model):
     case_number = models.CharField(max_length=255, null=True, blank=True)
     defendant_name = models.CharField(max_lenght=255,null=True, blank=True)
     complaiant = models.CharField(max_lenght= 255,null=True, blank=True)
     Attorney = models.CharField(max_lenght= 255,null=True, blank=True)
     Cont = models.CharField (max_length= 255, null=True, blank=True)   



class NoteBox(models.Model):
    txt = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    contact = models.ForeignKey(Contact,on_delete=models.CASCADE, null=True, related_name="notes")
