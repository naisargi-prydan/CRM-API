from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from datetime import date

class stblCountryCodeType(models.Model):
	CountryCodeID = models.AutoField(primary_key=True)
	CountryName = models.CharField(max_length=30)

	def __str__(self):
		return self.CountryName

	class Meta:
		verbose_name_plural = "stbl Country Code Type"	


class stblPhoneType(models.Model):
	PhoneTypeID = models.AutoField(primary_key=True)
	PhoneType = models.CharField(max_length=30)

	def __str__(self):
		return self.PhoneType

	class Meta:
		verbose_name_plural = "stbl Phone Type"	

class tblCountryCode(models.Model):
	CodeID = models.AutoField(primary_key=True)
	CountryCode = models.CharField(max_length=5)	
	CountryCodeIDF = models.OneToOneField('stblCountryCodeType',on_delete=models.SET_NULL,null=True,related_name='CCType')	

	def __str__(self):
		return str(self.CountryCode)

	

class tblPhone(models.Model):
	PhoneID = models.AutoField(primary_key=True)
	CodeIDF = models.ForeignKey('tblCountryCode',on_delete=models.SET_NULL,null=True,related_name='CC')		
	PhoneNo =models.BigIntegerField()	
	PhoneTypeIDF = models.ForeignKey('stblPhoneType',on_delete=models.SET_NULL,null=True,related_name='PT')	

	def __str__(self):
		return str(self.PhoneID	)	
	
		

class stblEntityType(models.Model):
	EntityTypeID = models.AutoField(primary_key=True)
	EntityType = models.CharField(max_length=30)

	def __str__(self):
		return self.EntityType

class tblEntity(models.Model):
	EntityID = models.AutoField(primary_key=True)
	FullName = models.CharField(max_length=256)	
	ShortName = models.CharField(max_length=16)
	EntityTypeIDF = models.ForeignKey('stblEntityType',on_delete=models.SET_NULL,null=True)	
	CreatedAT = models.DateTimeField(auto_now_add=True)
	CreatedBY = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

	def __str__(self):
		return str(self.FullName)		


class stblAddressType(models.Model):
	AddressTypeID = models.AutoField(primary_key=True)
	AddressType = models.CharField(max_length=30)

	def __str__(self):
		return self.AddressType

class tblAddress(models.Model):
	AddressID = models.AutoField(primary_key=True)
	Address = models.TextField()	
	City = models.CharField(max_length=30)
	District = models.CharField(max_length=30)
	State = models.CharField(max_length=30)
	PinCode = models.IntegerField()
	Country = models.CharField(max_length=30)
	AddressTypeIDF = models.ForeignKey('stblAddressType',on_delete=models.SET_NULL,null=True)	

	def __str__(self):
		return str(self.AddressID)		



class stblHeadCountType(models.Model):
	HeadCountTypeID = models.AutoField(primary_key=True)
	HeadCountType = models.CharField(max_length=10)

	def __str__(self):
		return self.HeadCountType

class tblHeadCount(models.Model):
	HeadCountID = models.AutoField(primary_key=True)
	HeadCountRange = models.BigIntegerField()	
	HeadCountTypeIDF = models.ForeignKey('stblHeadCountType',on_delete=models.SET_NULL,null=True)
	
	def __str__(self):
		return str(self.HeadCountID)	


class stblEmailType(models.Model):
	EmailTypeID = models.AutoField(primary_key=True)
	EmailType = models.CharField(max_length=11)

	def __str__(self):
		return self.EmailType

class tblEmail(models.Model):
	EmailID = models.AutoField(primary_key=True)
	EmailAddress = models.EmailField(max_length = 50)	
	EmailTypeIDF = models.ForeignKey('stblEmailType',on_delete=models.SET_NULL,null=True)
	
	def __str__(self):
		return str(self.EmailID)				



class stblPhotoType(models.Model):
	PhotoTypeID = models.AutoField(primary_key=True)
	PhotoType = models.CharField(max_length=30)

	def __str__(self):
		return self.PhotoType


class tblPhoto(models.Model):
	PhotoID = models.AutoField(primary_key=True)
	Photo = models.ImageField(upload_to="images",default='Static/avatar.jpg')	
	PhotoTypeIDF = models.ForeignKey('stblPhotoType',on_delete=models.SET_NULL,null=True)
	# EntityTypeIDF = models.ForeignKey('stblEntityType',on_delete=models.SET_NULL,null=True)
	EntityIDF = models.ForeignKey('tblEntity',on_delete=models.SET_NULL,null=True)
	
	def __str__(self):
		return str(self.PhotoID)



class stblSocialMediaType(models.Model):
	SocialMediaTypeID = models.AutoField(primary_key=True)
	SocialMediaType = models.CharField(max_length=30)

	def __str__(self):
		return self.SocialMediaType


class tblSocialMedia(models.Model):
	SocialmediaID = models.AutoField(primary_key=True)
	url = models.TextField()	
	SocialMediaTypeIDF = models.ForeignKey('stblSocialMediaType',on_delete=models.SET_NULL,null=True)
	
	def __str__(self):
		return str(self.SocialmediaID)										



