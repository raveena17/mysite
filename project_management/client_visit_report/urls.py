from django.conf.urls.defaults import patterns
from django.views.generic.simple import direct_to_template, redirect_to

urlpatterns = patterns('project_management.client_visit_report',
    (r'^cvr/$', 'views.manage_cvr'),
    
)
