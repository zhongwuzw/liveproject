from django.shortcuts import render
from django.views.generic.list import ListView
from liveupdate.models import Update
from django.views.generic.base import TemplateView
from django.http.response import HttpResponse
from django.core import serializers

# Create your views here.
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
            
    