from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from updates.models import Update as UpdateModel

from .mixins import CSRFExemptMixin

#Creating, updating, Deleting, Retriving(1) --Update Model

class UpdateModelDetailAPIView(CSRFExemptMixin,View):
    '''
    Retrieve, Update, Ddelete ---> Object
    '''
    def get(self, request, id, *args, ** kwargs):
        obj = UpdateModel.objects.get(id=id)
        json_data = obj.serialize()
        return HttpResponse(json_data)

    def post(self, request, *args, ** kwargs):

        return HttpResponse({})

    def put(self, request, *args, ** kwargs):

        return HttpResponse({})

    def delete(self, request, *args, ** kwargs):

        return HttpResponse({})

class UpdateModelListAPIView(CSRFExemptMixin,View):
    """
    List Vieew
    Create View
    """

    def render_to_response(data, status=200):
        return JsonResponse(data, status=status)

    def get(self, request, *args, ** kwargs):
        qs = UpdateModel.objects.all()
        json_data = qs.serialize()
        return self.render_to_response(json_data)

    def post(self, request, *args, ** kwargs):
        data = {
            "message":"Unknown data"
        }
        return self.render_to_response(data, status=400)

    def delete(self, request, *args, ** kwargs):
        data = {
            "message":"You canot delete as entire list"
        }
        return self.render_to_response(data, status=403)