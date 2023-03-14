import graphene

import producciones.schema

class Query(producciones.schema.Query, graphene.ObjectType):
    pass

class Mutation(producciones.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)