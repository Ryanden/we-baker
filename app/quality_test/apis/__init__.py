from django.shortcuts import get_list_or_404
from rest_framework import generics, permissions, status
from rest_framework.exceptions import NotAuthenticated
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework.views import APIView

from members.models import User
from recipe.models import Recipe
from ..models import QualityTest, TestInstitution
from ..serializers import QualityTestSerializer, TestInstitutionSerializer
from ..permission import IsUserOrReadOnly


# quality_test api
class QualityTestList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return self.list(request, *args, **kwargs)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def get_queryset(self):
        queryset = QualityTest.objects.filter(user=self.request.user)

        return queryset

    serializer_class = QualityTestSerializer


# 레시피와 업체를 선정하여 자가품질 검사 신청
class QualityTestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = QualityTest.objects.all()
    serializer_class = QualityTestSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsUserOrReadOnly,
    )

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class QualityTestCreate(APIView):
    permission_classes = (IsAuthenticated,)
    queryset = QualityTest.objects.all()
    serializer_class = QualityTestSerializer

    def get(self, request):

        if request.user.is_authenticated:
            return Response(QualityTestSerializer().data)
        raise NotAuthenticated('인증안됨')

    def post(self, request):

        if request.user.is_authenticated:
            user = User.objects.get(username=request.user)

            recipe = Recipe.objects.get(pk=request.data['recipe_pk'])

            institution = TestInstitution.objects.get(pk=request.data['institution_pk'])

            quality_test = QualityTest.objects.create(
                user=user,
                recipe=recipe,
                institution=institution,
            )

            return Response(QualityTestSerializer(quality_test).data, status=status.HTTP_201_CREATED)
        raise NotAuthenticated('인증안됨')


class TestInstitutionList(generics.ListAPIView):
    queryset = TestInstitution.objects.all()
    serializer_class = TestInstitutionSerializer
