from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Acallnote)
class AcallnoteAdmin(admin.ModelAdmin):
    list_display = ('family_ID',
                    'ARCH_ID',
                    'call_date',
                    'call_note',
                    'type',
                    'initial',
                    )
    search_fields = ('ARCH_ID',
                     )
    list_filter=(
                 'call_date',
                 'initial',

                 )
    fieldsets = [(None, {'fields': ['family_ID', 'ARCH_ID']}),
                 (u'Other Information', {
                     'classes': ('12',),
                     'fields': ['call_date', 'call_note', 'type', 'initial']})]

@admin.register(archtrack)
class archtrackAdmin(admin.ModelAdmin):
    list_display = ( 'arch_id',
                     'child_id',
                     'birthday',
                     'date_recent',
                     'echoreconsent',
                     'mom_firstname',
                     'mom_lastname',
                     'echo_id',
                     'echo_pin',
                    )
    search_fields = ('arch_id',
                     'child_id',
                     'mom_firstname',
                     'mom_lastname',
                     'echo_id',
                     )
    list_filter = (
        'echoreconsent',
        'age',
        'birthday',
    )

@admin.register(archallcontact)
class archallcontactAdmin(admin.ModelAdmin):
    list_display = ('ARCHID',
                    'currdate',
                    'address',
                    'phone_num',
                    'text_permission',
                    'text_num',
                    'other_phone',
                    'other_text_permission',
                    'email',
                    'source',
                    )
    search_fields = ('ARCHID',
                     )
    list_filter=(
                 'currdate',
                 'source',
                 'initial',
                )
