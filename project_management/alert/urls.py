"""
Url pattern for projectbudgegt application
"""

from django.conf.urls.defaults import patterns
from django.views.generic.simple import direct_to_template, redirect_to

urlpatterns = patterns('project_management.alert.views',   
    (r'^list/$', 'list'),
    (r'^edit/(?P<id>\w+\d+)/$', 'edit'),
    (r'^save/$', 'save'),
    (r'^preview/$', 'preview'),
    (r'^timesheet_report/$', 'pay_it_status'),
    (r'^sheet_report/$', 'sheet_report'),
    (r'^timesheet_xl/$', 'pay_it_status_days_genrte'),
    (r'^timesheet_hours/$', 'pay_it_status_hours_genrte'),
    (r'^task_report/$', 'task_report'),
    (r'^daily_report/$', 'daily_report'),
    (r'^activate/$', 'alert_status',{'status': True}, "activate-alert"),
    (r'^deactivate/$', 'alert_status',{'status': False}, "deactivate-alert"),
    (r'^project_report/$', 'project_report'),
    #(r'^get_perms/$', 'get_perms'),
)
