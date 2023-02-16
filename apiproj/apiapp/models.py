from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

class User_Manager(BaseUserManager):
    def create_user(self,email,username,password,is_active = True,is_staff = None,is_admin = None):
        if not email:
            raise ValueError("Must have n email adress")
        if not password:
            raise ValueError("password invalid")
        user_obj = self.model(
            email = self.normalize_email(email)
        )
        
        user_obj.set_password(password)
        user_obj.staff = is_staff 
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.username = username

        user_obj.save(using = self._db)
    
    def creat_staffuser(self,email,password = None):
        user = self.create_user(
            email,
            password = password,
            is_staff = True

        )
        return user
    def create_superuser(self,email,username,password = None):
        user = self.create_user(
            
            email,
            username = username,
            password = password,
            is_staff = True,
            is_admin = True,
            is_active=True,
            

        )
    
        return user



# Create your models here.
class newuser(AbstractBaseUser):

    category_choices = [('STUDENT','STUDENT'),('TEACHER','TEACHER'),('GRAD','GRAD')]
    email = models.EmailField( max_length=254,unique = True)
    username = models.CharField(max_length=200)
    # phone = models.IntegerField(null=True)
    category = models.CharField(max_length = 10,choices = category_choices,default = 'STUDENT')
    is_active   =models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    latest_login = models.DateTimeField(auto_now = True)
    isverified = models.BooleanField(default = False) 
    staff= models.BooleanField(default = False)
    admin = models.BooleanField(default = False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    object = User_Manager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self,apiapp):
        return True

    @property
    def is_staff(self):
        return self.staff
    @property
    def is_admin(self):
        return self.is_admin
    
    # @property
    # def is_active(self):
    #     return self.is_active


# class profile(models.Model):
#     newuser = models.OneToOneField(newuser)
    
    #extend extra data like fname , pref, data most viewed



class infodata(models.Model):
    category_choices = [('Science','Science'),('Eco','Eco'),('History','History'),('Tech','Tech')]
    data_id = models.IntegerField(primary_key = True)
    topic = models.CharField(max_length=120)
    informationdata = models.TextField(max_length=10000,blank=True)
    title = models.CharField(max_length=120)
    #time = models.DateTimeField(auto_now_add=True)#auto add now makes the field non editable hence it does not show up in admin site
    tags = models.TextField(max_length=120,null=True)
    #userid of the person posting the data 
    views = models.IntegerField(default=0)
    category = models.CharField(max_length = 50,choices=category_choices)
    image = models.ImageField(upload_to='apiapp/images',default ="" ,null=True)
    usertype = models.CharField(max_length=120,default="")
    def __str__(self):
        return self.title


class tasks(models.Model):
  
    taskid = models.IntegerField(primary_key = True)
    taskname = models.CharField(max_length = 120,default="Newtask")
    tskdetail = models.CharField(max_length = 50,default = "")
#to include the user who is linked to the task we make userid a foreignkey
    owner = models.ForeignKey('newuser',related_name='teacher',on_delete=models.CASCADE)
    assigned_to = models.ForeignKey('newuser',related_name='student',on_delete=models.CASCADE)
    task_topic = models.CharField(max_length=25,default='')
    def __str__(self):
        return self.taskname

    
