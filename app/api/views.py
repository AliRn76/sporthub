
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from django.utils.datetime_safe import datetime
from django.contrib.auth.models import User
from app.api.serializers import SignupSerializer, ShowAllClubSerializer, ShowClubPicturesSerializer, ClubSerializer, \
    CommentsSerializer

from app.models import Club, Clubpictures, Comments, Client


@api_view(['POST', ])
@permission_classes((AllowAny,))
def signup_view(request):
    if request.method == "POST":
        serializer = SignupSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = User.objects.create(username=serializer.data.get("username"), is_staff=True)
            user.set_password(serializer.data.get("password"))
            user.save()

            client = Client.objects.create(userid=user, age=10)
            client.datecreated = datetime.now()
            client.save()

            token = Token.objects.get(user=user).key
            data["response"]    = "successfully registered a new user and new client"
            data['user']        = serializer.data.get("username")
            data['date']        = client.datecreated
            # data['pass']      = serializer.data.get("password")
            data['token']       = token

        else:
            data = serializer.errors

        return Response(data)



@api_view(["GET", ])
@permission_classes((IsAuthenticated, ))
def show_all_clubs_view(request):
    if request.method == "GET":
        clubs = Club.objects.all()
        if clubs:
            result = []
            for club in clubs:
                pictures = Clubpictures.objects.filter(clubid=club.id)
                serializer1 = ShowAllClubSerializer(club)
                serializer = serializer1.data
                if pictures:
                    serializer2 = ShowClubPicturesSerializer(pictures[0])
                    picture_ser = serializer2.data

                else:
                    # set default image directory , age aks nadasht
                    picture_ser = {"picture": "/media/images/Screenshot_from_2020-02-23_02-44-59.png"}

                # image_dict ro be serializer add kard
                serializer.update(picture_ser)
                result.append(serializer)

            return Response(result, status=status.HTTP_200_OK)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def club_view(request):
    if request.method == 'GET':
        # be in function bayad {"clubname":"SOME NAME"} pas dade beshe
        club_name = request.data.get("clubname")
        print(club_name)
        if club_name is None:
            return Response({"response": "error, unexpected request"}, status=status.HTTP_417_EXPECTATION_FAILED)

        try:
            club = Club.objects.get(clubname=club_name)
            if club:
                serializer = []
                club_ser = ClubSerializer(club).data
                club_id = Club.objects.get(clubname=club_name).id
                serializer.append(club_ser)
                # Picture
                pictures = Clubpictures.objects.filter(clubid=club_id)
                if pictures:
                    pictures_ser = ShowClubPicturesSerializer(pictures, many=True).data
                    for picture in pictures_ser:
                        serializer.append(picture)

                else:
                    # set default image directory , age aks nadasht
                    pictures_ser = {"picture": "/media/images/Screenshot_from_2020-02-23_02-44-59.png"}
                    serializer.append(pictures_ser)
                # End Picture

                comments = Comments.objects.filter(clubid=club_id)
                if comments:
                    comments_ser = CommentsSerializer(comments, many=True).data
                    for comment in comments_ser:
                        serializer.append(comment)

        except Club.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(serializer)


@api_view(['POST', ])
def forgot_password_view(request):
    if request.method == "POST":
        pass
# Chon hanuz nmidonm ba email bashe ya phone number , pas felan nmizanm




# object.datetime     = datetime.now()   Baraye save time

# ye function ke harvaght kaC score dad , scores ro miangin bgire

# bayad too show_all_clubs_view() set konm bejaye avalin picture , akharin ro begire

# tedad comment ha va picture ha ro mitonm tooye json avali ezafe konm, age Amin bekhad

# sort bar asase location kar dare , nmidonm raveshe asoonesh chie