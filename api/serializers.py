from rest_framework import serializers
from .models import stblCountryCodeType,stblPhoneType,tblCountryCode,tblPhone,stblEntityType,tblEntity,stblAddressType,tblAddress,stblHeadCountType,tblHeadCount,stblEmailType,tblEmail,stblPhotoType,tblPhoto,stblSocialMediaType,tblSocialMedia,stblCompanyType,stblIndustryType,stblSuffixType,tblEntitySocialMedia,stblPersonType,tblPerson,tblCompany,tblEntityPhone,rtblEntityEmail,rtblEntity,rtblEntityAddress
from django.conf import settings
from drf_writable_nested.serializers import WritableNestedModelSerializer

from django.contrib.auth.models import User

from rest_framework import serializers
from django.core.files.base import ContentFile
import base64


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid
        print("ininternal")
        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            print("ininstance")
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name','last_name','username', 'email']

class stblPhoneTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = stblPhoneType
		fields = ['PhoneTypeID','PhoneType']

class stblCountryCodeTypeSerializer(serializers.ModelSerializer):
	# CCType = tblCountryCodeSerializer(many=True,read_only=True)
	class Meta:
		model = stblCountryCodeType
		fields = ['CountryCodeID','CountryName']

class tblCountryCodeSerializer(WritableNestedModelSerializer):
	CountryCodeIDF = stblCountryCodeTypeSerializer()
	class Meta:
		model = tblCountryCode
		fields = ['CodeID','CountryCode','CountryCodeIDF']		


class tblPhoneSerializer(WritableNestedModelSerializer):
	PhoneTypeIDF = stblPhoneTypeSerializer()
	CodeIDF = tblCountryCodeSerializer()

	class Meta:
		model = tblPhone
		fields = ['PhoneID','CodeIDF','PhoneNo','PhoneTypeIDF']		


class stblEntityTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = stblEntityType
		fields = '__all__'		

class tblEntitySerializer(WritableNestedModelSerializer):
	EntityTypeIDF = stblEntityTypeSerializer()
	class Meta:
		model = tblEntity
		fields = ['EntityID','FullName','ShortName','EntityTypeIDF','CreatedAT','CreatedBY',]		


class stblAddressTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = stblAddressType
		fields = '__all__'		

class tblAddressSerializer(WritableNestedModelSerializer):
	AddressTypeIDF = stblAddressTypeSerializer()
	class Meta:
		model = tblAddress
		fields = '__all__'		


class stblHeadCountTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = stblHeadCountType
		fields = '__all__'		

class tblHeadCountSerializer(WritableNestedModelSerializer):
	HeadCountTypeIDF = stblHeadCountTypeSerializer() 
	class Meta:
		model = tblHeadCount
		fields = '__all__'		


class stblEmailTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = stblEmailType
		fields = '__all__'		

class tblEmailSerializer(WritableNestedModelSerializer):
	EmailTypeIDF = stblEmailTypeSerializer( ) 
	class Meta:
		model = tblEmail
		fields = '__all__'		


class stblPhotoTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = stblPhotoType
		fields = '__all__'		

class tblPhotoSerializer(serializers.ModelSerializer):
	Photo = Base64ImageField(max_length=None, use_url=True, allow_null= True)
	class Meta:
		model = tblPhoto
		fields = '__all__'	


class stblSocialMediaTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = stblSocialMediaType
		fields = '__all__'		

class tblSocialMediaSerializer(serializers.ModelSerializer):
	SocialMediaTypeIDF = stblSocialMediaTypeSerializer()
	class Meta:
		model = tblSocialMedia
		fields = '__all__'	


class stblCompanyTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = stblCompanyType
		fields = '__all__'		


class stblIndustryTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = stblIndustryType
		fields = '__all__'		



class tblEntitySocialMediaSerializer(serializers.ModelSerializer):
	SocialMediaIDF = tblSocialMediaSerializer()
	class Meta:
		model = tblEntitySocialMedia
		fields = '__all__'		


class stblPersonTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = stblPersonType
		fields = '__all__'		


class stblSuffixTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = stblSuffixType
		fields = ['SuffixID','SuffixType']	



class tblCompanySerializer(WritableNestedModelSerializer):
	HeadcountIDF = tblHeadCountSerializer()
	CompanyTypeIDF = stblCompanyTypeSerializer()
	IndustryIDF = stblIndustryTypeSerializer()
	EntityIDF = tblEntitySerializer()
	class Meta:
		model = tblCompany
		fields = '__all__'	


class tblEntityPhoneSerializer(serializers.ModelSerializer):
	PhoneIDF = tblPhoneSerializer()
	class Meta:
		model = tblEntityPhone
		fields = '__all__'	

class rtblEntityEmailSerializer(serializers.ModelSerializer):
	EmailIDF = tblEmailSerializer()
	class Meta:
		model = rtblEntityEmail
		fields = '__all__'	

class rtblEntityAddressSerializer(serializers.ModelSerializer):
	AddressIDF = tblAddressSerializer()
	class Meta:
		model = rtblEntityAddress
		fields = '__all__'	

class tblPersonSerializer(WritableNestedModelSerializer):
	SuffixIDF = stblSuffixTypeSerializer(read_only=False) 
	EntityIDF = tblEntitySerializer(read_only=False)
	PersonTypeIDF = stblPersonTypeSerializer(read_only=False)
	# PhoneIDF = tblPhoneSerializer(read_only=False)
	# EmailIDF = tblEmailSerializer(read_only=False)

	class Meta:
		model = tblPerson
		fields = '__all__'	

class rtblEntitySerializer(serializers.ModelSerializer):	
	EntityTypeIDF = stblEntityTypeSerializer()
	PersonIDF = tblPersonSerializer()
	CompanyIDF = tblCompanySerializer()
	AddressIDF = tblAddressSerializer()
	class Meta:
		model = rtblEntity
		fields = '__all__'	