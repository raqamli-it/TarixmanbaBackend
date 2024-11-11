from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class ResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'limit'
    max_page_size = 1000
    filters = None

    def get_paginated_response(self, data):
        # print(data)
        page_size = int(self.request.query_params.get('limit', self.page_size))
        return Response({
            'pagination': {
                'currentPage': self.page.number,
                'lastPage': self.page.paginator.num_pages,
                'perPage': page_size,
                'total': self.page.paginator.count,
            },
            'results': data,
            'filters': self.filters
        })

    @classmethod
    def set_filter(cls, filters):
        cls.filters = filters


class LargeResultsSetPagination(ResultsSetPagination):
    page_size = 1000