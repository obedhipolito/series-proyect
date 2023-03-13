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

#tarea, cambiar por mis datos
class CreateProduccion(graphene.Mutation):
    id = graphene.Int()
    nombre = graphene.String()
    temporadas = graphene.Int()
    capitulos = graphene.Int()
    duracion = graphene.Int()
    clasificacion = graphene.String()
    categoria = graphene.String()
    idioma = graphene.String()
    plataforma = graphene.String()
    director = graphene.String()
    protagonista = graphene.String()

    #2
    class Arguments:
        nombre = graphene.String()
        temporadas = graphene.Int()
        capitulos = graphene.Int()
        duracion = graphene.Int()
        clasificacion = graphene.String()
        categoria = graphene.String()
        idioma = graphene.String()
        plataforma = graphene.String()
        director = graphene.String()
        protagonista = graphene.String()

    #3
    def mutate(self, info, nombre, temporadas, capitulos, duracion, clasificacion, categoria, idioma,plataforma, director, protagonista):
        produciones = Produccion(nombre=nombre, temporadas=temporadas, capitulos=capitulos, duracion=duracion, clasificacion=clasificacion, categoria=categoria, idioma=idioma,plataforma=plataforma, director=director, protagonista=protagonista)
        produciones.save()

        return CreateProduccion(
            id=produciones.id,
            nombre=produciones.nombre,
            temporadas=produciones.temporadas,
            capitulos=produciones.capitulos,
            duracion=produciones.duracion,
            clasificacion=produciones.clasificacion,
            categoria=produciones.categoria,
            idioma=produciones.idioma,
            plataforma=produciones.plataforma,
            director=produciones.director,
            protagonista=produciones.protagonista
        )


#4
class Mutation(graphene.ObjectType):
    create_producciones = CreateProduccion.Field()