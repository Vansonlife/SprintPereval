from rest_framework import viewsets
from rest_framework.generics import ListAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.response import Response

from .models import Pereval, Images, Users
from .serializers import ImagesSerializer, PerevalAddSerializer, PerevalSubmitDataListSerializer, \
    PerevalSubmitDataUpdateSerializer, PerevalSubmitDataSerializer


class PerevalViewSet(viewsets.ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalAddSerializer

    def create(self, request):
        img = ImagesSerializer(data=request.data)
        if img.is_valid():
            img.save()
            return Response(status=201)
        else:
            print("ошибка")
            return Response({"error": "validation error"}, status=400)


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer


class SubmitDataDetailView(RetrieveAPIView):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSubmitDataSerializer


class SubmitDataUpdateView(UpdateAPIView):
    queryset = Users.objects.all()
    serializer_class = PerevalSubmitDataUpdateSerializer

    def update(self, request, *args, **kwargs):
        submit_data = self.get_object()

        if submit_data.status != 'new':
            message = 'Данные не могут быть отредактированы, т.к. статус "new" не соответствует.'
            return Response({'state': 0, 'message': message}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(submit_data, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response({'state': 1})


class SubmitDataListView(ListAPIView):
    queryset = Users.objects.all()
    serializer_class = PerevalSubmitDataListSerializer

    def get_queryset(self):
        email = self.request.query_params.get('user__email', None)
        if email is not None:
            return self.queryset.filter(user__email=email)
        return self.queryset.none()


