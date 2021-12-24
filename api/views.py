from rest_framework import viewsets
from rest_framework.filters import SearchFilter,OrderingFilter
from .models import stblCountryCodeType,stblPhoneType,tblCountryCode,tblPhone,stblEntityType,tblEntity,stblAddressType,tblAddress,stblHeadCountType,tblHeadCount,stblEmailType,tblEmail,stblPhotoType,tblPhoto,stblSocialMediaType,tblSocialMedia,stblCompanyType,stblIndustryType,stblSuffixType,stblSocialMediaType,tblSocialMedia,stblCompanyType,stblIndustryType,stblSuffixType,tblEntitySocialMedia,stblPersonType,tblPerson,tblCompany,tblEntityPhone,rtblEntityEmail,rtblEntity,rtblEntityAddress
from .serializers import stblCountryCodeTypeSerializer,stblPhoneTypeSerializer,tblCountryCodeSerializer,tblPhoneSerializer,stblEntityTypeSerializer,tblEntitySerializer,stblAddressTypeSerializer,tblAddressSerializer,stblHeadCountTypeSerializer,tblHeadCountSerializer,stblEmailTypeSerializer,tblEmailSerializer,stblPhotoTypeSerializer,tblPhotoSerializer,stblSocialMediaTypeSerializer,tblSocialMediaSerializer,stblCompanyTypeSerializer,stblIndustryTypeSerializer,stblSuffixTypeSerializer,tblEntitySocialMediaSerializer,stblPersonTypeSerializer,tblPersonSerializer,tblCompanySerializer,tblEntityPhoneSerializer,rtblEntityEmailSerializer,rtblEntitySerializer,UserSerializer,rtblEntityAddressSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from drf_multiple_model.views import ObjectMultipleModelAPIView
# from django_filters.rest_framework import DjangoFilterBackend


class EDetailApi(APIView):
	def get(self,request,pk,*args, **kwargs):
		res_data = {}
		tbl_entity = tblEntity.objects.get(EntityID=pk)
		tbl_entity_serializer = tblEntitySerializer(tbl_entity)
		a = tbl_entity_serializer.data		
		res_data['Entity'] = a

		# print(tbl_entity.EntityTypeIDF)
		# if tbl_entity.EntityTypeIDF.EntityType == 'Person':

		tbl_Person = tblPerson.objects.filter(EntityIDF=tbl_entity).first()
		if tbl_Person:
			tbl_Person_serializer = tblPersonSerializer(tbl_Person)				
			b = tbl_Person_serializer.data
			res_data['Person'] = b

				
		tbl_company = tblCompany.objects.filter(EntityIDF=tbl_entity).first()
		if tbl_company:
			tbl_Company_Serializer = tblCompanySerializer(tbl_company)	
			c = tbl_Company_Serializer.data
			res_data['Company'] = c
		
		tbl_Photo = tblPhoto.objects.filter(EntityIDF=tbl_entity).first()
		if tbl_Photo:
			tbl_Photo_Serializer = tblPhotoSerializer(tbl_Photo)	
			h = tbl_Photo_Serializer.data
			res_data['Photo'] = h
			
		tbl_Entity_address = rtblEntityAddress.objects.filter(EntityIDF=tbl_entity)
		if tbl_Entity_address:
			eAddress = []
			for a in tbl_Entity_address:
				tbl_Address_Serializer = rtblEntityAddressSerializer(a)	
				d = tbl_Address_Serializer.data
				eAddress.append(d)
			res_data['Address'] = eAddress

		tbl_Entity_Phone =tblEntityPhone.objects.filter(EntityIDF=tbl_entity)
		if tbl_Entity_Phone:
			ePhone = []	
			for p in tbl_Entity_Phone:
				tbl_entity_phone_serializer = tblEntityPhoneSerializer(p)		
				e = tbl_entity_phone_serializer.data 
				ePhone.append(e)	
			res_data['Phone'] = ePhone

		rtbl_Entity_Email = rtblEntityEmail.objects.filter(EntityIDF=tbl_entity)
		if rtbl_Entity_Email:	
			rEmail = []
			for e in rtbl_Entity_Email:
				rtbl_Entity_Email_Serializer = rtblEntityEmailSerializer(e)
				f = rtbl_Entity_Email_Serializer.data
				rEmail.append(f)

			res_data['Email'] = rEmail	

		tbl_Entity_SocialMedia = tblEntitySocialMedia.objects.filter(EntityIDF=tbl_entity)
		if tbl_Entity_SocialMedia:	
			eSocial = []
			for s in tbl_Entity_SocialMedia:
				tbl_Entity_SocialMedia_Serializer = tblEntitySocialMediaSerializer(s)
				g = tbl_Entity_SocialMedia_Serializer.data
				eSocial.append(g)

			res_data['SocialMedia'] = eSocial	
			
		
		return Response(res_data)

	def delete(self,request,pk,*args,**kwargs):
		tblperson = tblPerson.objects.get(PersonID=pk)
		tblphone = tblPhone.objects.get(PhoneID = tblperson.PhoneIDF.PhoneID).delete()
		# print("phone deleted")
		tblemail = tblEmail.objects.get(EmailID = tblperson.EmailIDF.EmailID).delete()
		# print("email deleted")
		tbladdress = tblAddress.objects.get(AddressID = tblperson.AddressIDF.AddressID).delete()
		# print("address deleted")
		tblcompany = tblCompany.objects.get(CompanyID=tblperson.CompanyIDF.CompanyID).delete()
		# print("company deleted")
		tblperson.delete()	
		return Response()

	def patch(self, request, pk, format=None):
		tblperson = tblPerson.objects.get(PersonID=pk)
		tblperson_serializer = tblPersonSerializer(tblperson,data = request.data,partial=True)
		print(tblperson_serializer.is_valid())
		if tblperson_serializer.is_valid():
			tblperson_serializer.save()
			print(tblperson_serializer.data)
			return Response(tblperson_serializer.data)
		return Response(tblperson_serializer.errors, status=status.HTTP_400_BAD_REQUEST)		

