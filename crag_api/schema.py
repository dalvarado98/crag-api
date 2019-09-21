import graphene
import climbing_app.schema

class Query(climbing_app.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)