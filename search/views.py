from search.models import Product
from search.serializers import ProductSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from search.serializers import UserSerializer
from rest_framework import permissions
from rest_framework import viewsets
from django.http import HttpResponse
from django.template.loader import get_template
from .forms import *
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset =Product.objects.all()
    serializer_class = ProductSerializer

def searchprod(request):
    form = ContactForm()
    template = get_template('image.html')
    if request.method == 'GET':
        html = template.render({'form':form },request)
        return HttpResponse(html)
    elif request.method == 'POST':
        form = ContactForm(data=request.POST)
        form.fields['producto'].error_messages = {'required': 'Este campo es requerido'}
        if form.is_valid():
            results = Product.objects.filter(name=request.POST['producto'])
            html = template.render({'results': results, 'form': form}, request)
            return HttpResponse(html)
