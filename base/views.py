from django.shortcuts import render
from django.http import JsonResponse, Http404
from django.db.models import Q

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Advocates
from .serializers import AdvocatesSerializer



@api_view(['GET'])
def endpoints(request):
  data = ['/advocates', '/advocades/:username']
  #return JsonResponse(data, safe=False)
  return Response(data)



@api_view(['GET', 'POST'])
def advocates_list(request):
  # Handle "GET" request
  if request.method == 'GET':
    #data = ["Arafat", "Sakib", "Ayon"]
    query = request.GET.get('query')
    if query == None:
      query = ''
    
    advocates = Advocates.objects.filter(Q(username__icontains=query) | Q(bio__icontains=query))
    serializer = AdvocatesSerializer(advocates, many=True)
    return Response(serializer.data)
  
  if request.method == 'POST':
    
    advocate = Advocates.objects.create(
      username = request.data['username'],
      bio = request.data['bio']
    )
    serializer = AdvocatesSerializer(advocate, many=False)
    return Response(serializer.data, status=status.HTTP_201_CREATED)



# @api_view(['GET', 'PUT', 'DELETE'])
# def advocate_detail(request, username):
#   #data = username
#   advocate = Advocates.objects.get(username=username)
  
#   if request.method == 'GET':
#     serializer = AdvocatesSerializer(advocate, many=False)
#     return Response(serializer.data)
  
  
#   if request.method == 'PUT':
#     advocate.username = request.data['username']
#     advocate.bio = request.data['bio']
#     advocate.save()
    
#     serializer = AdvocatesSerializer(advocate, many=False)
#     return Response(serializer.data)
  
  
#   if request.method == 'DELETE':
#     advocate.delete()
#     return Response("delete successful")



class Advocate_detail(APIView):
  def get_object(self, username):
    try:
      return Advocates.objects.get(username=username)
    except Advocates.DoesNotExist:
      raise Http404("Advocate doesn't exist!")
  
  def get(self, request, username):
    advocate = self.get_object(username)
    serializer = AdvocatesSerializer(advocate, many=False)
    return Response(serializer.data)
  
  def put(self, request, username):
    advocate = self.get_object(username)
    advocate.username = request.data['username']
    advocate.bio = request.data['bio']
    advocate.save()
    serializer = AdvocatesSerializer(advocate, many=False)
    return Response(serializer.data)
  
  def delete(self, request, username):
    advocate = self.get_object(username)
    advocate.delete()
    return Response("delete successful")
  