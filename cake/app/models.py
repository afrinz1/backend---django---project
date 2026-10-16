from django.db import models

# Create your models here.

# class CategoryChoices(models.TextChoices):

#     BIRTHDAY_CAKE = "birthday cake","birthday cake"
#     WEDDING_CAKE = "wedding cake" , "wedding cake"

# class WeightChoices(models.TextChoices):

#     HALF_KG = "0.5kg",'0.5kg'    
#     ONE_KG = "1kg",'1kg'
#     TWO_KG = "2kg",'2kg'

# class ShapeChoices(models.TextChoices):

#     RECTANGLE = "rectangle",'rectangle'
#     CIRCLE = "circle",'circle'

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):

        return self.name

    class Meta:

        verbose_name_plural = "categories"

class Weight(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):

        return self.name

    class Meta:

        verbose_name_plural = "weights"

class Shape(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):

        return self.name

    class Meta:

        verbose_name_plural = "shapes"


class Cake(models.Model):

    name = models.CharField(max_length=20)

    description = models.TextField()

    photo = models.ImageField(upload_to='cake-images')

    category = models.ForeignKey("Category",on_delete = models.CASCADE)   #models.Cascade can be used to delte the field when delted

    weight = models.ForeignKey("Weight",on_delete = models.CASCADE)  # this should have been many yo many but we use one to many beacuse if we do many to many we will need to chagne price 

    shape = models.ForeignKey("Shape",on_delete = models.CASCADE)

    price = models.FloatField()

    def __str__(self):

        return self.name

    class Meta:

        verbose_name_plural = "cake"