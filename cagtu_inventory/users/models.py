from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email,company_name, phone_number, password=None):
        if not email:
            raise ValueError("email is required")
        if not company_name:
            raise ValueError("company name is required")
        if not phone_number:
            raise ValueError("prepare provide an active phone number")
        
        user = self.model(
            email = self.normalize_email(email),
            company_name = company_name,
            phone = phone_number
        )
        user.set_password(password)
        user.save(using=self._db)
        return user 


class Users(AbstractBaseUser):
    email = models.EmailField(verbose_name="email address", max_length=60, unique=True)
    company_name = models.CharField(verbose_name="company name",max_length=60)
    phone_number = models.CharField(max_length=20, verbose_name="phone number")
    date_joined = models.DateTimeField(verbose_name= "date joined",auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True )
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff =  models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["company_name","phone_number",]

    def __str__(self):
        return self.company_name

    
    def has_perm(self, perm, obj=None):
        return True


    def has_module_perms(self, app_label):
        return True 
 

