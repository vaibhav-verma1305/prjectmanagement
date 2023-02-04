from django.db import models
from django.contrib.auth.models import User

class First_year(models.Model):
    regnumber = models.IntegerField(null=True)
    enrollment1 = models.CharField(max_length=30)
    admission1 = models.CharField(max_length=30)
    name1 = models.CharField(max_length=30)
    email1 = models.EmailField()
    phone1= models.CharField(max_length=30)
    enrollment2 = models.CharField(max_length=30)
    admission2= models.CharField(max_length=30)
    name2 = models.CharField(max_length=30)
    email2 = models.EmailField()
    phone2= models.CharField(max_length=30) 
    enrollment3 = models.CharField(max_length=30)
    admission3 = models.CharField(max_length=30)
    name3 = models.CharField(max_length=30)
    email3 = models.EmailField()
    phone3= models.CharField(max_length=30)
    def _str_(self):
        return self.name1
class Second_year(models.Model):
    regnumber = models.IntegerField(null=True)
    enrollment4 = models.CharField(max_length=30)
    admission4 = models.CharField(max_length=30)
    name4 = models.CharField(max_length=30)
    email4 = models.EmailField()
    phone4= models.CharField(max_length=30)
    enrollment5 = models.CharField(max_length=30)
    admission5= models.CharField(max_length=30)
    name5 = models.CharField(max_length=30)
    email5 = models.EmailField()
    phone5= models.CharField(max_length=30) 
    enrollment6 = models.CharField(max_length=30)
    admission6 = models.CharField(max_length=30)
    name6 = models.CharField(max_length=30)
    email6 = models.EmailField()
    phone6= models.CharField(max_length=30)
    def _str_(self):
        return self.name4
class Third_year(models.Model):
    regnumber = models.IntegerField(null=True)
    enrollment7 = models.CharField(max_length=30)
    admission7= models.CharField(max_length=30)
    name7 = models.CharField(max_length=30)
    email7 = models.EmailField()
    phone7= models.CharField(max_length=30)
    enrollment8 = models.CharField(max_length=30)
    admission8= models.CharField(max_length=30)
    name8 = models.CharField(max_length=30)
    email8 = models.EmailField()
    phone8= models.CharField(max_length=30) 
    enrollment9 = models.CharField(max_length=30)
    admission9= models.CharField(max_length=30)
    name9 = models.CharField(max_length=30)
    email9 = models.EmailField()
    phone9= models.CharField(max_length=30)
    def _str_(self):
        return self.name7
class Fourth_year(models.Model):
    regnumber = models.IntegerField(null=True)
    enrollment10 = models.CharField(max_length=30)
    admission10 = models.CharField(max_length=30)
    name10 = models.CharField(max_length=30)
    email10 = models.EmailField()
    phone10= models.CharField(max_length=30)
    enrollment11 = models.CharField(max_length=30)
    admission11= models.CharField(max_length=30)
    name11 = models.CharField(max_length=30)
    email11 = models.EmailField()
    phone11= models.CharField(max_length=30) 
    enrollment12 = models.CharField(max_length=30)
    admission12 = models.CharField(max_length=30)
    name12 = models.CharField(max_length=30)
    email12 = models.EmailField()
    phone12= models.CharField(max_length=30)
    def _str_(self):
        return self.name11
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    forget_password_token= models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    def _str_(self):
        return self.user.username
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_student=False, is_staff=False, is_admin=False):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            is_student=is_student,
            is_staff=is_staff,
            is_admin=is_admin,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_student(self, email, password=None):
        return self.create_user(
            email,
            password=password,
            is_student=True,
        )

    def create_staff(self, email, password=None):
        return self.create_user(
            email,
            password=password,
            is_staff=True,
        )

    def create_admin(self, email, password=None):
        return self.create_user(
            email,
            password=password,
            is_admin=True,
        )

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_student = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_student(self):
        return self.is_student

    @property
    def is_staff(self):
        return self.is_staff

    @property
    def is_admin(self):
        return self.is_admin
from django.contrib.auth.models import User

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20)