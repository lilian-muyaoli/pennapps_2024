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

    # Personal Info Fields
    SCHOOL_CHOICES = [
        ('School1', 'College'),
        ('School2', 'High School'),
        # Add more schools as needed
    ]
    YEAR_CHOICES = [
        ('9', '9th Grade'),
        ('10', '10th Grade'),
        ('11', '11th Grade'),
        ('12', '12th Grade'),
    ]
    school = models.CharField(max_length=100, choices=SCHOOL_CHOICES)
    year = models.CharField(max_length=2, choices=YEAR_CHOICES)
    major = models.CharField(max_length=100, blank=True) 
    phone_number = models.CharField(max_length=15) 
    birthday = models.DateField()

    short_answer_1 = models.TextField(max_length=150)
    short_answer_2 = models.TextField(max_length=150)

    first_hackathon = models.BooleanField()

    team_member_1 = models.EmailField(blank=True, null=True)
    team_member_2 = models.EmailField(blank=True, null=True)
    team_member_3 = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.applicant.username}'s Application"
    member1 = models.EmailField(blank=True, null=True)
    member2 = models.EmailField(blank=True, null=True)
    member3 = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.applicant.username}'s Application"
    
