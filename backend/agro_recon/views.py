from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def home(request,format=None):
    return Response({
        'question':reverse('question_list',request=request,format=format),
        'answer':reverse('answer_list',request=request,format=format),
        'comment':reverse('comment_list',request=request,format=format),
        'predicted':reverse('predicted',request=request,format=format),
        'user_list':reverse('user_list',request=request,format=format),
        'password_change':reverse('password_change',request=request,format=format),
        'documentation':'http://localhost:8000/api/docs/'
    })