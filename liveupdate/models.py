from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django import forms
# Create your models here.
class Update(models.Model):
    timestamp = models.DateTimeField(auto_now_add = True)
    text = models.TextField()
    
    class Meta:
        ordering = ['-id']
        
    def __unicode__(self):
        return "[%s] %s"%(self.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                         self.text)
        
admin.site.register(Update)

class Contact(models.Model):
    user = models.OneToOneField(User)
    address = models.CharField(max_length = 255)
    
    def __unicode__(self):
        return self.user.get_full_name()
    
    @property
    def first_name(self):
        return self.user.first_name
    
    @property
    def last_name(self):
        return self.user.last_name
    
    @property
    def get_full_name(self):
        return self.user.get_full_name()
    
admin.site.register(Contact)

class UserEditorForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')
        
class ContactEditorForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ('user',)