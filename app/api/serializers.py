from django.contrib.auth.models import User

from rest_framework import serializers

from app.models import Club, Clubpictures


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

class ShowClubPictures(serializers.ModelSerializer):
    class Meta:
        model = Clubpictures
        fields = ['picture']

class ShowAllClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['clubname', 'location', 'scores']