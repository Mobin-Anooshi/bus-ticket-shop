from django.contrib import admin
from home.models import Cars,Travel,Distance,Ticket

# Register your models here.


admin.site.register(Cars)
class TravelAdmin(admin.ModelAdmin):
    list_display = ('origin','destination','car','time','valid')
    readonly_fields = ('price','destance')
admin.site.register(Travel,TravelAdmin)
class DistanceAdmin(admin.ModelAdmin):
    list_display=('origin','destination','o_d')
admin.site.register(Distance,DistanceAdmin)
admin.site.register(Ticket)