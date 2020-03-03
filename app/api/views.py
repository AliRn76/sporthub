
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from app.api.serializers import RegistrationSerializer, ShowAllClubSerializer, ShowClubPictures
from rest_framework.permissions import IsAuthenticated

from app.models import *


@api_view(['POST', ])
def registration_view(request):

    if request.method == "POST":
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = User.objects.create(username=serializer.data.get("username"), is_staff=True)
            user.set_password(serializer.data.get("password"))
            user.save()


            data["response"] = "successfully registered a new user"
            data['user'] = serializer.data.get("username")
            data['pass'] = serializer.data.get("password")
            token = Token.objects.get(user=user).key
            data['token'] = token
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
                if pictures:
                    serializer1 = ShowAllClubSerializer(club)
                    serializer2 = ShowClubPictures(pictures[0])
                    serializer = serializer1.data
                    image_dict = serializer2.data

                    # image_dict ro be serializer add kard
                    serializer.update(image_dict)

                    result.append(serializer)

                else:
                    serializer1 = ShowAllClubSerializer(club)
                    serializer = serializer1.data

                    # set default image directory , age aks nadasht
                    image_dict = {"picture": "/media/images/Screenshot_from_2020-02-23_02-44-59.png"}

                    serializer.update(image_dict)
                    result.append(serializer)

            return Response(result, status=status.HTTP_200_OK)


    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)



# ye function ke harvaght kaC score dad , scores ro miangin bgire