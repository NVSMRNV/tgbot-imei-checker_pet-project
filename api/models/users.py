from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

class UserManager(BaseUserManager):
    def _create_user(self, uid, password, **extra_fields):
        if not uid:
            raise ValueError('Нет ID пользователя.')
        user = self.model(uid=uid, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)        
        return user
    
    def create_user(self, uid, password, **extra_fields):
        return self._create_user(uid, password, **extra_fields)
    
    def create_superuser(self, uid, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_staff', True)
        return self._create_user(uid, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    last_login = None

    uid = models.PositiveBigIntegerField(
        verbose_name='Телеграм ID пользователя',
        unique=True,
        primary_key=True,
    )
    token = models.CharField(
        verbose_name='Токен',
        max_length=255,
        unique=True,
    )
    joined = models.DateTimeField(
        verbose_name='Дата присоединения',
        auto_now_add=True,
    )
    is_active = models.BooleanField(
        default=True
    )
    is_superuser = models.BooleanField(
        default=False
    )
    is_staff = models.BooleanField(
        default=False
    )

    USERNAME_FIELD = 'uid'
    objects = UserManager()

    class Meta:
        db_table = 'users'
        ordering = ['joined']

    def __str__(self):
        return self.uid
