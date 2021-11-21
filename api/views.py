from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RecipeSerializer
from .models import Recipe


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/Recipe/',
            'method': 'GET',
            'body': None,
            'description': 'returns array of notes'
        },
        {
            'Endpoint': '/Recipe/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/Recipe/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Create new note with data sent in post request'
        },
        {
            'Endpoint': '/Recipe/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in request'
        },
        {
            'Endpoint': '/Recipe/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Creates an existing note with data sent in request'
        },
    ]
    return Response(routes)


@api_view(['GET'])
def getRecipes(request):
    recipe = Recipe.objects.all()
    serializer = RecipeSerializer(recipe, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getRecipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    serializer = RecipeSerializer(recipe, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def creatRecipe(request):
    data = request.data
    recipe = Recipe.objects.create(
        recipe=data['recipe'],
        country=data['country'],
        image=data['image'],
        description=data['description']
    )
    serializer = RecipeSerializer(recipe, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def updateRecipe(request, pk):
    data = request.data
    recipe = Recipe.objects.get(id=pk)
    serializer = RecipeSerializer(recipe, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteRecipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    recipe.delete()
    return Response("recipe was deleted")
