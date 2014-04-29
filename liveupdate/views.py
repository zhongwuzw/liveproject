from django.shortcuts import render
from django.views.generic.list import ListView
from liveupdate.models import Update,Contact,ContactEditorForm,UserEditorForm
from django.views.generic.base import TemplateView
from django.http.response import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class HomeListView(ListView):
    template_name = 'update_list.html'
    model = Update
    context_object_name = 'update_list'
    
class UpdateAfterView(TemplateView):
    def get(self,request,**kwargs):
        if kwargs['id'] :
            response = HttpResponse()
            response['Content-Type'] = 'text/javascript'
            response.write(serializers.serialize("json", Update.objects.filter(pk__gt = kwargs['id'])))
            return response
      
class EditContact(TemplateView):
    def get_objects(self,username):
        if username:
            user = get_object_or_404(User,username = username)
            try:
                contact = user.contact
            except Contact.DoesNotExist:   
                contact = Contact(user = user)
        else:
            user = User()
            contact = Contact(user = user)
            
        return user,contact
    
    def get(self,request,username = None):
        user,contact = self.get_objects(username)
        
        return self.render_to_response({'username':username,
                                        'user_form':UserEditorForm(instance = user),
                                        'contact_form':ContactEditorForm(instance = contact),
                                        })
    
    def post(self,request,username = None):
        user,contact = self.get_objects(username)
        
        user_form = UserEditorForm(request.POST,instance = user)
        contact_form = ContactEditorForm(request.POST,instance = contact)
        
        if user_form.is_valid() and contact_form.is_valid():
            user = user_form.save()
            contact = contact_form.save(commit = False)
            contact.user = user
            contact.save()
            return HttpResponseRedirect(reverse('contact_detail',kwargs = {'slug':user.username}))
        
        return self.render_to_response({'username':username,'user_form':user_form,'contact_form':contact_form,})
        
            