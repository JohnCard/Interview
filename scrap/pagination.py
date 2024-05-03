from rest_framework.pagination import PageNumberPagination, CursorPagination

class vehiclePagination(PageNumberPagination):
    page_query_param = 'p'
    page_size_query_param = 'size'
    max_page_size = 5
    last_page_strings = 'end'
    
class ProductCPagination(CursorPagination):
    page_size = 4
    