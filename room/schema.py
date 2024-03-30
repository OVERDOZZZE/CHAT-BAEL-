import graphene
from graphene_django import DjangoObjectType
from .models import Room


class RoomType(DjangoObjectType):
    class Meta:
        model = Room
        fields = '__all__'


class Query(graphene.ObjectType):
    rooms = graphene.List(RoomType)

    def resolve_rooms(self, info, **kwargs):
        return Room.objects.all()


schema = graphene.Schema(query=Query)
