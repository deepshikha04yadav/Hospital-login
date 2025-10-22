# from django.db import models
# from django.contrib.auth.models import AbstractUser

# USER_TYPE = (
#     ('patient', 'Patient'),
#     ('doctor', 'Doctor'),
# )

# class User(AbstractUser):
#     user_type = models.CharField(max_length=10, choices=USER_TYPE)
#     profile_picture = models.ImageField(upload_to="profiles/", blank=True, null=True)
#     address_line1 = models.CharField(max_length=255)
#     city = models.CharField(max_length=50)
#     state = models.CharField(max_length=50)
#     pincode = models.CharField(max_length=10)


#     def __str__(self):
#         return self.username
from django.db import models
from django.contrib.auth.models import AbstractUser

USER_TYPE = (
    ('patient', 'Patient'),
    ('doctor', 'Doctor'),
)

class User(AbstractUser):
    user_type = models.CharField(max_length=10, choices=USER_TYPE)
    profile_pic = models.ImageField(upload_to='profiles/', null=True, blank=True)
    address_line1 = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)

    def __str__(self):
        return self.username
