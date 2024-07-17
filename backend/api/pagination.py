from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class ListedPagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data, include_data=None):
        resp = Response(data)
        resp["page_count"] = self.page.paginator.num_pages
        resp["object_count"] = self.page.paginator.count
        return resp
