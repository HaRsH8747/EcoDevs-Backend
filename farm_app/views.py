from django.shortcuts import render
from rest_framework import generics
from .models import ExtendedUser, FarmerDetail, Land, LandApplication, LandAgreement, Storage,StorageApplications
from .serializers import ExtendedUserSerializers, FarmerDetailSerializers, LandSerializers, LandApplicationSerializers, LandAgreementSerializers, UserRegistrationSerializer, UserLoginSerializer, StorageSerializers, LandApplicationStatusUpdateSerializer,StorageApplicationsSerializer
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework import status, views
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from django.contrib.auth import authenticate, login
from django.db.models import Q
from rest_framework.exceptions import PermissionDenied
from .backends import EmailBackend
from .predictor import predict_crops_and_prices, get_features_from_request
from .serializers import ImageSerializer, LandApplicationCreateSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Image
from django.middleware.csrf import get_token    
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
def crop_prediction_view(request):
    if request.method == 'POST':
        data = request.data
        features = get_features_from_request(data)
        prediction_results = predict_crops_and_prices(features)
        return JsonResponse(prediction_results, safe=False)
    
class UserRegistrationView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User registered successfully.", "id": user.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = EmailBackend().authenticate(request, email=serializer.validated_data['email'], password=serializer.validated_data['password'])
            if user:
                login(request, user)
                return Response({"message": "User logged in successfully.", "user_id": user.id})
            return Response({"message": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class StorageLists(generics.ListCreateAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializers

class ImageUploadView(APIView):
    # parser_classes = (MultiPartParser, FormParser)
        
    def post(self, request, *args, **kwargs):
        files = request.FILES.getlist('images')
        
        if not files:
            return Response({"error": "No files provided."}, status=status.HTTP_400_BAD_REQUEST)
        
        image_objects = []
        for file in files:
            image_instance = Image(photo=file)
            image_instance.save()
            image_objects.append(image_instance)
        
        serializer = ImageSerializer(image_objects, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

# @method_decorator(csrf_exempt, name='dispatch')
class ExtendedUserLists(generics.ListCreateAPIView):
    queryset = ExtendedUser.objects.all()
    serializer_class = ExtendedUserSerializers
    # permission_classes = [permissions.IsAuthenticated]

# @method_decorator(csrf_exempt, name='dispatch')
class ExtendedUserRetrieveUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = ExtendedUserSerializers
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user.id
        return ExtendedUser.objects.filter(user = user)
    
class FarmerLists(generics.ListCreateAPIView):
    queryset = FarmerDetail.objects.all()
    serializer_class = FarmerDetailSerializers
    # permission_classes = [permissions.IsAuthenticated]


class FarmerRetrieveUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = FarmerDetailSerializers
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return FarmerDetail.objects.filter(extendeduser__user = user)


class LandLists(generics.ListCreateAPIView):
    queryset = Land.objects.all()
    serializer_class = LandSerializers
    # permission_classes = [permissions.IsAuthenticated]

class LandRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LandSerializers
    # permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Land.objects.filter(extendeduser__user = user)
    
def get_csrf_token(request):
    return JsonResponse({'csrfToken': get_token(request)})
    
class LandApplicationLists(generics.ListCreateAPIView):
    queryset = LandApplication.objects.all()
    serializer_class = LandApplicationSerializers

class LandApplicationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LandApplicationSerializers

    def get_queryset(self):
        queryset = LandApplication.objects.all()
        return queryset
    
class LandApplicationStatusUpdateView(generics.UpdateAPIView):
    queryset = LandApplication.objects.all()
    serializer_class = LandApplicationStatusUpdateSerializer

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LandAgreementLists(generics.ListCreateAPIView):
    queryset = LandAgreement.objects.all()
    serializer_class = LandAgreementSerializers

class LandAgreementRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LandAgreementSerializers

    def get_queryset(self):
        # untill we use JWT in the frontend
        # user = self.request.user
        # if not user.is_authenticated:
        #     raise PermissionDenied("You must be logged in to access this resource.")
        # queryset = LandAgreement.objects.filter(Q(landowner__user=user) | Q(farmer__user=user))
        # if not queryset.exists():
        #     raise PermissionDenied("You do not have access to this resource.")
        # return queryset

        queryset = LandAgreement.objects.all()
        return queryset

class LandApplicationCreateView(generics.CreateAPIView):
    serializer_class = LandApplicationCreateSerializer

    def perform_create(self, serializer):
        serializer.save()
        
class LandApplicationUpdateStatusView(generics.CreateAPIView):
    serializer_class = LandApplicationCreateSerializer

    def perform_create(self, serializer):
        serializer.save()

class LandAgreementCreateView(generics.UpdateAPIView):
    queryset = LandApplication.objects.all()
    serializer_class = LandApplicationStatusUpdateSerializer

class StorageApplicationView(APIView):
    def post(self, request):
        serializer = StorageApplicationsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Application submitted successfully', 'id': serializer.data['id']}, status=status.HTTP_201_CREATED)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class DeleteStorageApplicationView(APIView):
    def delete(self, request, id):
        try:
            application = StorageApplications.objects.get(id=id)
            application.delete()
            return Response({'message': 'Application deleted successfully'}, status=status.HTTP_200_OK)
        except StorageApplications.DoesNotExist:
            return Response({'error': 'Application not found'}, status=status.HTTP_404_NOT_FOUND)