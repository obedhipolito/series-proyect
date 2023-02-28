import graphene
from graphene_django import DjangoObjectType

from .models import Produccion


class ProduccionType(DjangoObjectType):
    class Meta:
        model = Produccion


class Query(graphene.ObjectType):
    producciones = graphene.List(ProduccionType)

    def resolve_producciones(self, info, **kwargs):
        return Produccion.objects.all()