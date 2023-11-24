from users.models import User
from rest_framework.serializers import ModelSerializer

from typing import Dict


class UserCreateSerializer(ModelSerializer):

    def create(self, validated_data: Dict) -> User:
        user = User(
            email=validated_data['email']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User

        fields = [
            'email',
            'password'
        ]

        extra_kwargs = {
            'password': {'write_only': True}
        }


class UserMeSerializer(ModelSerializer):

    class Meta:
        model = User

        fields = [
            'email',
        ]
