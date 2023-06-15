from django.db import models
from django.db.models import Q

from django.contrib.auth.models import BaseUserManager,AbstractBaseUser ,PermissionsMixin 

class UserManager(BaseUserManager,models.Manager):

    def _create_user(self, username, email ,password, is_staff, is_superuser, is_active, **extra_fields):
        user = self.model(
            username = username,
            email = email,
            is_staff = is_staff,
            is_superuser = is_superuser,
            is_active = is_active,
            **extra_fields

        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,username,email,password=None,**extra_fields):
        return self._create_user(username, email, password, False, False, True,**extra_fields)

    def create_superuser(self, username,email ,password=None, **extra_fields):
        return self._create_user(username, email, password ,True , True, True, **extra_fields)

    def listar_cuidadores(self):
   
        return self.filter(
            categoria = 2 
        )
    

    
class MascotaManager(models.Manager):

    def mascota_por_user(self,usuario):

        return self.filter(
            user=usuario,
        )
    
class HorasManager(models.Manager):

    def horas_por_user(self,usuario):

        return self.filter(
            user=usuario,
        )





