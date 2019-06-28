from rest_framework.generics import GenericAPIView


class CustomAPIView(GenericAPIView):

    def set_list_attr_in_request(self, request, request_params, list_param_name):
        list_attr = request.GET.getlist(list_param_name)
        if list_attr:
            request_params[list_param_name] = list_attr

    def get_pk_from_url(self, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            return int(kwargs.get('pk'))
        return pk
