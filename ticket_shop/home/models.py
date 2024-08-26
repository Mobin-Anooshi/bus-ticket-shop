from django.db import models




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
    time = models.DateTimeField()
    price = models.PositiveIntegerField()
    orogin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    destance = models.CharField(default='0')
    
    
    def __str__(self):
        # from home.destination import main
        # main(self.orogin,self.destination)
        return f"{self.destination}"
    

class Distance(models.Model):
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    o_d = models.CharField(max_length=255)
    
    def __str__(self):
        return self.origin
    
    
# def create_distance(sender,**kwargs):
#     d = Distance.objects.filter(origin=kwargs['instance'].origin,destination=kwargs['instance'].destination)
#     if d.exists():
#         pass
    

    # try:
         
    # except:
    #     pass 
    
    