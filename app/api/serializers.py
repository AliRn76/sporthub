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
    picture = serializers.SerializerMethodField('get_club_picture')
    class Meta:
        model = Club
        fields = ['clubname', 'location', 'scores', 'picture']

    def get_club_picture(self, obj):
        picture_obj = Clubpictures.objects.filter(clubid=obj.id).last()
        if picture_obj:
            picture = picture_obj.picture.url
        else:
            # set default image directory , age aks nadasht
            picture = "/media/images/default.png"
        return picture



class ClubSerializer(serializers.ModelSerializer):
    pictures = serializers.SerializerMethodField('get_club_pictures')
    class Meta:
        model = Club
        fields = ['clubname', 'clubphonenumber', 'address', 'scores',
                  'parking', 'wc', 'shower', 'absardkon', 'tahviehava', 'rakhtkan', 'boofe', 'pictures']

    def get_club_pictures(self, obj):
        pictures_obj = Clubpictures.objects.filter(clubid=obj.id)
        if pictures_obj:
            pictures = []
            for pic in pictures_obj:
                pictures.append(pic.picture.url)

        else:
            pictures = "/media/images/default.png"

        return pictures



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