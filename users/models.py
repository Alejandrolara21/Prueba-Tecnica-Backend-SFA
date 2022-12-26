from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.db import models
from states.models import *
from locations.models import *

class DocumentType(models.Model):
    name = models.CharField(unique=True, max_length=100)
    def __str__(self):
        return '{}'.format(self.name)

class Leader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    document_type = models.ForeignKey(DocumentType, on_delete=models.CASCADE)
    document = models.CharField(max_length=30, unique=True)
    phone = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    image = models.ImageField(upload_to = 'users', null=True)
    address = models.CharField(max_length=100)
    coordinates_lat = models.CharField(max_length=100)
    coordinates_len = models.CharField(max_length=100)
    def __str__(self):
        return '{}'.format(self.user.first_name)

class Voter(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    document_type = models.ForeignKey(DocumentType, on_delete=models.CASCADE)
    document = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=30, validators=[RegexValidator(r'^\d{1,10}$')])
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    polling_station = models.IntegerField()
    leader = models.ForeignKey(Leader, on_delete=models.CASCADE)
    polling_place = models.ForeignKey(PollingPlace, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.document)


#### LOG VOTERS

class Type_Log(models.Model):
    name = models.CharField(max_length=50)

class Log(models.Model):
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    date_changed = models.DateTimeField(auto_now_add=True)
    data = models.CharField(max_length=500, blank=True, null=True)
    type_log = models.ForeignKey(Type_Log, on_delete=models.CASCADE)
