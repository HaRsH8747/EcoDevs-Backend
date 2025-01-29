from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from os.path import basename


from django.db import models
from django.utils.translation import gettext_lazy as _


class ProductChoices(models.TextChoices):
    FIELD_CROPS = 'Field crops (grains or beans)', _('Field crops (grains or beans)')
    FLOWERS = 'Flowers', _('Flowers')
    FRUITS_BERRIES_GRAPES = 'Fruit/berries/grapes', _('Fruit/berries/grapes')
    HAY_FORAGE_CROPS = 'Hay or forage crops', _('Hay or forage crops')
    HERBS = 'Herbs', _('Herbs')
    LIVESTOCK = 'Livestock', _('Livestock')
    SEEDS = 'Seeds, seedlings or nursery stock', _('Seeds, seedlings or nursery stock')
    VEGETABLES = 'Vegetables', _('Vegetables')
    OTHER_PRODUCTS = 'Other products', _('Other products')

class ProvinceChoices(models.TextChoices):
    ALBERTA = 'Alberta', _('Alberta')
    BRITISH_COLUMBIA = 'British Columbia', _('British Columbia')
    MANITOBA = 'Manitoba', _('Manitoba')
    NEW_BRUNSWICK = 'New Brunswick', _('New Brunswick')
    NEWFOUNDLAND = 'Newfoundland', _('Newfoundland')
    NOVA_SCOTIA = 'Nova Scotia', _('Nova Scotia')
    NORTHWEST_TERRITORIES = 'Northwest Territories', _('Northwest Territories')
    NUNAVUT = 'Nunavut', _('Nunavut')
    ONTARIO = 'Ontario', _('Ontario')
    PRINCE_EDWARD_ISLAND = 'Prince Edward Island', _('Prince Edward Island')
    QUEBEC = 'Quebec', _('Quebec')
    SASKATCHEWAN = 'Saskatchewan', _('Saskatchewan')
    YUKON = 'Yukon', _('Yukon')

class StatusChoices(models.TextChoices):
    ACCEPTED = 'Accepted', _('Accepted')
    PENDING = 'Pending', _('Pending')
    REJECTED = 'Rejected', _('Rejected')

