from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'money_manager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^money/', include('money.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
