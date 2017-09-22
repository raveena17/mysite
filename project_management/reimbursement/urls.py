"""
Url pattern for Reimbursement application
"""

from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template, redirect_to

uuid_regex = '[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}'

urlpatterns = patterns('project_management.reimbursement.views',
    url(r'^create/$', 'create',name="create"),
    url(r'^list/$', 'list',name="list"),
    url(r'^save/$', 'save',name="save"),    
    )
