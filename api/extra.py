class PersonDetailApi(APIView):
	def get(self, request, format=None):
		tblperson = tblPerson.objects.filter(CreatedBY=request.user)
		tblperson_serializer = tblPersonSerializer(tblperson, many=True)
		return Response(tblperson_serializer.data)
	
	def post(self,request,format=None):
		data = request.data
		# print(data)	
		# Head Count Type
		HeadCountType = stblHeadCountType.objects.get(HeadCountTypeID=data['CompanyIDF']['HeadcountIDF']['HeadCountTypeIDF']['HeadCountTypeID'])		
		HeadCount = tblHeadCount(HeadCountRange=int(data['CompanyIDF']['HeadcountIDF']['HeadCountRange']),HeadCountTypeIDF=HeadCountType)
		# HeadCount.save()
		latest_HeadCount = tblHeadCount.objects.last()


		CompanyType = stblCompanyType.objects.get(CompanyTypeID=data['CompanyIDF']['CompanyTypeIDF']['CompanyTypeID'])
		IndustryType = stblIndustryType.objects.get(IndustryID=data['CompanyIDF']['IndustryIDF']['IndustryID'])


		tblcompany = tblCompany(CompanyName=data['CompanyIDF']['CompanyName'],GSTINNo=data['CompanyIDF']['GSTINNo'],Headquarter=data['CompanyIDF']['Headquarter'],WebsiteURL=data['CompanyIDF']['WebsiteURL'],About=data['CompanyIDF']['About'],Founded=data['CompanyIDF']['Founded'],Specialities=data['CompanyIDF']['Speciality'],AnnualRevenue=int(data['CompanyIDF']['AnnualRevenue']),HeadcountIDF=latest_HeadCount,CompanyTypeIDF=CompanyType,IndustryIDF=IndustryType)
		# print(tblcompany)
		tblcompany.save()
		latest_Company = tblCompany.objects.last()

		 # for Email		
		Etype = stblEmailType.objects.get(EmailTypeID=data['EmailIDF']["EmailTypeIDF"]["EmailTypeID"])
		Email = tblEmail(EmailAddress=data['EmailIDF']["EmailAddress"],EmailTypeIDF=Etype).save()	
		latest_Email = tblEmail.objects.last()	

		 # for Phone
		Ctype = stblCountryCodeType.objects.get(CountryCodeID=data['PhoneIDF']["CodeIDF"]['CountryCodeIDF']['CountryCodeID'])

		Ccode = tblCountryCode.objects.get(CodeID=data['PhoneIDF']["CodeIDF"]["CodeID"])

		Ptype = stblPhoneType.objects.get(PhoneTypeID=data["PhoneIDF"]['PhoneTypeIDF']['PhoneTypeID'])


		Pnumber = tblPhone(CodeIDF=Ccode,PhoneNo=data["PhoneIDF"]["PhoneNo"],PhoneTypeIDF=Ptype).save()
		latest_Pnumber = tblPhone.objects.last()

		# for Address
		Atype = stblAddressType.objects.get(AddressTypeID=data['AddressIDF']['AddressTypeIDF']['AddressTypeID'])
		Address = tblAddress(Address=data['AddressIDF']['Address'],City=data['AddressIDF']['City'],District=data['AddressIDF']['District'],State=data['AddressIDF']['State'],Country=data['AddressIDF']['Country'],PinCode=data['AddressIDF']['PinCode'],AddressTypeIDF=Atype).save()
		latest_Address = tblAddress.objects.last()

		
		Stype = stblSuffixType.objects.filter(SuffixID=data['SuffixIDF']["SuffixID"]).first()
		PersonType = stblPersonType.objects.filter(PersonTypeID=data['PersonTypeIDF']["PersonTypeID"]).first()
		
		# for entity tbl
		# stblentitytype = stblEntityType.objects.get()
		# tblentity = tblEntity(FullName=,ShortName=,EntityTypeIDF=)

		#for Person tbl		
		tblperson = tblPerson(FirstName = data["FirstName"],MiddleName=data["MiddleName"],LastName = data["LastName"],Gender=data["Gcode"],DOB=data["DOB"],SuffixIDF=Stype,PersonTypeIDF= PersonType,EmailIDF=latest_Email,PhoneIDF=latest_Pnumber,AddressIDF=latest_Address,CreatedBY=request.user,CompanyIDF=latest_Company)
		tblperson.save()
		return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
