from rest_framework.pagination import PageNumberPagination

class SmallSet(PageNumberPagination):
    page_size = 2
