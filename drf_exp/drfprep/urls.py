from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk>',views.f1,name='all_apis'),
    path('',views.f1,name='all_apis'),
    path('create',views.f1,name='all_apis'),

    # class based view

    path('classdetail/<int:pk>',views.ProductDetailAPI.as_view()),
    path('classlist',views.ProductListApi.as_view()),
    path('classcreate',views.ProductCreateAPI.as_view()),
    path('classupdate/<int:pk>',views.ProductUpdateAPI.as_view()),
    path('classdelete/<int:pk>',views.ProductDeleteAPI.as_view()),

    # F expressions
    path('fupdate',views.price_update),
    # union
    path('union',views.checking_union),

]