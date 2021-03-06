from django.contrib import admin
from march.models import *

# Register your models here.
@admin.register(Mcallnote)
class McallnoteAdmin(admin.ModelAdmin):
    list_display = ('SAMPLEID',
                    'call_date',
                    'CALLNOTE',
                    'type',
                    'initial',
                    )
    search_fields = ('SAMPLEID',
                     )
    list_filter=(
                 'call_date',
                 'type',
                 'initial',

                 )

@admin.register(Mcontact)
class McontactAdmin(admin.ModelAdmin):
    list_display = ('q2_1_text',
                    'q2_3_text',
                    'sampleid',
                    )

    list_filter=('sampleid',
               'q2_1_text',
                'q2_3_text',



  )

@admin.register(Mcontactinfo)
class McontactinfoAdmin(admin.ModelAdmin):
    list_display = ('SAMPLEID',
                    'currdate',
                    'address',
                    'phone_num',
                    'text_permission',
                    'other_phone',
                    'other_text_permission',
                    'email',
                    'contact_a',
                    'contact_aphone',
                    'contact_b',
                    'contact_bphone',
                    'source',
                    'PCG',
                    'initial',
                    )
    search_fields = ('SAMPLEID',
                     'phone_num',
                     'other_phone',
                     'contact_aphone',
                     'contact_bphone',

                     )
    list_filter=(
                 'currdate',
                 'source',
                 'initial',
                 'PCG',

                 )
