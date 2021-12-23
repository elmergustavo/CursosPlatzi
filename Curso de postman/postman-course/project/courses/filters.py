from rest_framework import filters


class FilterByDate(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        begin_date = request.GET.get('begin_date')
        end_date = request.GET.get('end_date')

        if begin_date:
            queryset = queryset.filter(created_at__gte=begin_date)

        if end_date:
            queryset = queryset.filter(created_at__lte=end_date)

        return queryset
