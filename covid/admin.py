from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(covid)
class covidAdmin(admin.ModelAdmin):
    list_display = ('ResponseID',
                    'startdate',
                    'enddate',
                    'first_name',
                    'last_name',
                    'birthday',
                    'address',
                    'primary_phone',
                    'secondary_phone',
                    'email',
                    'type',
                    'first_childname',
                    'second_childname',
                    'child_lastname',
                    'child_dob',
                    'cohort_id',
                    )
    search_fields = ('cohort_id',
                     )
    list_filter=(
                 'enddate',
                 'type',
                 'birthday',

                 )