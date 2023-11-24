from typing import Dict, List
from ..serializers import UserCreateSerializer

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.tokens import RefreshToken


class UserCreateAV(CreateAPIView):
    serializer_class = UserCreateSerializer

    def create(
        self,
        request: Request,
        *args: List,
        **kwargs: Dict
    ) -> Response:

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        refresh = RefreshToken.for_user(serializer.save())

        return Response(
            data={
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            },

            status=status.HTTP_201_CREATED,
            headers=self.get_success_headers(serializer.data)
        )