class EntityDetailApi(APIView,):
	
	latest_person = None
	latest_Company = None
	
	# filter_backends = [SearchFilter]
	# search_fields = ['FullName', 'ShortName']
	# filter_backends = (DjangoFilterBackend,)
	# filter_fields = ('FullName', 'ShortName')
		

	# def get_queryset(self):
	# 	queryset = tblEntity.objects.filter(CreatedBY=request.user)
	# 	search = self.request.query_params.get('FullName')
	# 	print(search)	
	# 	if username is not None:
	# 	    queryset = queryset.filter(purchaser__username=username)
	# 	return queryset

	def get(self, request, format=None):
		# queryset = tblEntity.objects.filter(CreatedBY=request.user)
		# serializer_class = tblEntitySerializer
		# filter_backends = [SearchFilter]
		# search_fields = ['FullName', 'ShortName']

		res_data = []
		tbl_entity = tblEntity.objects.filter(CreatedBY=request.user)

		for Entity in tbl_entity:

			tbl_entity_serializer = tblEntitySerializer(Entity)

			tbl_Entity_Phone =tblEntityPhone.objects.get(EntityIDF=Entity.EntityID)
			tbl_entity_phone_serializer = tblEntityPhoneSerializer(tbl_Entity_Phone)		
			
			rtbl_Entity_Email = rtblEntityEmail.objects.get(EntityIDF= Entity.EntityID)
			rtbl_Entity_Email_Serializer = rtblEntityEmailSerializer(rtbl_Entity_Email)

			tbl_Photo = tblPhoto.objects.filter(EntityIDF=Entity.EntityID).first()
			tbl_Photo_Serializer = tblPhotoSerializer(tbl_Photo)	
			h = tbl_Photo_Serializer.data

			a = tbl_entity_serializer.data
			b =	tbl_entity_phone_serializer.data
			c = rtbl_Entity_Email_Serializer.data

			z = {**a,**b,**c,**h}
			# print(z)
			res_data.append(z)
		return Response(res_data)
	
	def post(self,request,format=None):
		data = request.data
		print(data)

		# tbl_Photo = tblPhoto(Photo = data['Photo']).save() 

		# # for entity
		# sbl_entity_type = stblEntityType.objects.get(EntityTypeID=data['EntityType'])
		# tbl_entity = tblEntity(FullName=data['FullName'],ShortName=data['ShortName'],EntityTypeIDF=sbl_entity_type,CreatedBY=request.user).save()
		# latest_entity = tblEntity.objects.last()

		
		# # for person
		# if data['FirstName']:
		# 	Stype = stblSuffixType.objects.get(SuffixID=data['SuffixType'])
		# 	PersonType = stblPersonType.objects.get(PersonTypeID=data['PersonType'])

		# 	tblperson = tblPerson(FirstName = data["FirstName"],MiddleName=data["MiddleName"],LastName = data["LastName"],Gender=data["Gcode"],DOB=data["DOB"],SuffixIDF=Stype,PersonTypeIDF= PersonType,EntityIDF=latest_entity)
		# 	tblperson.save()
		# 	global latest_person 
		# 	latest_person = tblPerson.objects.last()
			

		# if data['CompanyName']:
		# 	# Head Count Type
		# 	HeadCountType = stblHeadCountType.objects.get(HeadCountTypeID=data['HeadCountType'])		
		# 	HeadCount = tblHeadCount(HeadCountRange=data['HeadCountRange'],HeadCountTypeIDF=HeadCountType)
		# 	HeadCount.save()
		# 	latest_HeadCount = tblHeadCount.objects.last()
		# 	# print(latest_HeadCount)
		# 	CompanyType = stblCompanyType.objects.get(CompanyTypeID=data['CompanyType'])
		# 	IndustryType = stblIndustryType.objects.get(IndustryID=data['IndustryType'])
		# 	tblcompany = tblCompany(CompanyName=data['CompanyName'],GSTINNo=data['GSTINNo'],Headquarter=data['Headquarter'],WebsiteURL=data['WebsiteURL'],About=data['About'],Founded=data['Founded'],Specialities=data['Speciality'],AnnualRevenue=data['AnnualRevenue'],HeadcountIDF=latest_HeadCount,CompanyTypeIDF=CompanyType,IndustryIDF=IndustryType,EntityIDF=latest_entity)
		# 	tblcompany.save()
		# 	global latest_Company 
		# 	latest_Company = tblCompany.objects.last()

		# # for Address
		# Atype = stblAddressType.objects.get(AddressTypeID=data['AddressType'])
		# Address = tblAddress(Address=data['Address'],City=data['City'],District=data['District'],State=data['State'],Country=data['Country'],PinCode=data['PinCode'],AddressTypeIDF=Atype).save()
		# latest_Address = tblAddress.objects.last()
		# rtbl_entity_address = rtblEntityAddress(AddressIDF = latest_Address,EntityIDF=latest_entity) 
		# # print(latest_Address)

		# # for rtbl entity
		# rtbl_entity = rtblEntity(AddressIDF=latest_Address,EntityTypeIDF=sbl_entity_type)
		# if data['FirstName']:	
		# 	rtbl_entity.PersonIDF=latest_person
		# if data['CompanyName']:	
		# 	rtbl_entity.CompanyIDF=latest_Company
		# if data['Designation']:	
		# 	rtbl_entity.Designation=data['Designation']	
			
		# rtbl_entity.save()

					
		# # for social media
		# sbl_social_type = stblSocialMediaType.objects.get(SocialMediaTypeID=data['SocialMediaType'])
		# tbl_social = tblSocialMedia(url=data['url'],SocialMediaTypeIDF=sbl_social_type).save()
		# latest_social = tblSocialMedia.objects.last()
		# tbl_entity_social = tblEntitySocialMedia(EntityIDF=latest_entity,SocialMediaIDF=latest_social).save()

		# # for photo



		#  # for Email		
		# Etype = stblEmailType.objects.get(EmailTypeID=data["EmailType"])
		# Email = tblEmail(EmailAddress=data["EmailAddress"],EmailTypeIDF=Etype).save()	
		# latest_Email = tblEmail.objects.last()

		# rtbl_entity_email = rtblEntityEmail(EmailIDF=latest_Email,EntityIDF=latest_entity).save()

		#  # for Phone
		# Ctype = stblCountryCodeType.objects.get(CountryCodeID=data['CountryName'])
		# Ccode = tblCountryCode.objects.get(CountryCode=data['CountryCode'])
		# Ptype = stblPhoneType.objects.get(PhoneTypeID=data['PhoneType'])
		# Pnumber = tblPhone(CodeIDF=Ccode,PhoneNo=data["PhoneNo"],PhoneTypeIDF=Ptype).save()
		# latest_Pnumber = tblPhone.objects.last()
		# tbl_entity_phone = tblEntityPhone(EntityIDF=latest_entity,PhoneIDF=latest_Pnumber).save()


		return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)



