from django.db import models
from django.contrib.auth.models import User,Group
from django.utils.timezone import now
# Create your models here.

# class UserProfile(models.Model):
#     UserProfile_id =  models.AutoField(primary_key=True)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     phone = models.CharField(max_length=255,null=True)
#     codename = models.CharField(max_length=255,null=True)
#     codeno = models.CharField(max_length=255,null=True)
#     bdate = models.DateField(null=True)
#     User_type = models.ForeignKey(Group, on_delete=models.CASCADE,null=True)
#     # Add other fields as needed
#     def __str__(self):
#         return self.codename
class UserProfile(models.Model):
    UserProfile_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    User_type = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50, choices=[
        ('mr', 'Mr.'),
        ('mrs', 'Mrs.'),
        ('ms', 'Ms.'),
        ('dr', 'Dr.'),
        ('prof', 'Prof.')
    ], null=True, blank=True)
    phone = models.CharField(max_length=20, null=False, blank=False)
    fax = models.CharField(max_length=20, null=True, blank=True)
    research_field = models.CharField(max_length=255, null=True, blank=True)  # This field assumes free text, modify if using a foreign key
    institution = models.CharField(max_length=255, null=False, blank=False)
    address = models.TextField(null=False, blank=False)
    city = models.CharField(max_length=255, null=False, blank=False)
    country = models.CharField(max_length=255, null=False, blank=False)
    state_province = models.CharField(max_length=255, null=False, blank=False)
    zip_postal_code = models.CharField(max_length=20, null=False, blank=False)
    codename = models.CharField(max_length=255, null=True, blank=True)
    codeno = models.CharField(max_length=255, null=True, blank=True)
    bdate = models.DateField(null=True, blank=True)
    paymet_status = models.BooleanField(null=True,default=False)
    student_info = models.FileField(upload_to='Review_file/',null=True)  # Adjust the upload_to parameter as needed
class StateReview(models.Model):
    StateReview_id =  models.AutoField(primary_key=True)
    StateReview_name = models.CharField(max_length=255)
    StateReview_open = models.DateField(null=True)
    Is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=now)
    step = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.StateReview_name
class StateReview_User(models.Model):
    StateReview_User_id =  models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    StateReview = models.ForeignKey(StateReview, on_delete=models.CASCADE)
    Review_status = models.BooleanField(null=True,default=False)
    created_at = models.DateTimeField(default=now)
    def __str__(self):
        return f"{self.user.first_name} : {self.StateReview.StateReview_name}"
class Review_User_History(models.Model):
    Review_User_History_id = models.AutoField(primary_key=True)
    StateReview_User = models.ForeignKey('StateReview_User', on_delete=models.CASCADE)  # Adjust the model name if necessary
    Submition_title = models.CharField(max_length=255)
    status_review = models.BooleanField(null=True)
    comment = models.CharField(max_length=255, null=True)
    file = models.FileField(upload_to='Review_file/',null=True)  # Adjust the upload_to parameter as needed
    created_at = models.DateTimeField(default=now)
    Submission_Code = models.CharField(max_length=55,null=True,default=False)
    def __str__(self):
        return f"{self.Submission_Code}"