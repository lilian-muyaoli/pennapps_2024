from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class Applicant(AbstractUser):
    is_penn_student = models.BooleanField(default=False)

class Application(models.Model):
    STATUS_CHOICES = [
        ("ACPT", "Accepted"),
        ("RJCT", "Rejected"),
        ("WLST", "Waitlisted"),
        ("PROC", "Processing"),
    ]

    applicant = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    status = models.CharField(max_length=4, choices=STATUS_CHOICES, default="STRT")

    project_title = models.CharField(max_length=100)
    project_description = models.TextField()
    skills = models.CharField(max_length=200)
    previous_experience = models.TextField()

    
    member1 = models.EmailField(blank=True, null=True)
    member2 = models.EmailField(blank=True, null=True)
    member3 = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.applicant.username}'s Application"
    