# for All static table 
class StaticDataApi(ObjectMultipleModelAPIView):
	 querylist =[
		{'queryset':stblPhoneType.objects.all(),'serializer_class':stblPhoneTypeSerializer, 'label': 'Phone_Type'},
		{'queryset':tblCountryCode.objects.all(),'serializer_class':tblCountryCodeSerializer, 'label': 'Country_Code'},
		{'queryset':stblEntityType.objects.all(),'serializer_class':stblEntityTypeSerializer, 'label': 'Entity_Type'},
		
		{'queryset':stblAddressType.objects.all(),'serializer_class':stblAddressTypeSerializer, 'label': 'Address_Type'},
		{'queryset':stblHeadCountType.objects.all(),'serializer_class':stblHeadCountTypeSerializer, 'label': 'HeadCount_Type'},
		{'queryset':stblEmailType.objects.all(),'serializer_class':stblEmailTypeSerializer, 'label': 'Email_Type'},
		
		{'queryset':stblPhotoType.objects.all(),'serializer_class':stblPhotoTypeSerializer, 'label': 'Photo_Type'},
		{'queryset':stblSocialMediaType.objects.all(),'serializer_class':stblSocialMediaTypeSerializer, 'label': 'SocialMedia_Type'},
		{'queryset':stblCompanyType.objects.all(),'serializer_class':stblCompanyTypeSerializer, 'label': 'Company_Type'},
		
		{'queryset':stblIndustryType.objects.all(),'serializer_class':stblIndustryTypeSerializer, 'label': 'Industry_Type'},
		{'queryset':stblSuffixType.objects.all(),'serializer_class':stblSuffixTypeSerializer, 'label': 'Suffix_Type'},
		{'queryset':stblPersonType.objects.all(),'serializer_class':stblPersonTypeSerializer, 'label': 'Person_Type'},
	 ]
	 


