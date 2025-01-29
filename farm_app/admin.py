from django.contrib import admin
from .models import ExtendedUser, FarmerDetail, Land, LandApplication, LandAgreement, Product, Image, Storage, StorageApplications

@admin.register(ExtendedUser)
class ExtendedUserAdmin(admin.ModelAdmin):
    list_display = ("user", "designation")
admin.site.register(FarmerDetail)

@admin.register(Land)
class LandAdmin(admin.ModelAdmin):
    list_display = ("extendeduser","street_address","city", "land_size")

@admin.register(LandApplication)
class LandApplicationAdmin(admin.ModelAdmin):
    list_display = ("landowner", "farmer","landid" ,"application_date")

admin.site.register(StorageApplications)
admin.site.register(LandAgreement)
admin.site.register(Product)
admin.site.register(Storage)
admin.site.register(Image)