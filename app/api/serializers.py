from django.contrib.auth.models import User

from rest_framework import serializers

from app.models import Club, Clubpictures, Comments


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

class ShowClubPicturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clubpictures
        fields = ['picture']

class ShowAllClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['clubname', 'location', 'scores']


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['clubname', 'clubphonenumber', 'address', 'scores',
                  'parking', 'wc', 'shower', 'absardkon', 'tahviehava', 'rakhtkan', 'boofe']


class CommentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class CommentsSerializer(serializers.ModelSerializer):
    userid = CommentUserSerializer()
    class Meta:
        model = Comments
        fields = ['text', 'date', 'scores', 'userid']


# class ForgotPasswordSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['password']
#
# Chon hanuz nmidonm ba email bashe ya phone number , pas felan nmizanm