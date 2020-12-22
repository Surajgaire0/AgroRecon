from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'question': reverse('question_list', request=request, format=format),
        'question_upvote': reverse('question_upvote_toggle', request=request, format=format),
        'answer': reverse('answer_list', request=request, format=format),
        'answer_upvote': reverse('answer_upvote_toggle', request=request, format=format),
        'comment': reverse('comment_list', request=request, format=format),
        'comment_upvote': reverse('comment_upvote_toggle', request=request, format=format),
        'predict': reverse('predicted', request=request, format=format),
        'user_list': reverse('user_list', request=request, format=format),
        'password_change': reverse('password_change', request=request, format=format),
        'documentation': 'http://localhost:8000/api/docs/'
    })
