from django.shortcuts import render
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import get_object_or_404,HttpResponse
from django.db.models import F
from django.db import transaction
from .models import Product,Store
from itertools import chain

# Create your views here.


@api_view(['GET','POST'])
def f1(request,pk=None):

    if request.method == 'GET':
        if pk is not None:
            obj = get_object_or_404(Product,pk=pk)
            serializer = ProductSerializer(obj)
            return Response(serializer.data)

        else:
            obj_list = Product.objects.all()
            serializer = ProductSerializer(obj_list,many=True)
            return Response(serializer.data)
    elif request.method == 'POST':

        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('data saved')
        else:
            return Response('invalid data')


# class based API view

class ProductDetailAPI(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class ProductListApi(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateAPI(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateAPI(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDeleteAPI(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def price_update(request):
    with transaction.atomic():
        Product.objects.all().update(price=F('price') + 1)
    return HttpResponse('updated')


def checking_union(request):
    # q1 = Product.objects.filter(title='abc class 1')
    # q2 = Product.objects.filter(price__gte=400)
    product_qs = Product.objects.all()
    q3 = Store.objects.all()
    # print(q1)
    # print(q2)
    # print(q1.union(q2))
    # print(q1|q3)
    # combined_list = list(chain(q1,q3))
    # print(combined_list)
    for st in q3:
        print(st.name,st.product,st.minor_product)

    for p in product_qs:
        print(p)
        for st1 in p.minor_prod.all():
        # for st1 in p.store_set.all():
            print(st1)


    return HttpResponse('union')




