from django.contrib import admin
from infoGatherer.models import Personal_Information, Payer, Insurance_Information
      
class PIAdmin(admin.ModelAdmin):
    #fields = (('first_name','middle_name','last_name'),)
    #list_dsipaly = (('first_name','middle_name','last_name'),)
    #list_editable = ()
    pass

class PayerAdmin(admin.ModelAdmin):
    list_display = ('code','name','address','city','state','zip','phone','type',)
    list_editable = ('code','name','address','city','state','zip','phone','type',)
    
class IIAdmin(admin.ModelAdmin):
    list_display = ('insurance_id',)

class LogAdmin(admin.ModelAdmin):
    pass
    #list_display = ('insurance_id','log_user','log_type',)
 
admin.site.register(Personal_Information, PIAdmin) 
admin.site.register(Payer, PayerAdmin)
admin.site.register(Insurance_Information, IIAdmin)
