import sys
from piston.handler import BaseHandler, AnonymousBaseHandler
from piston.emitters import Emitter, JSONEmitter
from piston_api.emitters import GeoJSONEmitter, CSVEmitter, KMLEmitter
from mednet.sahana.models import *
from mednet.messaging.models import *
from piston.utils import rc
from datetime import *
import hashlib, random
import urllib

JSONEmitter.unregister('json')
Emitter.register('json', GeoJSONEmitter, 'application/javascript; charset=utf-8')
Emitter.register('csv', CSVEmitter, 'text/csv; charset=utf-8')
Emitter.register('kml', KMLEmitter, 'application/vnd.google-earth.kml+xml; charset=utf-8')

outgoing_fields = ('date_queued', 'receipt', 'date_sent', 'message', 'recipient', 'guid')

#Incoming SMS
class AnonymousIncomingSmsHandler(BaseHandler):
	allowed_methods=('GET','POST',)
	model = IncomingSmsMessage

	def read(self, request, message_id=None):
		if(message_id):
			return IncomingSmsMessage.objects.get(guid=message_id)
		else:
			return IncomingSmsMessage.objects.all()

	def create(self, request):
		if not self.has_model():
			return rc.NOT_IMPLEMENTED
		
		attrs = self.flatten_dict(request.POST)
		print attrs
		if attrs.has_key('data'):
			ext_posted_data = simplejson.loads(request.POST.get('data'))
			attrs = self.flatten_dict(ext_posted_data)
		try:
			inst = self.model.objects.get(**attrs)
			return rc.DUPLICATE_ENTRY
		except self.model.DoesNotExist:
			try:
				attrs['message'] = urllib.unquote(attrs['message']).decode('utf8')
			except:
				attrs['message'] = urllib.unquote(attrs['message'])
			inst = self.model(**attrs)
			inst.receipt = hashlib.sha1(str(random.random())).hexdigest()
			inst.status_changed_date = datetime.now()
			inst.status = 'NW'
			inst.save()
			return inst
		except self.model.MultipleObjectsReturned:
			return rc.DUPLICATE_ENTRY

class IncomingSmsHandler(BaseHandler):
	allow_methods = ('GET',)
	model = IncomingSmsMessage
	anonymous = AnonymousIncomingSmsHandler

#Outgoing SMS
class AnonymousOutgoingSmsHandler(BaseHandler):
	allowed_methods = ('GET','PUT')
	model = OutgoingSmsMessage
	fields = outgoing_fields

	def read(self, request, message_date=None):
		if(message_date):
			try:	
				objects = OutgoingSmsMessage.objects.filter(receipt=None)
				print objects
				return objects
			except:
				rc.BAD_REQUEST
		else:
			return OutgoingSmsMessage.objects.all()
	
	def update(self, request, *args, **kwargs):		
		attrs = self.flatten_dict(request.POST)
		print attrs
		try:
			guid=attrs['guid']
			instance = OutgoingSmsMessage.objects.get(guid=guid)
			print instance
		except self.model.DoesNotExist:
			print "model.DoesNotExist"
			return rc.NOT_FOUND
		except self.model.MultipleObjectsReturned:
			print "bad request1"
			return rc.BAD_REQUEST
		except:
			print "bad request2"
			print sys.exc_info()
			return rc.BAD_REQUEST
		attrs = self.flatten_dict(request.data)
		for k,v in attrs.iteritems():
			setattr(instance, k, v)
		instance.save()
		return instance

class OutgoingSmsHandler(BaseHandler):
	allow_methods = ('GET',)
	model = OutgoingSmsMessage
	fields = outgoing_fields
	anonymous = AnonymousOutgoingSmsHandler

#Hospitals
class AnonymousHospitalHandler(BaseHandler):
   allowed_methods = ('GET',)
   model = HmsHospital

   def read(self, request, hospital_id=None):
	if(hospital_id):
		return HmsHospital.objects.get(pk=hospital_id)
	else:
		return HmsHospital.objects.all()

class HospitalHandler(BaseHandler):
	allow_methods = ('GET',)
	model = HmsHospital
	anonymous = AnonymousHospitalHandler

