from django.urls import path,include
from api.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'profiles',ProfileViewSet)
router.register(r'statuses',StatusViewSet)


## USING ModelViewSet

# profile_viewset = ProfileViewSet.as_view({'get':'list', 'post':'create'})
# profile_detail_viewset = ProfileViewSet.as_view({'get':'retrieve'})
# profile_update_viewset = ProfileViewSet.as_view({'get':'update'})
#
# status_viewset = StatusViewSet.as_view({'get':'list','post':'create'})

# urlpatterns = [
#
#     path('profiles/',ProfileView.as_view()),
#     path('statuses/',StatusView.as_view()),
#
#     path('profile-viewset/',profile_viewset),
#     path('profile-viewset/<int:pk>/',profile_detail_viewset),
#     path('profile-update-viewset/<int:pk>/',profile_update_viewset),
#
#     path('status-viewset/',status_viewset)
# ]
urlpatterns =  [
    path('',include(router.urls)),
]
