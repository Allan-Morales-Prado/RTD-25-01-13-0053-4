from django.contrib import admin
from .models import Countries, CodesAll

@admin.register(Countries)
class CountriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    readonly_fields = ('name', 'code')
    search_fields = ('name',)

@admin.register(CodesAll)
class CodesAllAdmin(admin.ModelAdmin):
    list_display = ('entity', 'currency', 'alphabeticcode')
    readonly_fields = ('entity', 'currency', 'alphabeticcode')
    search_fields = ('entity', 'currency', 'alphabeticcode')