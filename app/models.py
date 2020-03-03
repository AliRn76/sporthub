

from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


User = settings.AUTH_USER_MODEL


class Admin(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey(User, models.DO_NOTHING, db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    birthdate = models.DateField(db_column='BirthDate', blank=True, null=True)  # Field name made lowercase.
    fathername = models.CharField(db_column='FatherName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gender = models.IntegerField(db_column='Gender', blank=True, null=True)  # Field name made lowercase.
    nationalcode = models.CharField(db_column='NationalCode', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Admin'


class Client(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey(User, models.DO_NOTHING, db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    teamname = models.CharField(db_column='TeamName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Client'


class Club(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    clubownerid = models.ForeignKey('Clubowner', models.DO_NOTHING, db_column='ClubOwnerID', blank=True, null=True)  # Field name made lowercase.
    adminid_acceptedby = models.ForeignKey(Admin, models.DO_NOTHING, db_column='AdminID_AcceptedBy', blank=True, null=True)  # Field name made lowercase.
    clubname = models.CharField(db_column='ClubName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    clubphonenumber = models.CharField(db_column='ClubPhoneNumber', max_length=11, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=200, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=50, blank=True, null=True)  # Field name made lowercase.
    scores = models.IntegerField(db_column='Scores', blank=True, null=True)  # Field name made lowercase.
    parking = models.IntegerField(db_column='Parking', blank=True, null=True)  # Field name made lowercase.
    wc = models.IntegerField(db_column='WC', blank=True, null=True)  # Field name made lowercase.
    shower = models.IntegerField(db_column='Shower', blank=True, null=True)  # Field name made lowercase.
    absardkon = models.IntegerField(db_column='AbSardKon', blank=True, null=True)  # Field name made lowercase.
    tahviehava = models.IntegerField(db_column='TahvieHava', blank=True, null=True)  # Field name made lowercase.
    rakhtkan = models.IntegerField(db_column='RakhtKan', blank=True, null=True)  # Field name made lowercase.
    boofe = models.IntegerField(db_column='Boofe', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Club'


class Clubowner(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey(User, models.DO_NOTHING, db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    nationalcode = models.CharField(db_column='NationalCode', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'ClubOwner'


class Clubpictures(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    clubid = models.ForeignKey(Club, models.DO_NOTHING, db_column='ClubID', blank=True, null=True)  # Field name made lowercase.
    picture = models.ImageField(db_column='Picture', upload_to='images/', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dateadded = models.DateTimeField(db_column='DateAdded', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'ClubPictures'


class Clubsans(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    clubid = models.ForeignKey(Club, models.DO_NOTHING, db_column='ClubID', blank=True, null=True)  # Field name made lowercase.
    fromtime = models.TimeField(db_column='FromTime', blank=True, null=True)  # Field name made lowercase.
    tilltime = models.TimeField(db_column='TillTime', blank=True, null=True)  # Field name made lowercase.
    capacity = models.IntegerField(db_column='Capacity', blank=True, null=True)  # Field name made lowercase.
    cost = models.IntegerField(db_column='Cost', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'ClubSans'


class Clubscore(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    clubid = models.ForeignKey(Club, models.DO_NOTHING, db_column='ClubID', blank=True, null=True)  # Field name made lowercase.
    clientid = models.ForeignKey(Client, models.DO_NOTHING, db_column='ClientID', blank=True, null=True)  # Field name made lowercase.
    score = models.IntegerField(db_column='Score', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'ClubScore'


class Commentscores(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    commentsid = models.ForeignKey('Comments', models.DO_NOTHING, db_column='CommentsID', blank=True, null=True)  # Field name made lowercase.
    clientid = models.ForeignKey(Client, models.DO_NOTHING, db_column='ClientID', blank=True, null=True)  # Field name made lowercase.
    score = models.IntegerField(db_column='Score', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'CommentScores'


class Comments(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    clubid = models.ForeignKey(Club, models.DO_NOTHING, db_column='ClubID', blank=True, null=True)  # Field name made lowercase.
    text = models.CharField(db_column='Text', max_length=200, blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey(User, models.DO_NOTHING, db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    commentsid = models.ForeignKey('self', models.DO_NOTHING, db_column='CommentsID', blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    scores = models.IntegerField(db_column='Scores', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Comments'


class Rent(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    clientid = models.ForeignKey(Client, models.DO_NOTHING, db_column='ClientID', blank=True, null=True)  # Field name made lowercase.
    clubsansid = models.ForeignKey(Clubsans, models.DO_NOTHING, db_column='ClubSansID', blank=True, null=True)  # Field name made lowercase.
    teamname = models.CharField(db_column='TeamName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    number = models.IntegerField(db_column='Number', blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Rent'




@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)