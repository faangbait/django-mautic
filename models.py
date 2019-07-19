from django.db import models

class leads(models.Model):
	owner_id=models.IntegerField(default=1)
	stage_id=models.IntegerField(blank=True,null=True)
	is_published=models.IntegerField(default=1)
	date_added=models.DateTimeField(auto_now_add=True)
	created_by=models.IntegerField(default=1)
	created_by_user=models.CharField(max_length=255,blank=True,null=True)
	points=models.IntegerField(default=0)
	last_active=models.DateTimeField(blank=True,null=True)
	internal=models.TextField(blank=True,null=True)
	social_cache=models.TextField(blank=True,null=True)
	date_identified=models.DateTimeField(blank=True,null=True)
	preferred_profile_image=models.CharField(max_length=255,blank=True,null=True)
	title=models.CharField(max_length=255,blank=True,null=True)
	firstname=models.CharField(max_length=255,blank=True,null=True)
	lastname=models.CharField(max_length=255,blank=True,null=True)
	company=models.CharField(max_length=255,blank=True,null=True)
	position=models.CharField(max_length=255,blank=True,null=True)
	email=models.CharField(max_length=255,blank=True,null=True)
	phone=models.CharField(max_length=255,blank=True,null=True)
	mobile=models.CharField(max_length=255,blank=True,null=True)
	address1=models.CharField(max_length=255,blank=True,null=True)
	address2=models.CharField(max_length=255,blank=True,null=True)
	city=models.CharField(max_length=255,blank=True,null=True)
	state=models.CharField(max_length=255,blank=True,null=True)
	zipcode=models.CharField(max_length=255,blank=True,null=True)
	timezone=models.CharField(max_length=255,blank=True,null=True)
	country=models.CharField(max_length=255,blank=True,null=True)
	fax=models.CharField(max_length=255,blank=True,null=True)
	preferred_locale=models.CharField(max_length=255,blank=True,null=True)
	attribution_date=models.DateTimeField(blank=True,null=True)
	attribution=models.FloatField(blank=True,null=True)
	website=models.TextField(blank=True,null=True)
	facebook=models.CharField(max_length=255,blank=True,null=True)
	foursquare=models.CharField(max_length=255,blank=True,null=True)
	googleplus=models.CharField(max_length=255,blank=True,null=True)
	instagram=models.CharField(max_length=255,blank=True,null=True)
	linkedin=models.CharField(max_length=255,blank=True,null=True)
	skype=models.CharField(max_length=255,blank=True,null=True)
	twitter=models.CharField(max_length=255,blank=True,null=True)

	def __str__(self):
		if self.email:
			return self.email
		elif self.lastname:
			if self.firstname:
				return self.lastname + ',' + self.firstname + '.'
			else:
				return self.lastname
		else:
			return 'Anonymous User ' + str(self.id)
