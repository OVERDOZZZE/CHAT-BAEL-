from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from room.schema import schema

urlpatterns = [
    path('', include('core.urls')),
    path('rooms/', include('room.urls')),
    path('admin/', admin.site.urls),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]
