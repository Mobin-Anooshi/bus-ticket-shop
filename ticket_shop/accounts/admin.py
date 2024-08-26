from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.models import User,Driver
from django.contrib.auth.models import Group
from accounts.forms import UserChangeForm,UserCreationForm
# Register your models here.



class UserAdmin (BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    
    list_display = ('email','full_name','is_superuser')
    
    readonly_fields = ('last_login',)
    
    list_filter=('is_superuser',)
    
    fieldsets = (
        (None,{'fields':('email','full_name','password','wallet')}),
        ('permissions',{'fields':('is_active','is_superuser','driver','last_login',)})
    )
    
    add_fieldsets=(
        (None,{'fields':('email','full_name','password1','password2')}),
    )
    
    search_fields = ('email','full_name')
    
    ordering = ('full_name',)
    
    filter_horizontal = ()
    
admin.site.unregister(Group)
admin.site.register(User , UserAdmin)
 
admin.site.register(Driver)