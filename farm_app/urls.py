from django.contrib import admin
from django.urls import path, include
from farm_app import views
from django.conf import settings
from django.conf.urls.static import static
from .views import get_csrf_token

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='user-register'),
    path('login/', views.UserLoginView.as_view(), name='user-login'),
    path('api/extendedusers', views.ExtendedUserLists.as_view()),
    path('api/extendedusers/<int:pk>', views.ExtendedUserRetrieveUpdate.as_view()),
    path('api/farmers', views.FarmerLists.as_view()),
    path('api/farmers/<int:pk>', views.FarmerRetrieveUpdate.as_view()),
    path('api/lands', views.LandLists.as_view()),
    path('api/lands/<int:pk>', views.LandRetrieveUpdateDestroy.as_view()),
    path('api/landapplications', views.LandApplicationLists.as_view()),
    path('api/landapplications/<int:pk>', views.LandApplicationRetrieveUpdateDestroy.as_view()),
    path('api/landapplications/<int:pk>/status', views.LandApplicationStatusUpdateView.as_view(), name='update-landapplication-status'),
    path('api/landapplications/create', views.LandApplicationCreateView.as_view()),
    path('api/agreements', views.LandAgreementLists.as_view()),
    path('api/agreements/create', views.LandAgreementLists.as_view()),
    path('api/agreements/<int:pk>', views.LandAgreementRetrieveUpdateDestroy.as_view()),
    path('predict', views.crop_prediction_view, name='predict'),
    path('upload_images/', views.ImageUploadView.as_view(), name='upload_images'),
    path('api/storage', views.StorageLists.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('api/csrf-token/', get_csrf_token, name='get_csrf_token'),

    path('api/storage-application/', views.StorageApplicationView.as_view(), name='storage_application'),
    path('api/storage-application/delete/<int:id>/', views.DeleteStorageApplicationView.as_view(), name='delete_application'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)