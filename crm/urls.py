from django.contrib import admin
from django.conf.urls import url
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


schema_view = get_schema_view(
   openapi.Info(
      title="DOCS FOR CRM APIs",
      default_version='v1',
      # description="Test description",
      # terms_of_service="https://www.google.com/policies/terms/",
      # contact=openapi.Contact(email="contact@snippets.local"),
      # license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
# router.register('PersonDetailApi',views.PersonDetailApi,basename='PersonDetailApi'),
router.register('userViewSet',views.UserViewSet,basename='userViewSet'),
router.register('stblCountryCodeType',views.stblCountryCodeTypeViewSet,basename='stblCountryCodeType'),
router.register('stblPhoneType',views.stblPhoneTypeViewSet,basename='stblPhoneType'),
router.register('tblCountryCode',views.tblCountryCodeViewSet,basename='tblCountryCode'),
router.register('tblPhone',views.tblPhoneViewSet,basename='tblPhone'),
router.register('stblEntityType',views.stblEntityTypeViewSet,basename='stblEntityType'),
router.register('tblEntity',views.tblEntityViewSet,basename='tblEntity'),
router.register('stblAddressType',views.stblAddressTypeViewSet,basename='stblAddressType'),
router.register('tblAddress',views.tblAddressViewSet,basename='tblAddress'),
router.register('stblHeadCountType',views.stblHeadCountTypeViewSet,basename='stblHeadCountType'),
router.register('tblHeadCount',views.tblHeadCountViewSet,basename='tblHeadCount'),
router.register('stblEmailType',views.stblEmailTypeViewSet,basename='stblEmailType'),
router.register('tblEmail',views.tblEmailViewSet,basename='tblEmail'),
router.register('stblPhotoType',views.stblPhotoTypeViewSet,basename='stblPhotoType'),
router.register('tblPhoto',views.tblPhotoViewSet,basename='tblPhoto'),
router.register('stblSocialMediaType',views.stblSocialMediaTypeViewSet,basename='stblSocialMediaType'),
router.register('tblSocialMedia',views.tblSocialMediaViewSet,basename='tblSocialMedia'),
router.register('stblCompanyType',views.stblCompanyTypeViewSet,basename='stblCompanyType'),
router.register('stblIndustryType',views.stblIndustryTypeViewSet,basename='stblIndustryType'),
router.register('stblSuffixType',views.stblSuffixTypeViewSet,basename='stblSuffixType'),
router.register('tblEntitySocialMedia',views.tblEntitySocialMediaViewSet,basename='tblEntitySocialMedia'),
router.register('stblPersonType',views.stblPersonTypeViewSet,basename='stblPersonType'),
router.register('tblPerson',views.tblPersonViewSet,basename='tblPerson'),
router.register('tblCompany',views.tblCompanyViewSet,basename='tblCompany'),
router.register('tblEntityPhone',views.tblEntityPhoneViewSet,basename='tblEntityPhone'),
router.register('rtblEntityEmail',views.rtblEntityEmailViewSet,basename='rtblEntityEmail'),
router.register('rtblEntity',views.rtblEntityViewSet,basename='rtblEntity'),


urlpatterns = [
    path('crm-admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('api/EntityDetailApi',views.EntityDetailApi.as_view(),name="EntityDetailApi"),
    path('api/EntityDetailApi/<int:pk>',views.EDetailApi.as_view(),name="EDetailApi"),
    path('api/StaticDataApi',views.StaticDataApi.as_view(),name="StaticDataApi"),
    # path('api/PersonApi',views.PersonApi.as_view(),name="PersonApi"),

   	url(r'^docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
