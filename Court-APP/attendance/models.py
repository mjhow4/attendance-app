from django.db import models



class Case(model.Model):
     file_number = models.CharField(max_length=255, null=True, blank=True)
     attorney = models.CharField(max_lenght=255,null=True, blank=True)
     court_date = models.CharField(max_lenght= 255,null=True, blank=True)
     court_session = models.CharField(max_lenght= 255,null=True, blank=True)
     plea_request = models.CharField (max_length= 255, null=True, blank=True)   

class Attorney(model.Model):
     attorney_name = models.Charfield(max_length=255, null=True)
     attorney_name = models.ForeignKey(Attorney,on_delete=models.CASCADE, null=True, related_name="notes")

     
class Plea(model.Model):
     date_requested = models.CharField(max_lenght=255,null=True)
     (Accepted_Deny)

class User(model.Model):
      user_name = models.CharField(max_lenght=255,null=True)
      user_type = models.CharField(max_lenght=255,null=True)

class NoteBox(models.Model):
    txt = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    contact = models.ForeignKey(Contact,on_delete=models.CASCADE, null=True, related_name="notes")

