from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Profile(models.Model):
    """
    This class represents a profile.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='+')
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
