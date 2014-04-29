from django.conf.urls import patterns, include, url
from liveupdate.views import HomeListView,UpdateAfterView,EditContact
from django.contrib import admin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from liveupdate.models import Contact
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'liveproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',HomeListView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^updates-after/(?P<id>\d+)/$',UpdateAfterView.as_view()),
    url(r'^contact/$',ListView.as_view(queryset = Contact.objects.all(),
                                       template_name = 'list.html',
                                       paginate_by = 10),name = 'contact_list',),
    url(r'^contact/add/$',EditContact.as_view(template_name = 'editor_form.html',),name = 'contact_add_form'),
    url(r'^contact/(?P<slug>[\w-]+)/$',DetailView.as_view(queryset = Contact.objects.all(),
                                                          slug_field = 'user__username',
                                                          template_name = 'detail.html'),
        name = 'contact_detail'),
    url(r'^contact/(?P<username>[\w-]+)/edit/$',EditContact.as_view(template_name = 'editor_form.html',),
        name = 'contact_edit_form'),                    
)
