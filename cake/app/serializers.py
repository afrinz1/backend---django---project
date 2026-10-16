from rest_framework import serializers
from .models import Cake,Category,Weight,Shape

class CategorySerializer(serializers.ModelSerializer):

    class Meta:

        model = Category
        fields = '__all__'

class WeightSerializer(serializers.ModelSerializer):

    class Meta:

        model = Weight
        fields = '__all__'

class ShapeSerializer(serializers.ModelSerializer):

    class Meta:

        model = Shape
        fields = '__all__'

class CatergoryField(serializers.PrimaryKeyRelatedField):

    def get_attribute(self, instance):

        return getattr(instance,self.source_attrs[0])

    def to_representation(self, value):
        return CategorySerializer(value).data
       #this is to convert that instance (category object) into json format

class WeightField(serializers.PrimaryKeyRelatedField):

    def get_attribute(self, instance):

        return getattr(instance,self.source_attrs[0])

    def to_representation(self, value):
        return WeightSerializer(value).data

class ShapeField(serializers.PrimaryKeyRelatedField):

    def get_attribute(self, instance):

        return getattr(instance,self.source_attrs[0])

    def to_representation(self, value):
        return ShapeSerializer(value).data

class CakeSerializer(serializers.ModelSerializer):   # this is to get or extract serializer the entire data inside category weight shape

    category = CatergoryField(queryset=Category.objects.all())
    weight = WeightField(queryset=Weight.objects.all())
    shape = ShapeField(queryset=Shape.objects.all())

    flag = serializers.SerializerMethodField()

    def get_flag(self,obj):  #here obj is basically the cake object
        if obj.price < 1000 :

            return 'super save'

        return None
    class Meta:

        model = Cake

        # fields = ['id','name','photo','description']

        fields = '__all__' 

        # exclude = ['name']


# class CakeSerializer(serializers.ModelSerializer):   #this is nested serilaizer

    
#     # weight = WeightSerializer()
#     # shape = ShapeSerializer()

#     class Meta:

#         model = Cake

#         # fields = ['id','name','photo','description']

#         fields = '__all__' 

#         # exclude = ['name']

    