
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import render
from django.utils.datetime_safe import datetime
from django.contrib.auth.models import User

from app.api.serializers import SignupSerializer, ShowAllClubSerializer, ShowClubPicturesSerializer, ClubSerializer, \
    CommentsSerializer

from app.models import Club, Clubpictures, Comments, Client




def main_view(request):
    return render(request, "main.html", {})



@api_view(['POST', ])
@permission_classes((AllowAny,))
def signup_view(request):
    if request.method == "POST":
        serializer = SignupSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            # Create User
            user = User.objects.create(username=serializer.data.get("username"), is_staff=True)
            user.set_password(serializer.data.get("password"))
            user.save()

            # Create Client
            # Age , TeamName = Null
            client = Client.objects.create(userid=user)
            client.datecreated = datetime.now()
            client.save()

            # Take Token And Make Response Data
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
        paginator = PageNumberPagination()
        paginator.page_size = 1
        clubs = Club.objects.all()

        if clubs:
            result_page = paginator.paginate_queryset(clubs, request)
            serializer = ShowAllClubSerializer(result_page, many=True)

            return paginator.get_paginated_response(serializer.data)

        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def club_view(request):
    if request.method == 'GET':
        # be in function bayad {"clubname":"SOME NAME"} pas dade beshe
        club_name = request.data.get("clubname")
        if club_name is None:
            return Response({"response": "error, unexpected request"}, status=status.HTTP_417_EXPECTATION_FAILED)

        try:
            club = Club.objects.get(clubname=club_name)
            if club:
                serializer = ClubSerializer(club)

        except Club.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(serializer.data)


@api_view(['POST', ])
def forgot_password_view(request):
    if request.method == "POST":
        pass




# Chon hanuz nmidonm ba email bashe ya phone number , pas felan nmizanm

# Show_all_club() ro bar asase Paginations Besazam

# object.datetime     = datetime.now()   Baraye save time

# ye function ke harvaght kaC score dad , scores ro miangin bgire

# bayad too show_all_clubs_view() set konm bejaye avalin picture , akharin ro begire

# tedad comment ha va picture ha ro mitonm tooye json avali ezafe konm, age Amin bekhad

# sort bar asase location kar dare , nmidonm raveshe asoonesh chie