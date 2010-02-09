from django.contrib.gis.db import models
from django.utils.encoding import *
from datetime import *
import hashlib, random

MESSAGE_STATUS_CHOICE = (
	('NW', 'New Message'),
	('IP', 'In Process'),
	('CM', 'Complete'),
	('IG', 'Ignored')
)

def guid_gen():
	return hashlib.sha1(str(random.random())).hexdigest()


class CharNullField(models.CharField):
	description = "CharField that stores NULL but returns ''"
	def to_python(self, value):
		if isinstance(value, models.CharField):
			return value 
		if value==None:
			return ""
		else:
			return value
	def get_db_prep_value(self, value):
		if value=="":
			return None
		else:
			return value

class OutgoingSmsMessage(models.Model):
	guid = models.CharField(max_length=512, default=guid_gen)
	recipient = models.CharField(max_length=25)
	message = models.CharField(max_length=160)
	date_queued = models.DateTimeField(default=datetime.now)
	date_sent = models.DateTimeField(null=True, blank=True)
	receipt = CharNullField(max_length=512, null=True, blank=True, default=None)	
	def __unicode__(self):
        	return str(self.recipient + ' ' + str(self.message)) 
	class Meta:
		verbose_name = "Outgoing SMS Message"

class IncomingSmsMessage(models.Model):
	guid = models.CharField(max_length=512)
	sender = models.CharField(max_length=25)
	message = models.CharField(max_length=255, null=True, blank=True)
	date_sent = models.DateTimeField(null=True, blank=True)
	notes = models.TextField(null=True, blank=True)
	status = models.CharField(max_length=2, choices=MESSAGE_STATUS_CHOICE)
	status_changed_date = models.DateTimeField(default=datetime.now)
	receipt = models.CharField(max_length=512, null=True, blank=True)	
	objects = models.GeoManager()
	def __unicode__(self):
        	return str(self.sender + ' ' + str(self.date_sent)) 
	class Meta:
		verbose_name = "Incoming SMS Message"

class VoiceMessage(models.Model):
	gvoice_id = models.CharField(max_length=256)
	start_time = models.DateTimeField(null=True, blank=True)
	phone_number = models.CharField(max_length=100, null=True, blank=True)
	subject = models.CharField(max_length=255, null=True, blank=True)
	notes = models.TextField(null=True, blank=True)
	mp3_url = models.CharField(max_length=255, blank=True, null=True)
	status = models.CharField(max_length=2, choices=MESSAGE_STATUS_CHOICE)
	status_changed_date = models.DateTimeField()
	objects = models.GeoManager()
	def __unicode__(self):
        	return str(self.phone_number + ' ' + str(self.start_time))
	class Meta:
		verbose_name = "Incoming Voice Message"

class MailMessage(models.Model):
	from_address = models.CharField(max_length=512, null=True, blank=True)
	subject = models.CharField(max_length=512,null=True,blank=True)
	date_sent = models.DateTimeField(null=True,blank=True)
	message = models.TextField(null=True,blank=True)
	return_path = models.CharField(max_length=512, null=True, blank=True)
	message_id = models.CharField(max_length=512, null=True, blank=True)
	status = models.CharField(max_length=2, choices=MESSAGE_STATUS_CHOICE)
	status_changed_date = models.DateTimeField()
	objects = models.GeoManager()
	def __unicode__(self):
        	return str(self.return_path + ' ' + str(self.date_sent))
	class Meta:
		verbose_name = "Incoming Mail Message"

class OutgoingMailMessage(models.Model):
	guid = models.CharField(max_length=512, default=guid_gen) 
	to_address = models.EmailField()
	subject = models.CharField(max_length=512,null=True,blank=True)
	date_queued = models.DateTimeField(null=True,blank=True, default=datetime.now)
	date_sent = models.DateTimeField(null=True,blank=True)
	message = models.TextField(null=True,blank=True)
	message_id = models.CharField(max_length=512, null=True, blank=True)
	objects = models.GeoManager()
	def __unicode__(self):
        	return str(self.to_address + ' ' + str(self.date_queued))
	class Meta:
		verbose_name = "Outgoing Mail Message"
	
