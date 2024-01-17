
def get_validated_data(data, serializer_class, context=None, partial=False):
    serializer = serializer_class(data=data, partial=partial, context=context)
    serializer.is_valid(raise_exception=True)
    return serializer.validated_data