class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	
	def get_queryset(self):
		# print(self.request.user)
		user = User.objects.filter(username=self.request.user) 
		return user

class stblCountryCodeTypeViewSet(viewsets.ModelViewSet):
	queryset = stblCountryCodeType.objects.all()
	serializer_class = stblCountryCodeTypeSerializer
	# permission_classes = [IsAuthenticated]
	# filter_backends = [SearchFilter]

class stblPhoneTypeViewSet(viewsets.ModelViewSet):
	queryset = stblPhoneType.objects.all()
	serializer_class = stblPhoneTypeSerializer	


class tblCountryCodeViewSet(viewsets.ModelViewSet):
	queryset = tblCountryCode.objects.all()
	serializer_class = tblCountryCodeSerializer		


class tblPhoneViewSet(viewsets.ModelViewSet):
	queryset = tblPhone.objects.all()
	serializer_class = tblPhoneSerializer	
	search_fields = ['PhoneNo']


class stblEntityTypeViewSet(viewsets.ModelViewSet):
	queryset = stblEntityType.objects.all()
	serializer_class = stblEntityTypeSerializer	

class tblEntityViewSet(viewsets.ModelViewSet):
	queryset = tblEntity.objects.all()
	serializer_class = tblEntitySerializer
	filter_backends = [SearchFilter]
	search_fields = ['FullName','ShortName']					


