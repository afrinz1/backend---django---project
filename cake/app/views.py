from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from . models import Cake,Category,Shape,Weight

from .serializers import CakeSerializer,CategorySerializer,ShapeSerializer,WeightSerializer

from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly

from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

from django.contrib.auth.models import User
# Create your views here.


class CakeCreateListView(APIView):
    authentication_classes = [TokenAuthentication]

    # permission_classes = [IsAdminUser]

    # def get_permissions(self):

    #     permissions = [] 
    #     if self.request.method == 'POST':   #TO CHECK IF THE REQUEST METHOD IS POST OR NOT, will only work when post method is used

    #         permissions = [IsAdminUser]

    #     return [permission()for permission in permissions]

    # serializer_cake = CakeSerializer



    def get(self,request,*args,**kwargs):

        cakes = Cake.objects.all()
        # serializer = self.serializer_cake(cakes,many=True)
        serializer = CakeSerializer(cakes,many=True)  #noramlly serializer will convert only one object so may is used to convert multiple objects
        

        return Response(serializer.data,status=200)

    def post(self,request,*args,**kwargs):

        # serializer = self.serializer_cake(data=request.data)
        serializer = CakeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            data = {'msg' : 'cake created succesfully'}

            return Response(data,status=201)

        return Response(serializer.errors,status=400)


class CakeRetriveUpdateDestroyView(APIView):

    serializer_class = CakeSerializer

    def get(self,request,*args,**kwargs):
        id = kwargs.get('id')
        cake = Cake.objects.get(id=id)

        serializer = self.serializer_class(cake)


        return Response(serializer.data,status=200)

    def patch(self,request,*args,**kwargs):

        id = kwargs.get('id')

        cake = Cake.objects.get(id=id)

        serializer = self.serializer_class(instance = cake, data = request.data, partial=True)

        if serializer.is_valid():

            serializer.save()

            data = {'msg' : 'cake updated succesfully'}

            return Response(data,status=200)

        return Response(serializer.errors,status=400)

    def delete(self,request,*args,**kwargs):

        id = kwargs.get('id')

        cake = Cake.objects.get(id=id)

        cake.delete()

        data = {'msg':'data deleted sucefully'}

        return Response(data,status=200)


class CategoryListCreateView(ListCreateAPIView):

    queryset = Category.objects.all()

    serializer_class = CategorySerializer  #doing this GET nad POST methods are done.

class CategoryRetriveUpdateDestroyView(RetrieveUpdateDestroyAPIView):

    lookup_field = 'id'
    
    queryset = Category.objects.all()

    serializer_class = CategorySerializer

# this is for shape
class ShapeListCreateView(ListCreateAPIView):

    queryset = Shape.objects.all()

    serializer_class = ShapeSerializer  #doing this GET nad POST methods are done.

class ShapeRetriveUpdateDestroyView(RetrieveUpdateDestroyAPIView):

    lookup_field = 'id'

    queryset = Shape.objects.all()

    serializer_class = ShapeSerializer


class WeightListCreateView(ListCreateAPIView):

    queryset = Weight.objects.all()

    serializer_class = WeightSerializer  #doing this GET nad POST methods are done.

class WeightRetriveUpdateDestroyView(RetrieveUpdateDestroyAPIView):

    lookup_field = 'id'

    queryset = Weight.objects.all()

    serializer_class = WeightSerializer

        

        


