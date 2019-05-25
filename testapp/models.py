from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model): 
    user = models.OneToOneField(User,on_delete='CASCADE')
    desc = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to = 'profile_image',blank=True)
    
    def __str__(self): 
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']: 
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender = User)

class news1(models.Model): 

    n_id = models.AutoField(primary_key = True)
    category = models.CharField(max_length = 64)

    def __str__(self): 
        return self.category

class news_items1(models.Model): 
    ni_id = models.AutoField(primary_key = True)
    des = models.CharField(max_length = 64)
    reporter_name = models.CharField(max_length = 64)
    category_id = models.ForeignKey(news1,on_delete=models.CASCADE)

    def __str__(self): 
        return self.des