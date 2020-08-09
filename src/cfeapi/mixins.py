from django.http import JsonResponse


class JsonResponseMixin(object):
    def render_to_json_response(self, context, **response_kwards):
        return JsonResponse(self.get_data(context), ** response_kwards)

    def get_data(self, context):
        return context