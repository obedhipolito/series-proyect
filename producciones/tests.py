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
CREATE_PRODUCCION_MUTATION = '''
    mutation createProduccionesMutation($nombre: String, $temporadas: Int, $capitulos: Int, $duracion: Int, $clasificacion: String, $categoria: String, $idioma: String, $plataforma: String, $director: String, $protagonista: String){
        createProducciones(nombre: $nombre, temporadas: $temporadas, capitulos: $capitulos, duracion: $duracion, clasificacion: $clasificacion, categoria: $categoria, idioma: $idioma, plataforma: $plataforma, director: $director, protagonista: $protagonista){
            nombre
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

    def test_createProduccion_mutation(self):

        response = self.query(
            CREATE_PRODUCCION_MUTATION,
            variables={'nombre':'los simpson', 'temporadas':32, 'capitulos':706, 'duracion':21180, 'clasificacion':'mayores de 14 años', 'categoria':'comedia', 'idioma':'español e ingles', 'plataforma':'start +', 'director':'Matt Groening', 'protagonista':'homero simpson'}
        )
        print('mutation ')
        print(response)
        content = json.loads(response.content)
        print(content)
        self.assertResponseNoErrors(response)
        self.assertDictEqual({"createProducciones": {"nombre": "los simpson"}}, content['data'])