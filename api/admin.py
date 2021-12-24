from django.contrib import admin
from .models import stblCountryCodeType,stblPhoneType,tblCountryCode,tblPhone,stblEntityType,tblEntity,stblAddressType,tblAddress,stblHeadCountType,tblHeadCount,stblEmailType,tblEmail,stblPhotoType,tblPhoto,stblSocialMediaType,tblSocialMedia,stblCompanyType,stblIndustryType,stblSuffixType,stblSocialMediaType,tblSocialMedia,stblCompanyType,stblIndustryType,stblSuffixType,tblEntitySocialMedia,stblPersonType,tblPerson,tblCompany,tblEntityPhone,rtblEntityEmail,rtblEntity

# Register your models here.

@admin.register(stblCountryCodeType)
class stblCountryCodeTypeAdmin(admin.ModelAdmin):
	list_display = ['CountryCodeID','CountryName']


@admin.register(stblPhoneType)
class stblPhoneTypeAdmin(admin.ModelAdmin):
	list_display = ['PhoneTypeID','PhoneType']


@admin.register(tblCountryCode)
class tblCountryCodeAdmin(admin.ModelAdmin):
	list_display = ['CodeID','CountryCode','CountryCodeIDF']	


@admin.register(tblPhone)
class tblPhoneAdmin(admin.ModelAdmin):
	list_display = ['PhoneID','CodeIDF','PhoneNo','PhoneTypeIDF']


@admin.register(stblEntityType)
class stblEntityTypeAdmin(admin.ModelAdmin):
	list_display = ['EntityTypeID','EntityType']		


@admin.register(tblEntity)
class tblEntityAdmin(admin.ModelAdmin):
	list_display = ['EntityID','FullName','ShortName','EntityTypeIDF','CreatedAT','CreatedBY']


@admin.register(stblAddressType)
class stblAddressTypeAdmin(admin.ModelAdmin):
	list_display = ['AddressTypeID','AddressType']		


@admin.register(tblAddress)
class tblAddressAdmin(admin.ModelAdmin):
	list_display = ['AddressID','Address','City','District','State','PinCode','Country','AddressTypeIDF']


@admin.register(stblHeadCountType)
class stblHeadCountTypeAdmin(admin.ModelAdmin):
	list_display = ['HeadCountTypeID','HeadCountType']		


@admin.register(tblHeadCount)
class tblHeadCountAdmin(admin.ModelAdmin):
	list_display = ['HeadCountID','HeadCountRange','HeadCountTypeIDF']	


@admin.register(stblEmailType)
class stblEmailTypeAdmin(admin.ModelAdmin):
	list_display = ['EmailTypeID','EmailType']		


@admin.register(tblEmail)
class tblEmailAdmin(admin.ModelAdmin):
	list_display = ['EmailID','EmailAddress','EmailTypeIDF']	


@admin.register(stblPhotoType)
class stblPhotoTypeAdmin(admin.ModelAdmin):
	list_display = ['PhotoTypeID','PhotoType']		


@admin.register(tblPhoto)
class tblPhotoAdmin(admin.ModelAdmin):
	list_display = ['PhotoID','Photo','PhotoTypeIDF','EntityIDF']	


@admin.register(stblSocialMediaType)
class stblSocialMediaTypeAdmin(admin.ModelAdmin):
	list_display = ['SocialMediaTypeID','SocialMediaType']		


@admin.register(tblSocialMedia)
class tblSocialMediaAdmin(admin.ModelAdmin):
	list_display = ['SocialmediaID','url','SocialMediaTypeIDF']	


@admin.register(stblCompanyType)
class stblCompanyTypeAdmin(admin.ModelAdmin):
	list_display = ['CompanyTypeID','CompanyType']		


@admin.register(stblIndustryType)
class tblSocialMediaAdmin(admin.ModelAdmin):
	list_display = ['IndustryID','IndustryType']


@admin.register(stblSuffixType)
class stblSuffixTypeAdmin(admin.ModelAdmin):
	list_display = ['SuffixID','SuffixType']


@admin.register(tblEntitySocialMedia)
class tblEntitySocialMediaAdmin(admin.ModelAdmin):
	list_display = ['EntitySocialMediaID','EntityIDF','SocialMediaIDF']



@admin.register(stblPersonType)
class stblPersonTypeAdmin(admin.ModelAdmin):
	list_display = ['PersonTypeID','PersonType']


@admin.register(tblPerson)
class tblPersonAdmin(admin.ModelAdmin):
	list_display = ['PersonID','FirstName','MiddleName','LastName','Gender','DOB','SuffixIDF','EntityIDF','PersonTypeIDF']


@admin.register(tblCompany)
class tblCompanyAdmin(admin.ModelAdmin):
	list_display = ['CompanyID','CompanyName','GSTINNo','Headquarter','WebsiteURL','About','Founded','Specialities','AnnualRevenue','EntityIDF','HeadcountIDF','CompanyTypeIDF','IndustryIDF']


@admin.register(tblEntityPhone)
class tblEntityPhoneAdmin(admin.ModelAdmin):
	list_display = ['EntityPhoneID','EntityIDF','PhoneIDF']


@admin.register(rtblEntityEmail)
class rtblEntityEmailAdmin(admin.ModelAdmin):
	list_display = ['EntityEmailID','EmailIDF','EntityIDF']


@admin.register(rtblEntity)
class rtblEntityAdmin(admin.ModelAdmin):
	list_display = ['EntityTypeIDF','PersonIDF','CompanyIDF','AddressIDF','Designation']