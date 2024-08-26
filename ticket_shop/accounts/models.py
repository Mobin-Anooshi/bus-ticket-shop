from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from accounts.managers import UserManagers
from home.models import Cars
from django.db.models.signals import post_save
# Create your models here.


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255 , unique=True)
    full_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default= False)
    created = models.DateTimeField(auto_now_add=True)
    driver = models.BooleanField(default=False)
    wallet = models.PositiveIntegerField(default=0)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('full_name',)

    objects = UserManagers()    
    
    def __str__(self) -> str:
        return self.email
    
    def has_perm(self,perm , obj=None):
        return True 
    
    def has_module_perms(self,app_lable):
        return True
    
    @property
    def is_staff(self):
        return self.is_superuser



class Driver(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE,related_name='driver_profiles')
    National_code = models.CharField(max_length=10, default='0000000000')

    def __str__(self):
        return f"Driver: {self.user.email}"
    
    



def create_driver(sender ,**kwargs):
    user = User.objects.get(email=kwargs['instance'].email)
    try:
        driver = Driver.objects.get(user=user)
        if not user.driver:
            driver.delete()
    except:
        if user.driver:
            Driver.objects.create(user=user)



post_save.connect(receiver=create_driver,sender=User)