from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, brandname, password, **extra_fields):
        values = [email, brandname]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
        for field_brandname, value in field_value_map.items():
            if not value:
                raise ValueError('The {} value must be set'.format(field_brandname))

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            brandname=brandname,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, brandname, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, brandname, password, **extra_fields)

    def create_superuser(self, email, brandname, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, brandname, password, **extra_fields)



class User(AbstractBaseUser, PermissionsMixin):
    brandname = models.CharField(max_length=150, unique=True)
    email = models.EmailField(blank=True, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = "brandname"
    REQUIRED_FIELDS = ['email']


    def __str__(self):
        return self.brandname


    class Meta:
        ordering = ['date_joined']