class stblAddressTypeViewSet(viewsets.ModelViewSet):
	queryset = stblAddressType.objects.all()
	serializer_class = stblAddressTypeSerializer	

class tblAddressViewSet(viewsets.ModelViewSet):
	queryset = tblAddress.objects.all()
	serializer_class = tblAddressSerializer					
	filter_backends = [SearchFilter]
	search_fields = ['City','District','State','PinCode','Country']
	

	
class stblHeadCountTypeViewSet(viewsets.ModelViewSet):
	queryset = stblHeadCountType.objects.all()
	serializer_class = stblHeadCountTypeSerializer	

class tblHeadCountViewSet(viewsets.ModelViewSet):
	queryset = tblHeadCount.objects.all()
	serializer_class = tblHeadCountSerializer					



class stblEmailTypeViewSet(viewsets.ModelViewSet):
	queryset = stblEmailType.objects.all()
	serializer_class = stblEmailTypeSerializer	

class tblEmailViewSet(viewsets.ModelViewSet):
	queryset = tblEmail.objects.all()
	serializer_class = tblEmailSerializer					



class stblPhotoTypeViewSet(viewsets.ModelViewSet):
	queryset = stblPhotoType.objects.all()
	serializer_class = stblPhotoTypeSerializer	

class tblPhotoViewSet(viewsets.ModelViewSet):
	queryset = tblPhoto.objects.all()
	serializer_class = tblPhotoSerializer					



class stblSocialMediaTypeViewSet(viewsets.ModelViewSet):
	queryset = stblSocialMediaType.objects.all()
	serializer_class = stblSocialMediaTypeSerializer	

class tblSocialMediaViewSet(viewsets.ModelViewSet):
	queryset = tblSocialMedia.objects.all()
	serializer_class = tblSocialMediaSerializer					


class stblCompanyTypeViewSet(viewsets.ModelViewSet):
	queryset = stblCompanyType.objects.all()
	serializer_class = stblCompanyTypeSerializer	

class stblIndustryTypeViewSet(viewsets.ModelViewSet):
	queryset = stblIndustryType.objects.all()
	serializer_class = stblIndustryTypeSerializer					

class stblSuffixTypeViewSet(viewsets.ModelViewSet):
	queryset = stblSuffixType.objects.all()
	serializer_class = stblSuffixTypeSerializer					


class tblEntitySocialMediaViewSet(viewsets.ModelViewSet):
	queryset = tblEntitySocialMedia.objects.all()
	serializer_class = tblEntitySocialMediaSerializer	

class stblPersonTypeViewSet(viewsets.ModelViewSet):
	queryset = stblPersonType.objects.all()
	serializer_class = stblPersonTypeSerializer					

class tblPersonViewSet(viewsets.ModelViewSet):
	queryset = tblPerson.objects.all()
	serializer_class = tblPersonSerializer
	filter_backends = [SearchFilter]
	search_fields = ['FirstName','MiddleName','LastName']

class tblCompanyViewSet(viewsets.ModelViewSet):
	queryset = tblCompany.objects.all()
	serializer_class = tblCompanySerializer
	filter_backends = [SearchFilter]
	search_fields = ['CompanyName']



class tblEntityPhoneViewSet(viewsets.ModelViewSet):
	queryset = tblEntityPhone.objects.all()
	serializer_class = tblEntityPhoneSerializer

class rtblEntityEmailViewSet(viewsets.ModelViewSet):
	queryset = rtblEntityEmail.objects.all()
	serializer_class = rtblEntityEmailSerializer

class rtblEntityViewSet(viewsets.ModelViewSet):
	queryset = rtblEntity.objects.all()
	serializer_class = rtblEntitySerializer			
	filter_backends = [SearchFilter]
	search_fields = ['Designation']
