import re
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from user.models import User
from user.serializers import UserSerializer
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # permission_classes = [IsAccountAdminOrReadOnly]
    
    def list(self, request):
        return Response('Not allowed', status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        return Response('Not allowed', status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        return Response('Not allowed, please use PATCH method', status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        try:
            player = User.objects.filter(pk=pk, token=request.headers["Token"]).first()
            serializer = UserSerializer(player, data = request.data, partial=True)

            if not serializer.is_valid():
                return Response({"message": "Data is not valid"})
            
            serializer.save()
            data = serializer.data
            data['password'] = 'Anonymous'
            return Response({"message": "Data was updated successfully", "data": data})
        except Exception as e:
            return Response({"message": "Without credentials", "error": str(e)})

    def destroy(self, request, pk=None):
        try:
            player = User.objects.filter(pk=pk, token=request.headers["Token"]).first()

            player.delete()
            return Response({"message": "Data was deleted successfully"})
        except Exception as e:
            return Response({"message": "Without credentials", "error": str(e)})

@api_view(['GET', 'POST'])
def login(request):
    # If the method is not POST
    if request.method != 'POST':
        return Response({"message": "Please use POST method"})

    #If method is POST continue...
    try:
        print(request.data)
        player = User.objects.get(email=request.data["email"])
        matchThePasswords = check_password(request.data["password"], player.password)

        if not matchThePasswords:
            return Response({"message": "Invalid User", "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserSerializer(player).data
        serializer['password'] = 'Anonymous'
        
        return Response({"player": f"{serializer}", "message": "Login sucessfully", "error": ''})
    except Exception as e:
        return Response({"message": "User or password incorrect", "error": str(e)})