#Hospital Activities
class AnonymousHospitalActivityHandler(BaseHandler):
   allowed_methods = ('GET',)
   model = HmsActivity

   def read(self, request, hospital_activity_id=None):
	if(hospital_activity_id):
		return HmsActivity.objects.get(pk=hospital_activity_id)
	else:
		return HmsActivity.objects.all()

class HospitalActivityHandler(BaseHandler):
	allow_methods = ('GET',)
	model = HmsActivity
	anonymous = AnonymousHospitalActivityHandler

#Hospital Bed Capacity
class AnonymousHospitalBedCapacityHandler(BaseHandler):
   allowed_methods = ('GET',)
   model = HmsBedCapacity

   def read(self, request, hospital_bed_capacity_id=None):
	if(hospital_bed_capacity_id):
		return HmsBedCapacity.objects.get(pk=hospital_bed_capacity_id)
	else:
		return HmsBedCapacity.objects.all()

class HospitalBedCapacityHandler(BaseHandler):
	allow_methods = ('GET',)
	model = HmsBedCapacity
	anonymous = AnonymousHospitalBedCapacityHandler

#Hospital Contacts
class AnonymousHospitalContactHandler(BaseHandler):
   allowed_methods = ('GET',)
   model = HmsContact

   def read(self, request, hospital_contact_id=None):
	if(hospital_contact_id):
		return HmsContact.objects.get(pk=hospital_contact_id)
	else:
		return HmsContact.objects.all()

class HospitalContactHandler(BaseHandler):
	allow_methods = ('GET',)
	model = HmsContact
	anonymous = AnonymousHospitalContactHandler

#Hospital Images 
class AnonymousHospitalImageHandler(BaseHandler):
   allowed_methods = ('GET',)
   model = HmsImage

   def read(self, request, hospital_image_id=None):
	if(hospital_image_id):
		return HmsImage.objects.get(pk=hospital_image_id)
	else:
		return HmsImage.objects.all()

class HospitalImageHandler(BaseHandler):
	allow_methods = ('GET',)
	model = HmsImage
	anonymous = AnonymousHospitalImageHandler

#Hospital Request 
class AnonymousHospitalRequestHandler(BaseHandler):
   allowed_methods = ('GET',)
   model = HmsRequest

   def read(self, request, hospital_request_id=None):
	if(hospital_request_id):
		return HmsRequest.objects.get(pk=hospital_request_id)
	else:
		return HmsRequest.objects.all()

class HospitalRequestHandler(BaseHandler):
	allow_methods = ('GET',)
	model = HmsRequest
	anonymous = AnonymousHospitalRequestHandler

#Hospital Resource 
class AnonymousHospitalResourceHandler(BaseHandler):
   allowed_methods = ('GET',)
   model = HmsResource

   def read(self, request, hospital_resource_id=None):
	if(hospital_resource_id):
		return HmsResource.objects.get(pk=hospital_resource_id)
	else:
		return HmsResource.objects.all()

class HospitalResourceHandler(BaseHandler):
	allow_methods = ('GET',)
	model = HmsResource
	anonymous = AnonymousHospitalResourceHandler

#Hospital Service 
class AnonymousHospitalServiceHandler(BaseHandler):
   allowed_methods = ('GET',)
   model = HmsService

   def read(self, request, hospital_service_id=None):
	if(hospital_service_id):
		return HmsService.objects.get(pk=hospital_service_id)
	else:
		return HmsService.objects.all()

class HospitalServiceHandler(BaseHandler):
	allow_methods = ('GET',)
	model = HmsService
	anonymous = AnonymousHospitalServiceHandler

#Hospital Status 
class AnonymousHospitalStatusHandler(BaseHandler):
   allowed_methods = ('GET',)
   model = HmsStatus

   def read(self, request, hospital_id=None):
	if(hospital_id):
		return HmsStatus.objects.filter(hospital=HmsHospital.objects.get(pk=hospital_id))
	else:
		return HmsStatus.objects.all()

class HospitalStatusHandler(BaseHandler):
	allow_methods = ('GET',)
	model = HmsStatus
	anonymous = AnonymousHospitalStatusHandler
