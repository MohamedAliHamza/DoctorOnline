from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    
    def _create_user(self, email, password, **extra_fields):
        user = self.model(
            email=self.normalize_email(email), 
            **extra_fields,
            )
        user.set_password(password)        
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True) 
        return self._create_user(email, password, **extra_fields)