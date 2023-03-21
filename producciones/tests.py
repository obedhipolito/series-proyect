from django.test import TestCase
from graphene_django.utils.testing import GraphQLTestCase
from mixer.backend.django import mixer
import graphene
import json

# Create your tests here.

from series.schema import schema
from producciones.models import Produccion

PRODUCCION_QUERY = '''{
    producciones{
        id
        nombre
        temporadas
        capitulos
        duracion
        clasificacion
        categoria
        idioma
        plataforma
        director
        protagonista
    }
}
'''

class ProduccionTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    def setUp(self):
        self.producciones1 = mixer.blend(Produccion)
        self.producciones2 = mixer.blend(Produccion)
    
    def test_producciones_query(self):
        response = self.query(
            PRODUCCION_QUERY,
        )
        content = json.loads(response.content)
        #print(content)
        self.assertResponseNoErrors(response)
        print("query producciones results ")
        print(content)
        assert len(content['data']['producciones']) == 2