class Storage(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    province = models.CharField(
        max_length=100,
        choices=ProvinceChoices.choices,
        null = True
    )
    capacity = models.PositiveIntegerField()
    crop_type = models.CharField(
        max_length=100,
        choices=ProductChoices.choices,
        null = True,
    )
    min_renting_period = models.PositiveIntegerField()
    status = models.CharField(
        max_length=100,
        choices=StatusChoices.choices,
        default = StatusChoices.PENDING,
    )

    def __str__(self):
        return self.name

class Designation(models.TextChoices):
    FARMER = "F", _("Farmer")
    LANDOWNER = "L", _("Land Owner")
    ADMIN = "A", _("Admin")

class ExtendedUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(
        max_length=1, choices=Designation.choices, default=Designation.ADMIN, null=False
    )
    about_me = models.TextField(null=True)

    def __str__(self):
        return self.user.username

class ProductChoices(models.TextChoices):
    FIELD_CROPS = 'Field crops (grains or beans)', _('Field crops (grains or beans)')
    FLOWERS = 'Flowers', _('Flowers')
    FRUITS_BERRIES_GRAPES = 'Fruit/berries/grapes', _('Fruit/berries/grapes')
    HAY_FORAGE_CROPS = 'Hay or forage crops', _('Hay or forage crops')
    HERBS = 'Herbs', _('Herbs')
    LIVESTOCK = 'Livestock', _('Livestock')
    SEEDS = 'Seeds, seedlings or nursery stock', _('Seeds, seedlings or nursery stock')
    VEGETABLES = 'Vegetables', _('Vegetables')
    OTHER_PRODUCTS = 'Other products', _('Other products')

class Product(models.Model):
    product_item = models.CharField(
        max_length=100,
        choices=ProductChoices.choices,
        null = True,
    )

    def __str__(self):
        return self.product_item


class EquipmentChoices(models.TextChoices):
    HOUSING = 'Housing', _('Housing')
    IRRIGATION_CAPACITY = 'Irrigation capacity', _('Irrigation capacity')
    IRRIGATION_EQUIPMENT = 'Irrigation equipment', _('Irrigation equipment')
    GREENHOUSE = 'Greenhouse', _('Greenhouse')
    FENCING = 'Fencing', _('Fencing')
    AGRICULTURAL_MACHINERY = 'Agricultural machinery', _('Agricultural machinery')
    COLD_STORAGE = 'Cold storage', _('Cold storage')
    PROCESSING_FACILITIES = 'Processing facilities', _('Processing facilities')
    OTHER_FACILITIES = 'Other facilities', _('Other facilities')
class ProvinceChoices(models.TextChoices):
    ALBERTA = 'Alberta', _('Alberta')
    BRITISH_COLUMBIA = 'British Columbia', _('British Columbia')
    MANITOBA = 'Manitoba', _('Manitoba')
    NEW_BRUNSWICK = 'New Brunswick', _('New Brunswick')
    NEWFOUNDLAND = 'Newfoundland', _('Newfoundland')
    NOVA_SCOTIA = 'Nova Scotia', _('Nova Scotia')
    NORTHWEST_TERRITORIES = 'Northwest Territories', _('Northwest Territories')
    NUNAVUT = 'Nunavut', _('Nunavut')
    ONTARIO = 'Ontario', _('Ontario')
    PRINCE_EDWARD_ISLAND = 'Prince Edward Island', _('Prince Edward Island')
    QUEBEC = 'Quebec', _('Quebec')
    SASKATCHEWAN = 'Saskatchewan', _('Saskatchewan')
    YUKON = 'Yukon', _('Yukon')
class FarmerDetail(models.Model):
    email = models.CharField(max_length=255)
    phoneNo = models.CharField(max_length=255)
    extendeduser = models.ForeignKey(ExtendedUser, on_delete=models.CASCADE)
    experience = models.IntegerField(null = True)
    product_planning_to_produce = models.ManyToManyField(Product)
    equipment_needed = models.CharField(
        max_length=100,
        choices=EquipmentChoices.choices,
        null = True
    )
    province_to_farm = models.CharField(
        max_length=100,
        choices=ProvinceChoices.choices,
        null = True
    )

    def __str__(self):
        return self.extendeduser.user.username
    

class FarmlandChoices(models.TextChoices):
    ON_FARM_EMPLOYMENT = 'On-farm employment', _('On-farm employment')
    MENTORING = 'Mentoring', _('Mentoring')
    INTERNSHIP = 'Internship', _('Internship')
    BUSINESS_PARTNERSHIP = 'Business partnership', _('Business partnership')
    LEASE = 'Lease', _('Lease')
    LEASE_TO_OWN = 'Lease-to-own', _('Lease-to-own')
class SoilTypeChoices(models.TextChoices):
    CLAY = 'Clay', _('Clay')
    LOAM = 'Loam', _('Loam')
    SAND = 'Sand', _('Sand')
    CLAY_LOAM = 'Clay loam', _('Clay loam')
    SANDY_LOAM = 'Sandy loam', _('Sandy loam')
    OTHER_SOIL_TYPE = 'Other soil type', _('Other soil type')
    UNKNOWN = 'Unknown', _('Unknown')

class LandUseChoices(models.TextChoices):
    LIVESTOCK = 'Livestock', _('Livestock')
    FIELD_CROPS = 'Field crops', _('Field crops')
    MARKET_GARDEN = 'Market garden', _('Market garden')
    HAY_OR_PASTURE = 'Hay or pasture', _('Hay or pasture')
    FALLOW = 'Fallow', _('Fallow')
    WOODLOT = 'Woodlot', _('Woodlot')
    VEGETABLES = 'Vegetables', _('Vegetables')
    FRUIT_BERRIES_GRAPES = 'Fruit/berries/grapes', _('Fruit/berries/grapes')
    OTHER_USE = 'Other use', _('Other use')
    NOT_IN_USE = 'Not in use', _('Not in use')

class FacilityAndEquipmentChoices(models.TextChoices):
    HOUSING = 'Housing', _('Housing')
    IRRIGATION_CAPACITY = 'Irrigation capacity', _('Irrigation capacity')
    IRRIGATION_EQUIPMENT = 'Irrigation equipment', _('Irrigation equipment')
    GREENHOUSE = 'Greenhouse', _('Greenhouse')
    FENCING = 'Fencing', _('Fencing')
    AGRICULTURAL_MACHINERY = 'Agricultural machinery', _('Agricultural machinery')
    COLD_STORAGE = 'Cold storage', _('Cold storage')
    PROCESSING_FACILITIES = 'Processing facilities', _('Processing facilities')
    OTHER_FACILITIES = 'Other facilities', _('Other facilities')

class ExperienceNeededChoices(models.TextChoices):
    NOT_YET_STARTED = 'Not yet started', _('Not yet started')
    LESS_THAN_1_YEAR = 'Less than 1 year', _('Less than 1 year')
    ABOUT_1_YEAR = 'About 1 year', _('About 1 year')
    ONE_TO_TWO_YEARS = '1-2 years', _('1-2 years')
    THREE_TO_FIVE_YEARS = '3-5 years', _('3-5 years')
    SIX_TO_TEN_YEARS = '6-10 years', _('6-10 years')
    NO_PREFERENCE = 'No preference', _('No preference')

class ProductChoices(models.TextChoices):
    FIELD_CROPS = 'Field crops (grains or beans)', _('Field crops (grains or beans)')
    FLOWERS = 'Flowers', _('Flowers')
    FRUITS_BERRIES_GRAPES = 'Fruit/berries/grapes', _('Fruit/berries/grapes')
    HAY_FORAGE_CROPS = 'Hay or forage crops', _('Hay or forage crops')
    HERBS = 'Herbs', _('Herbs')
    LIVESTOCK = 'Livestock', _('Livestock')
    SEEDS = 'Seeds, seedlings or nursery stock', _('Seeds, seedlings or nursery stock')
    VEGETABLES = 'Vegetables', _('Vegetables')
    OTHER_PRODUCTS = 'Other products', _('Other products')

class ProvinceChoices(models.TextChoices):
    ALBERTA = 'Alberta', _('Alberta')
    BRITISH_COLUMBIA = 'British Columbia', _('British Columbia')
    MANITOBA = 'Manitoba', _('Manitoba')
    NEW_BRUNSWICK = 'New Brunswick', _('New Brunswick')
    NEWFOUNDLAND = 'Newfoundland', _('Newfoundland')
    NOVA_SCOTIA = 'Nova Scotia', _('Nova Scotia')
    NORTHWEST_TERRITORIES = 'Northwest Territories', _('Northwest Territories')
    NUNAVUT = 'Nunavut', _('Nunavut')
    ONTARIO = 'Ontario', _('Ontario')
    PRINCE_EDWARD_ISLAND = 'Prince Edward Island', _('Prince Edward Island')
    QUEBEC = 'Quebec', _('Quebec')
    SASKATCHEWAN = 'Saskatchewan', _('Saskatchewan')
    YUKON = 'Yukon', _('Yukon')

class StatusChoices(models.TextChoices):
    ACCEPTED = 'Accepted', _('Accepted')
    PENDING = 'Pending', _('Pending')
    REJECTED = 'Rejected', _('Rejected')

class Storage(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    province = models.CharField(
        max_length=100,
        choices=ProvinceChoices.choices,
        null = True
    )
    capacity = models.PositiveIntegerField()
    crop_type = models.CharField(
        max_length=100,
        choices=ProductChoices.choices,
        null = True,
    )
    min_renting_period = models.PositiveIntegerField()
    status = models.CharField(
        max_length=100,
        choices=StatusChoices.choices,
        default = StatusChoices.PENDING,
    )

    def __str__(self):
        return self.name

class Image(models.Model):
    photo = models.ImageField(upload_to='images/')

    def __str__(self):
        return basename(self.photo.name)

class Land(models.Model):
    extendeduser = models.ForeignKey(ExtendedUser, on_delete=models.CASCADE)
    land_name = models.CharField(max_length=255, null=True)
    land_image = models.ManyToManyField(Image)
    latitude = models.FloatField()
    longitude = models.FloatField()
    street_address = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    province = models.CharField(max_length=100,
        choices=ProvinceChoices.choices,
        null = True)
    land_size = models.CharField(max_length=255, null=True)
    farmland_available_for = models.CharField(
        max_length=100,
        choices=FarmlandChoices.choices,
    )
    type_of_soil = models.CharField(
        max_length=100,
        choices=SoilTypeChoices.choices,
    )
    and_currently_being_used_for = models.CharField(
        max_length=100,
        choices=LandUseChoices.choices,
    )
    facility_and_equipment = models.CharField(
        max_length=100,
        choices=FacilityAndEquipmentChoices.choices,
    )
    experience_needed = models.CharField(
        max_length=100,
        choices=ExperienceNeededChoices.choices,
    )

    def __str__(self):
        return (self.extendeduser.user.username +" - "+self.street_address)

class StatusChoices(models.TextChoices):
    ACCEPTED = 'Accepted', _('Accepted')
    PENDING = 'Pending', _('Pending')
    REJECTED = 'Rejected', _('Rejected')

class LandApplication(models.Model):
    landowner = models.ForeignKey(ExtendedUser, on_delete=models.CASCADE, related_name='land_applications_owned')
    farmer = models.ForeignKey(ExtendedUser, on_delete=models.CASCADE, related_name='land_applications_applied')
    landid = models.ForeignKey(Land, on_delete=models.CASCADE)
    application_date = models.DateField(auto_now_add=True)
    status = models.CharField(
        max_length=100,
        choices=StatusChoices.choices,
        default = StatusChoices.PENDING,
    )
    facility_and_equipment_agreed_to = models.CharField(
        max_length=100,
        choices=FacilityAndEquipmentChoices.choices,
    )
    application_description = models.TextField(blank=True, null=True)
    product_planning_to_produce = models.CharField(
        max_length=100,
        choices=ProductChoices.choices,
        null=True
    )


class LandAgreement(models.Model):
    land_application = models.OneToOneField(LandApplication, on_delete=models.CASCADE, null=True)
    landowner = models.ForeignKey(ExtendedUser, on_delete=models.CASCADE, related_name='land_agreements_owned')
    farmer = models.ForeignKey(ExtendedUser, on_delete=models.CASCADE, related_name='land_agreements_signed')
    landid = models.ForeignKey(Land, on_delete=models.CASCADE)
    agreement_duration = models.CharField(max_length=255, null=True)
    agreement_starting_date = models.DateField(auto_now_add=True)
    product_planning_to_produce = models.ManyToManyField(Product)
    facility_and_equipment_agreed_to = models.CharField(
        max_length=100,
        choices=FacilityAndEquipmentChoices.choices,
    )
    agreement_description = models.TextField(blank=True, null=True)

class StorageApplications(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    crop_name = models.CharField(max_length=100)
    weight = models.FloatField()
    area_needed = models.FloatField()
    need_vehicle = models.BooleanField(default=False, blank=True)
    vehicle_type = models.CharField(max_length=100, blank=True, null=True)
    distance = models.FloatField(blank=True, null=True)
    pickup_address = models.TextField(blank=True, null=True)
    pickup_date_time = models.DateTimeField(blank=True, null=True)
    total_cost = models.FloatField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.crop_name}"
