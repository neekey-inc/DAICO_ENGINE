from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, _user_has_perm
)
from django.core import validators
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
# from django.utils.translation import ugettext_lazy as _

# class UserManager(BaseUserManager):
#     def _create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('Users must have a email address')
#         email = UserManager.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_user(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(email, password, **extra_fields)

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)        
#         return self._create_user(email, password, **extra_fields)

# class User(AbstractBaseUser, PermissionsMixin):
#     type_choices = {
#         ('A', 'Client User'),
#         ('B', 'Customer User')
#     }
#     user_type = models.CharField(
#         max_length=1,
#         choices=type_choices,
#         default='B'
#     )

#     email = models.EmailField(max_length=128, unique=True)
#     name = models.CharField(max_length=150, blank=True, unique=True,)
#     sex_choices = {
#         ('A', '男性'),
#         ('B', '女性'),
#         ('C', 'その他')
#     }
#     sex = models.CharField(
#         max_length=1,
#         choices=sex_choices,
#         default=None,
#         null=True
#     )
#     birth_year = models.IntegerField(
#         max_length=4,
#         default=None,
#         null=True
#     )
#     birth_month = models.IntegerField(
#         max_length=2,
#         default=None,
#         null=True
#     )
#     birth_day = models.IntegerField(
#         max_length=2,
#         default=None,
#         null=True
#     )
#     address = models.CharField(
#         max_length=300,
#         default=None,
#         null=True
#     )
#     phone = models.TextField(
#         max_length=12,
#         default=None,
#         null=True
#     )
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)

#     USERNAME_FIELD = 'email'

#     objects = UserManager()
#     class Meta:
#         db_table = 'user'
#         swappable = 'AUTH_USER_MODEL'


class UserManager(BaseUserManager):
    def create_user(self, request_data, **kwargs):
        now = timezone.now()
        if not request_data['email']:
            raise ValueError('Users must have an email address.')

        if request_data.get('profile'):
            profile = request_data['profile']
        else:
            profile = ""

        user = self.model(
            username=request_data['username'],
            email=self.normalize_email(request_data['email']),
            is_active=True,
            last_login=now,
            date_joined=now,
            profile=profile
        )

        user.set_password(request_data['password'])
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        request_data = {
            'username': username,
            'email': email,
            'password': password
        }
        user = self.create_user(request_data)
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        # user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username    = models.CharField(_('username'), max_length=30, unique=True)
    first_name  = models.CharField(_('first name'), max_length=30, blank=True)
    last_name   = models.CharField(_('last name'), max_length=30, blank=True)
    email       = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    profile     = models.CharField(_('profile'), max_length=255, blank=True)
    is_active   = models.BooleanField(default=True)
    is_staff    = models.BooleanField(default=False)
    is_admin    = models.BooleanField(default=False)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def user_has_perm(user, perm, obj):
        return _user_has_perm(user, perm, obj)

    def has_perm(self, perm, obj=None):
        return _user_has_perm(self, perm, obj=obj)

    def has_module_perms(self, app_label):
        return self.is_admin

    def get_short_name(self):
        return self.first_name

    @property
    def is_superuser(self):
        return self.is_admin

    class Meta:
        db_table = 'user'
        swappable = 'AUTH_USER_MODEL'