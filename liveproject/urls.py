from django.conf.urls import patterns, include, url
from liveupdate.views import HomeListView,UpdateAfterView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'liveproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',HomeListView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^updates-after/(?P<id>\d+)/$',UpdateAfterView.as_view()),
)
