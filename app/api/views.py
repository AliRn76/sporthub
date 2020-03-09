
from django.shortcuts import render
from django.contrib.auth.models import User
from django.utils.datetime_safe import datetime

from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes

from app.api.serializers import (
    SignupSerializer,
    ShowAllClubSerializer,
    ClubSerializer,
    ClubSansSerializer
)

from app.models import (
    Club,
    Client,
    Clubsans,
    Comments
)




def main_view(request):
    return render(request, "main.html", {})



@api_view(['POST', ])
@permission_classes((AllowAny,))
def signup_view(request):
    if request.method == "POST":
        data = {}

        # Collecting Data
        serializer = SignupSerializer(data=request.data)

        if serializer.is_valid():
            # Create User
            user = User.objects.create(username=serializer.data.get("username"), is_staff=True)
            user.set_password(serializer.data.get("password"))
            user.save()

            # Create Client
            # Age & Teamname = Null
            client = Client.objects.create(userid=user)
            client.datecreated = datetime.now()
            client.save()

            # Take Token And Create data For Response
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

        # Set Pagination
        paginator = PageNumberPagination()
        paginator.page_size = 6

        # Take All clubs
        clubs = Club.objects.all()

        # Serialize clubs If We Have
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
def show_club_view(request):
    if request.method == 'GET':
        data = {}

        # Collecting Data
        club_name = request.data.get("clubname")

        try:
            club = Club.objects.get(clubname=club_name)

        except Club.DoesNotExist:
            data['response']    = 'clubname is invalid'
            return Response(data, status=status.HTTP_404_NOT_FOUND)

        # Serialize club If We Have
        if club:
            serializer = ClubSerializer(club)

    return Response(serializer.data)




@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def show_club_sans(request):
    if request.method == "GET":
        data = {}
        # Collecting Data
        club_name = request.data.get("clubname")

        # Take club_id From club_name
        try:
            club_id = Club.objects.get(clubname=club_name).id
        except Club.DoesNotExist:
            data['response'] = "clubname is not valid"
            return Response(data, status=status.HTTP_404_NOT_FOUND)

        # Take sans From club_id
        sans = Clubsans.objects.filter(clubid=club_id)

        # Serialize sans If We Have
        if sans:
            serializer = ClubSansSerializer(sans, many=True)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(serializer.data)





@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
def send_comment_view(request):
    if request.method == "POST":
        data = {}

        # Collecting Data
        user = request.user
        club_name = request.data.get("clubname")
        text = request.data.get("text")

        # Check Text And Make It Correct
        text = " ".join(text.split())
        temp_text = text.replace(' ', '')
        if temp_text is None or temp_text == '':
            data['response']    = "text is not valid"
            return Response(data)

        # Take club From club_name
        try:
            club = Club.objects.get(clubname=club_name)
        except Club.DoesNotExist:
            data['response']    = "clubname is not valid"
            return Response(data, status=status.HTTP_404_NOT_FOUND)

        # Create Comment Object
        comment = Comments.objects.create(clubid=club, text=text, userid=user)
        comment.date = datetime.now()
        comment.save()

        # Create data For Response
        data['response']    = "successfully comment added"
        data['username']    = request.user.username
        data['clubname']    = club_name
        data['text']        = text
        data['date']        = comment.date


        return Response(data)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)






@api_view(['POST', ])
@permission_classes((AllowAny,))
def check_username_view(request):
    if request.method == "POST":
        data = {}

        # Collecting Data
        username = request.data.get('username')

        if username:
            user = User.objects.filter(username=username)

            if user:
                data['response']    = 'username is taken'
                return Response(data, status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                data['response'] = 'username is free'
                return Response(data, status=status.HTTP_200_OK)

        else:
            data['response'] = 'username is not valid'
            return Response(status=status.HTTP_404_NOT_FOUND)


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