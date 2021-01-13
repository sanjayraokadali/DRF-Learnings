from rest_framework  import viewsets
from api.permissions import IsAuthorOrReadOnly
from questions.serializers import QuestionSerializer
from questions.models import Question
from  rest_framework.permissions import IsAuthenticated

class QuestionViewSet(viewsets.ModelViewSet):


    queryset = Question.objects.all()
    lookup_field = 'slug'
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated,IsAuthorOrReadOnly,]

    def perform_create(self, serializer):

        serializer.save(author=self.request.user)
