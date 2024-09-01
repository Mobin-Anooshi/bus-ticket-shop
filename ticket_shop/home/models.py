from django.db import models
from django.db.models.signals import pre_save,post_save,pre_migrate
from django.contrib.auth import get_user_model  

class Cars(models.Model):
    choice_car = {
        'car':'CAR',
        'bus':'BUS',
        'van':'VAN'
    }
    car = models.CharField(max_length=3,choices=choice_car)
    number = models.CharField(max_length=8)
    model = models.CharField(max_length=30)
    chair = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f'{self.car} - {self.model}'
    
    

class Travel(models.Model):
    car = models.ForeignKey(Cars,on_delete=models.CASCADE)
    driver = models.ForeignKey('accounts.Driver',on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    price = models.PositiveIntegerField(default=0)
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    destance = models.PositiveIntegerField(default='0')
    valid =models.BooleanField(default=False)
    sell_chair = models.SmallIntegerField(default=0,)
        
    
    
    def __str__(self):
        return f"{self.destination}"
    
    def sell_chairs(self):
        self.sell_chair += 1
        return self.save(self)
    
    
    
class Distance(models.Model):
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    o_d = models.PositiveIntegerField(default='0')
    
    def __str__(self):
        return self.origin
    
    
    
def create_distance(sender,instance,**kwargs):
    d = Distance.objects.filter(origin=instance.origin, destination=instance.destination)
    
    if d.exists():
        instance.destance = d[0].o_d
        
    else:
        from home.destination import main
        destance = main(place1=instance.origin,place2=instance.destination)
        instance.destance = int(destance) 
    if not instance.destance == 0:
        instance.valid = True
        instance.price = instance.destance * 1200
    else:
        instance.valid=False
        print('-'*90)
    # instance.save()
        

pre_save.connect(receiver=create_distance,sender=Travel)



class Ticket(models.Model):
    user = models.ForeignKey('accounts.User',on_delete=models.CASCADE)
    travel = models.ForeignKey(Travel,on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    
    def __str__(self) :
        return f'{self.user}-{self.travel}'
    
    
    