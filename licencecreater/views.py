from django.shortcuts import render
from licencecreater.utilities import*
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from .models import Keyword
from .models import Document
import json
from django.core import serializers
import os
from django.core.files import File
# by post method we will get the file using the if request.method and it is assign to document variable twice 
# using the if condition first to check wheather the file is in the request and second is to check the file is a txt file
# if it has file and it is atxt file the it prevails else fails and invoke status 400. The file is need to store in the databse
# for this reason the file is creating in line 33 , here the document is passing through one of the attributies of the class document
# and the file is created as an object in databse . for every object created in the database has a unique id(feteching it in line 40) , this id is need 
# to be returned as a response and in line 43 it depics to how to return in as a json resposne.

def upload_document(request):
    
    if request.method == 'POST' and request.FILES['document']:
        document = request.FILES['document']
    
    if not document:
        return HttpResponse(status=400)

    if not document.name.endswith('.txt'):
        return HttpResponse(status=400)
    file = Document.objects.create(
        uploaded=document)  
    file.save()  # created
   

    response_data = {'id': file.id}

   
    response = json.dumps(response_data)
    return HttpResponse(response, content_type='json')


# The id of the document is need to perform the appending the trademark symbol , firstly calling the get function
# using the try and except and if the document id is in the GET REQUEST  then it pass to a function in line 57 ELSE 404.
# The id is passing to a function which is responsbile for the operation to append the symbol and the file_content will
# have the modified file content and this modified file content gives as reponse in json format.(line 61) ? the missing parts 
# the document need to save in the converted file it is on the way..

def download_converted_document(request, document_id):
    try:
        
        document = Document.objects.get(id=document_id)
    except:
        return HttpResponse(staus=404)

    file_content = convert_file(document.uploaded)
    print(file_content)
    response = json.dumps(file_content)    # the resposne is need to create as an object 
    print(response)
    return HttpResponse(response, content_type='json')

 # To create the a set of words that is to undergo the transformation which is mentioned above . the word need to add to the
   # database should pass in json format ( line 75) receving the data as post and decoding the encoded format proceed by assign
# it to a a varible in line 77. like previous cases checking that wheather the POST request lands in the funcrion create_keyword
# contains word or something else and preceeed only the request carries the word. line number 82 is to create the object as it 
# happens through the one and only attribute of the selected word need to face the alternation. As it stated above each object
# in the database has a distinctive id which is required to be enclosed in the json response and the lines 85, 87 performing this art.

    
    
def create_keyword(request):  # create keyword
    
    print (request.body)
    receive_data = json.loads(request.body.decode('utf-8'))
    keyword = receive_data['keyword']
    if not keyword:
        return HttpResponse(Status=400)

    obj, created = Keyword.objects.get_or_create(name=keyword)
    response_data = {'id': obj.id}

    response = json.dumps(response_data)
    return HttpResponse(response, content_type='json')

# A GET Request to get all words which is created in database through json. it initaites with a GET request and it is passing
# to a varibale in line 94 . next line is for to get all the words in databse(97 line) . line number 100 calling a for loop
# and inside this for loop iterating the each and every word that is allready in the databse and pick up the id and the name 
# of the keyword guides to the dictionary declared in line 101 , storing the data from line 103 into line 101 dictionary. Rest 
# of the operation is same in the previous cases.


def get_keywords(request):  # list of keywords
    keyword = request.GET.get('keyword')
    
    keywords = Keyword.objects.all()
    # print(keywords)
    response_data = []
    for keyword in keywords:
        response_data = {'id': keyword.id, 'name': keyword.name}
        
        response = json.dumps(response_data)
        print(response)
        return HttpResponse(response, content_type='json')
    # return JsonResponse((response), safe=False)
    #response = json.dumps(response_data)
    # print(response)
    # return JsonResponse(response, sasfe=False)
    # return HttpResponse(response, content_type='json')


# def get_keywords(request, keyword):  # list of keywords
    #keywords = get_list_or_404(Keyword, name=keyword)
    #response_data = {'id': keywords.id, 'name': keyword.name}
    # return(json.dumps(response_data))

    
# A GET request to get a single word from the database for this the request comes with the id if the word which is want to return
# as a json response. In line 132 makes the job easier by collecting the requied object and this object is pass to the variable in the asme line
# next actions are riping the atributes of the object and send convert and send it as json response.

def single_keyword(request, keyword_id):
 # get one keyword
    if not keyword_id:
        return HttpResponse(staus=400)
    element = get_object_or_404(Keyword, id=keyword_id)
    response_data = {'id': element.id, 'name': element.name}
    response = json.dumps(response_data)
    return HttpResponse(response, content_type='json')

# This operation is to replace a word which is no longer wanted as word that is supposed to modify inside the file . it is a 
# POST operation carries the id of the word need to change not only this but also brings the new word to be in place of the word that will undergo a change . 
# Thanks to get_object method to find the object supposed to substitute line 148 performs the operation of replacing the words 
# and it will deleiver a sucess message

def edit_keyword(request, keyword_id):

    receive_data = json.loads(request.body.decode('utf-8'))
    keyword = receive_data['new_keyword']
    element = get_object_or_404(Keyword, id=keyword_id)
    print(element)
    element.name = keyword
    element.save()
    return HttpResponse()

# the delete operation is to delete the particular word from the database and it is get request contains the id of the word 
# want to delete which will get through get_object operation in the line 160 and the following lines performs the actions to delete
# in line 162. finaly returns a http response.

def delete_keyword(request, keyword_id):

    if not keyword_id:
        return HttpResponse(staus=400)
    element = get_object_or_404(Keyword, id=keyword_id)
    element.delete()
    return HttpResponse()


# Create your views here.
