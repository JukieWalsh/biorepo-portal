from django.conf.urls import url, include
from rest_framework import routers
from api import views
router = routers.DefaultRouter()

# Basic root level object views
router.register(r'users', views.UserViewSet)
router.register(r'organizations', views.OrganizationViewSet)
router.register(r'protocols', views.ProtocolViewSet)
router.register(r'datasources', views.DataSourceViewSet)
router.register(r'protocoldatasources', views.PDSViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include the login URLs for the browsable API
urlpatterns = [
    # Retrieve all subjects on a Protocol (with their external records)
    url(r'^protocols/(?P<pk>[0-9]+)/subjects/$',
        views.ProtocolSubjectsView.as_view(), name='protocol-subject-list'),
    # Create a subject on a Protocol
    url(r'^protocols/(?P<pk>[0-9]+)/subjects/create$',
        views.ProtocolSubjectDetailView.as_view(), name='protocol-subject-create'),
    # Retrieve or Update Subject
    url(r'^protocols/(?P<pk>[0-9]+)/subjects/(?P<subject>[0-9]+)$',
        views.ProtocolSubjectDetailView.as_view(), name='protocol-subject-view'),
    url(r'^protocols/(?P<pk>[0-9]+)/data_sources/$',
        views.ProtocolDataSourceView.as_view(),
        name='protocol-datasources-list'),
    url(r'^protocols/(?P<pk>[0-9]+)/organizations/$',
        views.ProtocolOrganizationView.as_view(),
        name='protocol-organization-list'),
    url(
        r'^protocoldatasources/(?P<pk>[0-9]+)/subjects/(?P<subject>[0-9]+)/records/$',
        views.PDSSubjectRecordsView.as_view(),
        name='pds-subject-record-list'),
    url(
        r'^protocoldatasources/(?P<pk>[0-9]+)/subjects/(?P<subject>[0-9]+)/record/(?P<record>[0-9]+)/$',
        views.PDSSubjectRecordDetailView.as_view(),
        name='pds-subject-record'),
    url(
        r'^protocoldatasources/(?P<pk>[0-9]+)/subjects/(?P<subject>[0-9]+)/record/(?P<record>[0-9]+)/links/$',
        views.PDSRecordLinkDetailView.as_view(),
        name='pds-subject-record-links'),
    url(
        r'^protocoldatasources/(?P<pk>[0-9]+)/subjects/$',
        views.PDSSubjectView.as_view(),
        name='pds-subject-list'),
    url(
        r'^protocoldatasources/(?P<pk>[0-9]+)/links/$',
        views.PDSAvailableLinksView.as_view(),
        name='pds-links'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
