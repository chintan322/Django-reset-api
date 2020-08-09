from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import View

from django.core.serializers import serialize
from cfeapi.mixins import JsonResponseMixin
from .models import Update

# def detail_view(request):
#     # return render() # return JSON data --> JS Object Notation
#     return HttpResponse(get_template().render({}))



def json_example_view(request):
    '''
    URI -- for a REST API
    GET -- Retrieve
    '''
    data = {
        "count": 1000,
        "content": "some new content"
    }
    return JsonResponse(data)

class JsonCBV(View):
    def get(self,request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "some new content"
        }
        return JsonResponse(data)



class JsonCBV2(JsonResponseMixin, View):
    def get(self,request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "some new content"
        }
        return self.render_to_json_response(data)

class SerializedView(View):
    def get(self,request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        json_data = obj.serialize()
        return HttpResponse(json_data)

class SerializedListView(View):
    def get(self,request, *args, **kwargs):
        qs = Update.objects.all()
        json_data = Update.objects.all().serialize()
        return HttpResponse(json_data)