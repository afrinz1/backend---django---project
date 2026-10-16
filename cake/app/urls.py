from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('cake/',views.CakeCreateListView.as_view()),
    path('cake/<int:id>/',views.CakeRetriveUpdateDestroyView.as_view()),
    path('categories/',views.CategoryListCreateView.as_view()),
    path('categories/<int:id>',views.CategoryRetriveUpdateDestroyView.as_view()),

    path('shape/',views.ShapeListCreateView.as_view()),
    path('shape/<int:id>',views.ShapeRetriveUpdateDestroyView.as_view()),

    path('weight/',views.WeightListCreateView.as_view()),
    path('weight/<int:id>',views.WeightRetriveUpdateDestroyView.as_view()),


]
