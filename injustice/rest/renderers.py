from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer

class CustomJSONRenderer(JSONRenderer, BrowsableAPIRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response_data = { }

        resource = getattr(renderer_context.get('view').get_serializer().Meta, 'resource_name', 'objects')

        try:
            data.get('paginated_results')
            response_data['meta'] = data['meta']
            response_data[resource] = data.get('paginated_results')
        except:
            response_data[resource] = data

        response = super(CustomJSONRenderer, self).render(response_data, accepted_media_type, renderer_context)

        return response
