from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import ProductSerializer, RegisterUserSerializer
from products.models import Product, Review
from django.core.mail import send_mail
from django.conf import settings



@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET': '/api/products'},
        {'GET': '/api/products/id'},
        {'POST': '/api/products/id/vote'},
        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'},
        {'GET': '/api/testEmail'},
    ]
    return Response(routes)

@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
    return Response(routes)

@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def productVote(request, pk):
    product = Product.objects.get(id=pk)
    user = request.user.profile
    data = request.data

    review, created = Review.objects.get_or_create(
        owner = user,
        project = product
    )

    review.value = data['value']
    review.save()
    product.getVoteCount


    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def testEmail(request):
        send_mail(
            'sub',
            'mess',
            'testemails105@gmail.com',
            ['zanzong43@gmail.com'],
            fail_silently=False
        )
        return Response("done")


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getCart(request, pk):
    product = Product.objects.get(id=pk)
    user = request.user.profile
    data = request.data

    review, created = Review.objects.get_or_create(
        owner = user,
        project = product
    )

    review.value = data['value']
    review.save()
    product.getVoteCount


    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def productVote(request, pk):
    product = Product.objects.get(id=pk)
    data = request.data
    print(product)
    print(data)


    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def registerUser(request):
    reg_serializer = RegisterUserSerializer(data=request.data)
    if reg_serializer.is_valid():
        user = reg_serializer.save()
        if user:
            return Response(status=status.HTTP_201_CREATED)
    return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)