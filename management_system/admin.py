from django.contrib import admin

from .models import *

# Register your models here.

class ImagesInline(admin.TabularInline):
    model = Images
    fields = ('id', 'file', 'img_preview',)
    readonly_fields = ('id', 'img_preview',)
class VaccineInline(admin.TabularInline):
    model = Vaccine

class AnimalAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'pub_date',
        'gender',
        'status',
        'size',
        'age',
        'breed',
        'img_preview',
    )
    search_fields = ('id', 'name')
    list_per_page = 30
    list_filter = ('gender', 'status', 'size', 'age', 'breed')
    fieldsets = (
        ('Informações', {
            "fields": (
                'name', 'observation', 'pub_date', 'status',
            ),
            "description": 'Informações basicas do animal',
        }),
        # ('Arquivos', {
        #     "fields": (
        #         ('img_preview', 'image',),
        #     ),
        #     "description": 'Documentos de identificação do animal',
        # }),
        ('Caracteristicas', {
            "fields": (
                'gender', 'size', 'age' , 'breed', 'color', 'type',
            ),
            "description": 'Caracterisitas do animal',
        }),
        # ('Vacinação', {
        #     "fields": (
        #         'vaccinations',
        #     ),
        #     "description": 'Vacinas aplicadas ao animal',
        # }),
    )
    readonly_fields = ('id', 'img_preview',)
    inlines = [ImagesInline, VaccineInline]
    def save_model(self, request, obj, form, change):
        obj.save()
    
admin.site.register(Animal, AnimalAdmin)

@admin.register(Vaccine)
class VaccineAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )
    search_fields = ('id', 'name')
    list_per_page = 30

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )
    search_fields = ('id', 'name')
    list_per_page = 30

@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'breed_type',
    )
    search_fields = ('id', 'breed_type')
    list_per_page = 30

@admin.register(Adopter)
class AdopterAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'phone',
        'email',
    )
    search_fields = ('id', 'name', 'phone', 'email')
    list_per_page = 30

@admin.register(Adoption)
class AdoptionAdmin(admin.ModelAdmin):
    pass

@admin.register(AnimalType)
class AnimalTypeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'animal_type',
    )
    search_fields = ('id', 'animal_type')
    list_per_page = 30

@admin.register(AnimalStatus)
class AnimalStatusAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'animal_status',
    )
    search_fields = ('id', 'animal_status')
    list_per_page = 30

@admin.register(AnimalSize)
class AnimalSizeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'animal_size',
    )
    search_fields = ('id', 'animal_size')
    list_per_page = 30

@admin.register(Telephone)
class TelephoneAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'ddd',
        'numero',
    )
    search_fields = ('id', 'numero')
    list_per_page = 30

@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'file',       
        'img_preview', 
    )
    search_fields = ('id', 'file')
    list_per_page = 30
    readonly_fields = ['img_preview']