from django.views.generic import TemplateView


from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
                       # url(r'^blog/', include('blog.urls')),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
                       url(r'personnel$', TemplateView.as_view(template_name='personnel.html'), name='personnel'),
                       url(r'employee$', TemplateView.as_view(template_name='employee.html'), name='employee'),
                       url(r'^admin/', include(admin.site.urls)),
                       )
