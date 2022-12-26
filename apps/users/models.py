from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.db import models
from apps.states.models import *
from apps.locations.models import *
from django.dispatch import receiver
from django.db.models.signals import post_save,pre_save
from django.forms.models import model_to_dict
from django.utils import timezone

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
    leader = models.ForeignKey(Leader, on_delete=models.CASCADE)
    date_changed = models.DateTimeField(auto_now_add=True)
    data = models.TextField(blank = True)
    type_log = models.ForeignKey(Type_Log, on_delete=models.CASCADE)


def dataService(key,voter,instance,dato_new,dato_old):
	data = ""
	new = ""
	old = ""
	if str(key) == "document_type":
		if instance.document_type != None:
			new = instance.document_type.name
		if voter.document_type != None:
			old = voter.document_type.name
	elif str(key) == "state":
		if instance.state != None:
			new = instance.state.name
		if voter.state != None:
			old = voter.state.name
	elif str(key) == "leader":
		if instance.leader != None:
			new = str(instance.leader.user.id) +" - " + str(instance.leader.user.first_name) + " " + str(instance.leader.user.last_name)
		if voter.leader != None:
			old = str(voter.leader.user.id) +" - " + str(voter.leader.user.first_name) + " " + str(voter.leader.user.last_name)
	elif str(key) == "polling_place":
		if instance.polling_place != None:
			new = instance.polling_place.name
		if voter.polling_place != None:
			old = voter.polling_place.name
	else:
		new = dato_new[key]
		old = dato_old[key]

	data = {
		"new":new,
		"old":old
	}
	return data


@receiver(pre_save, sender=Voter)
def voter_before_save(sender, instance, *args, **kwargs):
    if instance.id != None:
        voter = Voter.objects.get(id = instance.id)
        list_new= model_to_dict(instance)
        list_old = model_to_dict(voter)
        dataSave = ""
        i = 0
        for key,value in list_old.items():
            if list_old[key] != list_new[key]:
                data = dataService(key,voter,instance,list_new,list_old)
                if i == 0:
                    dataSave += str(key)+"%%%"+str(data["old"])+"%%%"+str(data["new"])
                else:
                    dataSave += "#//#"+str(key)+"%%%"+str(data["old"])+"%%%"+str(data["new"])
                i += 1

        if dataSave:
            event = Type_Log.objects.get(name = "update")
            leader = Leader.objects.get(user__id = voter.leader.user.id)
            Log.objects.create(
                voter = instance,
                leader = leader,
                data = dataSave,
                type_log = event,
            )


@receiver(post_save, sender=Voter)
def create_log_for_service(sender, instance, created, **kwargs):
    if created:
        list_new= model_to_dict(instance)
        dataSave = ""
        i = 0
        for key, value in list_new.items():
            if i == 0:
                dataSave += str(key)+"%%%"+str(list_new[key])
            else:
                dataSave += "#//#"+str(key)+"%%%"+str(list_new[key])
        i += 1

        event = Type_Log.objects.get(name = "create")
        Log.objects.create(
            voter = instance,
            leader = instance.leader,
            data = dataSave,
            type_log = event,
        )