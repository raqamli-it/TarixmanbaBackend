from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
# from user.models import CustomUser
from django.contrib.auth.models import User
from user.serializers import UserSerializers,  RegisterSerializer


class UserView(ListCreateAPIView):
    serializer_class = UserSerializers
    # pagination_class = ResultsSetPagination
    # filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend)
    # filterset_class = ParticipatingFinancialInstitutionFilter
    # ordering = ['pk']
    # search_fields = (
    #     'name',
    #     'region',
    #     'district',
    # )

    def get_queryset(self):
        return CustomUser.objects.all()

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class UserDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializers

    def get_queryset(self):
        return User.objects.all()

    def get(self, request, pk):
        instance = get_object_or_404(CustomUser, id=pk)
        serializer = self.serializer_class(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        instance = get_object_or_404(CustomUser, id=pk)
        serializer = self.serializer_class(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_202_ACCEPTED)

    def delete(self, request, pk):
        instance = get_object_or_404(CustomUser, id=pk)
        instance.delete()
        return Response(status.HTTP_204_NO_CONTENT)