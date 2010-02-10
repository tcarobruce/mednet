from django.conf.urls.defaults import *
from piston.resource import Resource
from piston_api.handlers import *
from piston.authentication import OAuthAuthentication

auth = OAuthAuthentication()

incomingsms_handler = Resource(IncomingSmsHandler, authentication=auth)
outgoingsms_handler = Resource(OutgoingSmsHandler, authentication=auth)
hospital_handler = Resource(HospitalHandler, authentication=auth)
hospital_activity_handler = Resource(HospitalActivityHandler, authentication=auth)
hospital_bed_capacity_handler = Resource(HospitalBedCapacityHandler, authentication=auth)
hospital_contact_handler = Resource(HospitalContactHandler, authentication=auth)
hospital_image_handler = Resource(HospitalImageHandler, authentication=auth)
hospital_request_handler = Resource(HospitalRequestHandler, authentication=auth)
hospital_resource_handler = Resource(HospitalResourceHandler, authentication=auth)
hospital_service_handler = Resource(HospitalServiceHandler, authentication=auth)
hospital_status_handler = Resource(HospitalStatusHandler, authentication=auth)

urlpatterns = patterns('',
	url(r'^insms/(?P<message_id>\d+)/$', incomingsms_handler),
	url(r'^insms/$', incomingsms_handler),
	
	url(r'^outsms/(?P<message_date>[0-9]*\.?[0-9]*)/$', outgoingsms_handler),
	url(r'^outsms/$', outgoingsms_handler),

	url(r'^hospital/(?P<hospital_id>\d+)/$', hospital_handler),
	url(r'^hospital/$', hospital_handler),

	url(r'^hospital_activity/(?P<hospital_activity_id>\d+)/$', hospital_activity_handler),
	url(r'^hospital_activity/$', hospital_activity_handler),

	url(r'^hospital_bed_capacity/(?P<hospital_bed_capacity_id>\d+)/$', hospital_bed_capacity_handler),
	url(r'^hospital_bed_capacity/$', hospital_bed_capacity_handler),

	url(r'^hospital_contact/(?P<hospital_contact_id>\d+)/$', hospital_contact_handler),
	url(r'^hospital_contact/$', hospital_contact_handler),

	url(r'^hospital_image/(?P<hospital_image_id>\d+)/$', hospital_image_handler),
	url(r'^hospital_image/$', hospital_image_handler),

	url(r'^hospital_request/(?P<hospital_request_id>\d+)/$', hospital_request_handler),
	url(r'^hospital_request/$', hospital_request_handler),

	url(r'^hospital_resource/(?P<hospital_resource_id>\d+)/$', hospital_resource_handler),
	url(r'^hospital_resource/$', hospital_resource_handler),

	url(r'^hospital_service/(?P<hospital_service_id>\d+)/$', hospital_service_handler),
	url(r'^hospital_service/$', hospital_service_handler),
	
	url(r'^hospital_status/(?P<hospital_id>\d+)/$', hospital_status_handler),
	url(r'^hospital_status/$', hospital_status_handler),
)
