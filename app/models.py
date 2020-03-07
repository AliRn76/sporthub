

from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token



User = settings.AUTH_USER_MODEL

class Admin(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    userid = models.ForeignKey(User, models.DO_NOTHING, db_column='UserID', blank=True, null=True)
    birthdate = models.DateField(db_column='BirthDate', blank=True, null=True)
    fathername = models.CharField(db_column='FatherName', max_length=50, blank=True, null=True)
    gender = models.IntegerField(db_column='Gender', blank=True, null=True)
    nationalcode = models.CharField(db_column='NationalCode', max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'Admin'


class Client(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    userid = models.ForeignKey(User, models.DO_NOTHING, db_column='UserID', blank=True, null=True)
    teamname = models.CharField(db_column='TeamName', max_length=50, blank=True, null=True)
    age = models.IntegerField(db_column='Age', blank=True, null=True)
    datecreated = models.DateTimeField(db_column='Date', blank=True, null=True)

    class Meta:
        db_table = 'Client'


class Club(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    clubownerid = models.ForeignKey('Clubowner', models.DO_NOTHING, db_column='ClubOwnerID', blank=True, null=True)
    adminid_accdeptedby = models.ForeignKey(Admin, models.DO_NOTHING, db_column='AdminID_AcceptedBy', blank=True, null=True)
    clubname = models.CharField(db_column='ClubName', max_length=50, blank=True, null=True)
    clubphonenumber = models.CharField(db_column='ClubPhoneNumber', max_length=11, blank=True, null=True)
    address = models.CharField(db_column='Address', max_length=200, blank=True, null=True)
    location = models.CharField(db_column='Location', max_length=50, blank=True, null=True)
    scores = models.IntegerField(db_column='Scores', blank=True, null=True)
    parking = models.BooleanField(db_column='Parking', blank=True, null=True)
    wc = models.BooleanField(db_column='WC', blank=True, null=True)
    shower = models.BooleanField(db_column='Shower', blank=True, null=True)
    absardkon = models.BooleanField(db_column='AbSardKon', blank=True, null=True)
    tahviehava = models.BooleanField(db_column='TahvieHava', blank=True, null=True)
    rakhtkan = models.BooleanField(db_column='RakhtKan', blank=True, null=True)
    boofe = models.BooleanField(db_column='Boofe', blank=True, null=True)

    class Meta:
        db_table = 'Club'


class Clubowner(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    userid = models.ForeignKey(User, models.DO_NOTHING, db_column='UserID', blank=True, null=True)
    nationalcode = models.CharField(db_column='NationalCode', max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'ClubOwner'


class Clubpictures(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    clubid = models.ForeignKey(Club, models.DO_NOTHING, db_column='ClubID')
    picture = models.ImageField(db_column='Picture', upload_to='images/', max_length=255)
    dateadded = models.DateTimeField(db_column='DateAdded', blank=True, null=True)

    class Meta:
        db_table = 'ClubPictures'


class Clubsans(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    clubid = models.ForeignKey(Club, models.DO_NOTHING, db_column='ClubID', blank=True, null=True)
    fromtime = models.TimeField(db_column='FromTime', blank=True, null=True)
    tilltime = models.TimeField(db_column='TillTime', blank=True, null=True)
    capacity = models.IntegerField(db_column='Capacity', blank=True, null=True)
    cost = models.IntegerField(db_column='Cost', blank=True, null=True)

    class Meta:
        db_table = 'ClubSans'


class Clubscore(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    clubid = models.ForeignKey(Club, models.DO_NOTHING, db_column='ClubID', blank=True, null=True)
    clientid = models.ForeignKey(Client, models.DO_NOTHING, db_column='ClientID', blank=True, null=True)
    score = models.IntegerField(db_column='Score', blank=True, null=True)

    class Meta:
        db_table = 'ClubScore'


class Commentscores(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    commentsid = models.ForeignKey('Comments', models.DO_NOTHING, db_column='CommentsID', blank=True, null=True)
    clientid = models.ForeignKey(Client, models.DO_NOTHING, db_column='ClientID', blank=True, null=True)
    score = models.IntegerField(db_column='Score', blank=True, null=True)

    class Meta:
        db_table = 'CommentScores'


class Comments(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    clubid = models.ForeignKey(Club, models.DO_NOTHING, db_column='ClubID', blank=True, null=True)
    text = models.CharField(db_column='Text', max_length=200, blank=True, null=True)
    userid = models.ForeignKey(User, models.DO_NOTHING, db_column='UserID', blank=True, null=True)
    commentsid = models.ForeignKey('self', models.DO_NOTHING, db_column='CommentsID', blank=True, null=True)
    date = models.DateTimeField(db_column='Date', blank=True, null=True)
    scores = models.IntegerField(db_column='Scores', blank=True, null=True)

    class Meta:
        db_table = 'Comments'


class Rent(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    clientid = models.ForeignKey(Client, models.DO_NOTHING, db_column='ClientID', blank=True, null=True)
    clubsansid = models.ForeignKey(Clubsans, models.DO_NOTHING, db_column='ClubSansID', blank=True, null=True)
    teamname = models.CharField(db_column='TeamName', max_length=50, blank=True, null=True)
    number = models.IntegerField(db_column='Number', blank=True, null=True)
    date = models.DateTimeField(db_column='Date', blank=True, null=True)

    class Meta:
        db_table = 'Rent'




@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)