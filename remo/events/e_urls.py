from django.conf.urls.defaults import *

urlpatterns = patterns('remo.events.views',
    url(r'^(?P<slug>[a-z0-9-]+)/$', 'view_event',
        name='events_view_event'),
    url(r'^(?P<slug>[a-z0-9-]+)/edit/$', 'edit_event',
        name='events_edit_event'),
    url(r'^(?P<slug>[a-z0-9-]+)/delete/$', 'delete_event',
        name='events_delete_event'),
    url(r'^(?P<slug>[a-z0-9-]+)/subscribe/$', 'manage_subscription',
        {'subscribe': True}, name='events_subscribe_to_event'),
    url(r'^(?P<slug>[a-z0-9-]+)/unsubscribe/$', 'manage_subscription',
        {'subscribe': False}, name='events_unsubscribe_from_event'),
    url(r'^(?P<slug>[a-z0-9-]+)/plusoneconverted/$',
        'count_converted_visitors',
        name='events_count_converted_visitors'),
)
