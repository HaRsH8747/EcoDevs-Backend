from rest_framework import serializers
from .models import ExtendedUser, FarmerDetail, Land, LandApplication, LandAgreement, Product, Image, Storage, StatusChoices,StorageApplications
from django.contrib.auth import get_user_model
import base64
from django.core.files.base import ContentFile

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, style={'input_type': 'password'})

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ExtendedUserSerializers(serializers.ModelSerializer):
    user = UserSerializer()
    user_name = serializers.ReadOnlyField(source = 'user.username')
    class Meta:
        model = ExtendedUser
        fields = '__all__'

    # same thing
    # def get_extendeduser_name(self, obj):
    #     user = User.objects.get(id=obj.user.id)
    #     return user.username

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_item']  

class FarmerDetailSerializers(serializers.ModelSerializer):
    farmer_name = serializers.ReadOnlyField(source = 'extendeduser.user.username')
    product_planning_to_produce = ProductSerializer(many=True)

    class Meta:
        model = FarmerDetail
        fields = ['id', 'email', 'phoneNo','extendeduser', 'farmer_name', 'experience', 'product_planning_to_produce', 'equipment_needed', 'province_to_farm']

    # def get_farmer_name(self, obj):
    #     user = User.objects.get(id=obj.extendeduser.user.id)
    #     return user.username

class StorageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id']

    # def create(self, validated_data):
    #     photo_data = validated_data.pop('photo')
    #     photo = self.decode_base64_image(photo_data)
    #     return Image.objects.create(photo=photo)

    # def decode_base64_image(self, photo_data):
    #     format, imgstr = photo_data.split(';base64,')
    #     ext = format.split('/')[-1]
    #     return ContentFile(base64.b64decode(imgstr), name=f'image.{ext}')

class LandSerializers(serializers.ModelSerializer):
    land_owner_name = serializers.SerializerMethodField()
    land_image_names = serializers.SerializerMethodField()
    land_owner_id = serializers.SerializerMethodField()

    class Meta:
        model = Land
        fields = '__all__'

    def get_land_owner_id(self, obj):
        user = User.objects.get(id=obj.extendeduser.user_id)
        return obj.extendeduser.id

    def get_land_owner_name(self, obj):
        user = User.objects.get(id=obj.extendeduser.user.id)
        return user.username
    
    def get_land_image_names(self, obj):
        image_names = [image.photo.name for image in obj.land_image.all()]
        return image_names

class LandDetailForApplicationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Land
        fields = '__all__'
        
class LandApplicationSerializers(serializers.ModelSerializer):
    landowner_name = serializers.ReadOnlyField(source = 'extendeduser.user.username')
    farmer_name = serializers.ReadOnlyField(source = 'extendeduser.user.username')
    land_street_address = serializers.ReadOnlyField(source = 'land.street_address')
    farmer_interested_to_produce_items = ProductSerializer(source='farmer_interested_to_produce', many=True, read_only=True)
    landowner_extended = ExtendedUserSerializers(source='landowner', read_only=True)
    farmer_extended = ExtendedUserSerializers(source='farmer', read_only=True)
    land_detail = LandDetailForApplicationSerializers(source='landid', read_only=True)
    
    class Meta:
        model = LandApplication
        fields = '__all__'


class LandAgreementSerializers(serializers.ModelSerializer):
    landowner_name = serializers.SerializerMethodField()
    farmer_name = serializers.SerializerMethodField()
    landowner_extended = ExtendedUserSerializers(source='landowner', read_only=True)
    farmer_extended = ExtendedUserSerializers(source='farmer', read_only=True)
    land_detail = LandDetailForApplicationSerializers(source='landid', read_only=True)

    class Meta:
        model = LandAgreement
        fields = '__all__'

    def get_landowner_name(self, obj):
        return obj.landowner.user.username

    def get_farmer_name(self, obj):
        return obj.farmer.user.username

    # def get_farmer_interested_to_produce_names(self, instance):
    #     return ", ".join(str(product) for product in instance.farmer_interested_to_produce.all())


class LandApplicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandApplication
        fields = '__all__'

class LandApplicationStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandApplication
        fields = ['status']

class StorageApplicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageApplications
        fields = '__all__'
