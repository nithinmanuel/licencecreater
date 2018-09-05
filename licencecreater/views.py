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


def upload_document(request):
    # we use Files because if it is media files then it's a get
    # if request.files['file'].filename == '':
    # return 'No selected file'
    #receive_data = json.loads(request.body.decode('utf-8'))
    #document = receive_data['document']
    if request.method == 'POST' and request.FILES['document']:
        document = request.FILES['document']
    #document = request.FILES.get('document')
    # if len(request.FILES) == 0:
    # return HttpResponse(status=400)
    if not document:
        return HttpResponse(status=400)

    if not document.name.endswith('.txt'):
        return HttpResponse(status=400)
    file = Document.objects.create(
        uploaded=document)  # defenition of the object
    file.save()  # created
    # this is a dictinary and it is used to respon

    response_data = {'id': file.id}

    # it should be converted into json so there is command
    response = json.dumps(response_data)
    return HttpResponse(response, content_type='json')


def download_converted_document(request, document_id):
    try:
        # create aya objectnte id eduthu athinuvendi mukalilathe id eduthu athu documentleku assign cheythu
        document = Document.objects.get(id=document_id)
    except:
        return HttpResponse(staus=404)

    file_content = convert_file(document.uploaded)
    print(file_content)
    response = json.dumps(file_content)
    print(response)
    return HttpResponse(response, content_type='json')

    # this is need to be converted into a file s


def create_keyword(request):  # create keyword
    # if the requst is empty means there is no data is send then give 404
    print (request.body)
    receive_data = json.loads(request.body.decode('utf-8'))
    keyword = receive_data['keyword']
    if not keyword:
        return HttpResponse(Status=400)

    obj, created = Keyword.objects.get_or_create(name=keyword)
    response_data = {'id': obj.id}

    response = json.dumps(response_data)
    return HttpResponse(response, content_type='json')


def get_keywords(request):  # list of keywords
    keyword = request.GET.get('keyword')
    #word = keyword.objects.filter(name__icontains='keyword')
    #data = []
    keywords = Keyword.objects.all()
    # print(keywords)
    response_data = []
    for keyword in keywords:
        response_data = {'id': keyword.id, 'name': keyword.name}
        # print(response_data)
    # for item in range(len(keywords)):
        # response_data.append('data')
        # print(response_data)
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


def single_keyword(request, keyword_id):
 # get one keyword
    if not keyword_id:
        return HttpResponse(staus=400)
    element = get_object_or_404(Keyword, id=keyword_id)
    response_data = {'id': element.id, 'name': element.name}
    response = json.dumps(response_data)
    return HttpResponse(response, content_type='json')


def edit_keyword(request, keyword_id):

    receive_data = json.loads(request.body.decode('utf-8'))
    keyword = receive_data['new_keyword']
    element = get_object_or_404(Keyword, id=keyword_id)
    print(element)
    element.name = keyword
    element.save()
    return HttpResponse()


def delete_keyword(request, keyword_id):

    if not keyword_id:
        return HttpResponse(staus=400)
    element = get_object_or_404(Keyword, id=keyword_id)
    element.delete()
    return HttpResponse()


# Create your views here.
