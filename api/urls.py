from django.conf.urls import url, include
from rest_framework.authtoken import views

import api.v1.urls

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^v1/', include(api.v1.urls)),
    url(r'^auth-token/', views.obtain_auth_token),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework'))
]