class stblCompanyType(models.Model):
	CompanyTypeID = models.AutoField(primary_key=True)
	CompanyType = models.CharField(max_length=30)

	def __str__(self):
		return self.CompanyType


class stblIndustryType(models.Model):
	IndustryID = models.AutoField(primary_key=True)
	IndustryType = models.CharField(max_length=30)

	def __str__(self):
		return self.IndustryType		


class stblSuffixType(models.Model):
	SuffixID = models.AutoField(primary_key=True)
	SuffixType = models.CharField(max_length=10)

	def __str__(self):
		return self.SuffixType




class tblEntitySocialMedia(models.Model):
	EntitySocialMediaID = models.AutoField(primary_key=True)
	EntityIDF = models.ForeignKey('tblEntity',on_delete=models.SET_NULL,null=True)
	SocialMediaIDF = models.ForeignKey('tblSocialMedia',on_delete=models.SET_NULL,null=True)
	
	def __str__(self):
		return str(self.EntitySocialMediaID)														


class stblPersonType(models.Model):
	PersonTypeID = models.AutoField(primary_key=True)
	PersonType = models.CharField(max_length=30)

	def __str__(self):
		return self.PersonType		

class tblCompany(models.Model):
	CompanyID = models.AutoField(primary_key=True)
	CompanyName = models.CharField(max_length=50)
	GSTINNo = models.CharField(max_length=15)
	Headquarter = models.CharField(max_length=30)
	WebsiteURL = models.TextField()
	About = models.TextField()
	Founded = models.DateField()
	Specialities = models.TextField()
	AnnualRevenue = models.IntegerField()
	EntityIDF = models.ForeignKey('tblEntity',on_delete=models.SET_NULL,null=True)
	HeadcountIDF = models.ForeignKey('tblHeadCount',on_delete=models.SET_NULL,null=True)
	CompanyTypeIDF = models.ForeignKey('stblCompanyType',on_delete=models.SET_NULL,null=True)
	IndustryIDF = models.ForeignKey('stblIndustryType',on_delete=models.SET_NULL,null=True)

	def __str__(self):
		return str(self.CompanyName)

class tblPerson(models.Model):
	PersonID = models.AutoField(primary_key=True)
	FirstName = models.CharField(max_length=30)
	MiddleName = models.CharField(max_length=30)
	LastName = models.CharField(max_length=30)
	Gender = models.CharField(max_length=2)
	DOB = models.DateField()
	SuffixIDF = models.ForeignKey('stblSuffixType',on_delete=models.SET_NULL,null=True,related_name='SuffixBy')
	EntityIDF = models.ForeignKey('tblEntity',on_delete=models.CASCADE,null=True)
	PersonTypeIDF = models.ForeignKey('stblPersonType',on_delete=models.SET_NULL,null=True)
	# PhoneIDF = models.ForeignKey('tblPhone',on_delete=models.SET_NULL,null=True)
	# EmailIDF = models.ForeignKey('tblEmail',on_delete=models.SET_NULL,null=True)
	# AddressIDF = models.ForeignKey('tblAddress',on_delete=models.SET_NULL,null=True)
	# CompanyIDF = models.ForeignKey('tblCompany',on_delete=models.SET_NULL,null=True)
	# CreatedAT = models.DateTimeField(auto_now_add=True)
	# CreatedBY = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

	def __str__(self):
		return self.MiddleName																



		
class tblEntityPhone(models.Model):
	EntityPhoneID = models.AutoField(primary_key=True)
	EntityIDF = models.ForeignKey('tblEntity',on_delete=models.SET_NULL,null=True)
	PhoneIDF = models.ForeignKey('tblPhone',on_delete=models.SET_NULL,null=True)
	
	def __str__(self):
		return str(self.EntityPhoneID)																

class rtblEntityEmail(models.Model):
	EntityEmailID = models.AutoField(primary_key=True)
	EmailIDF = models.ForeignKey('tblEmail',on_delete=models.SET_NULL,null=True)
	EntityIDF = models.ForeignKey('tblEntity',on_delete=models.SET_NULL,null=True)
	
	def __str__(self):
		return str(self.EntityEmailID)	

class rtblEntityAddress(models.Model):
	EntityAddessID = models.AutoField(primary_key=True)
	AddressIDF = models.ForeignKey('tblAddress',on_delete=models.SET_NULL,null=True)
	EntityIDF = models.ForeignKey('tblEntity',on_delete=models.SET_NULL,null=True)
	
	def __str__(self):
		return str(self.EntityEmailID)						


class rtblEntity(models.Model):
	EntityTypeIDF = models.ForeignKey('stblEntityType',on_delete=models.SET_NULL,null=True)
	PersonIDF = models.ForeignKey('tblPerson',on_delete=models.CASCADE,null=True)
	CompanyIDF = models.ForeignKey('tblCompany',on_delete=models.CASCADE,null=True)
	AddressIDF = models.ForeignKey('tblAddress',on_delete=models.CASCADE,null=True)
	Designation = models.CharField(max_length=30,null=True)
	
	def __str__(self):
		return self.Designation				