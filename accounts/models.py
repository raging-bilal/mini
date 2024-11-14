from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

# Custom user manager
class BaseUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

# BaseUser class
class BaseUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='baseuser_set',
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups"
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='baseuser_permissions',
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions"
    )

    objects = BaseUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        # If password is set and not already hashed, hash it
        # if self.password and not self.password.startswith(('pbkdf2_sha256$', 'argon2$')):
            # self.set_password(self.password)  # Hash the password
        super().save(*args, **kwargs)  # Call the real save method

    def __str__(self):
        return self.email


# Admin class inheriting from BaseUser
class Admin(BaseUser):
    name = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = 'Admin'
        verbose_name_plural = 'Admins'

    def save(self, *args, **kwargs):
        self.is_staff = True
        self.is_superuser = True
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Admin: {self.name} ({self.email})"

# GymOwner class
class WebUser(BaseUser):
    name = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=10, null= True)
    address = models.CharField(max_length=255,blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"User: {self.name} - {self.email}"

# Trainer class
class PanelAdmin(BaseUser):

    name = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=10, null= True)
    address = models.CharField(max_length=255,blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Trainer: {self.name} - {self.email}"

