from rest_framework  import viewsets
from api.permissions import IsAuthorOrReadOnly
from questions.serializers import QuestionSerializer,AnswerSerializer
from questions.models import Question, Answer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status
from rest_framework.generics import  get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView

class IndexTemplateView(LoginRequiredMixin, TemplateView):

    def get_template_names(self):
        template_name = 'index.html'
        return template_name

class QuestionViewSet(viewsets.ModelViewSet):


    queryset = Question.objects.all()
    lookup_field = 'slug'
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated,IsAuthorOrReadOnly,]
    pagination_class = PageNumberPagination

    def perform_create(self, serializer):

        serializer.save(author=self.request.user)

class AnswerAPIView(generics.CreateAPIView):

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated,]

    def perform_create(self, serializer):

        request_user = self.request.user

        kwargs_slug = self.kwargs.get("slug")
        question = get_object_or_404(Question, slug = kwargs_slug)

        if question.answers.filter(author=request_user).exists():
            raise ValidationError("You have already answered  the Question!")

        serializer.save(author = request_user, question = question)

class AnswerListAPIView(generics.ListAPIView):

    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated,]
    pagination_class = PageNumberPagination

    def  get_queryset(self):

        kwargs_slug = self.kwargs.get("slug")

        return Answer.objects.filter(question__slug = kwargs_slug).order_by('-created_at')

class AnswerRUDAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated,IsAuthorOrReadOnly,]

class AnswerLikeAPIView(APIView):

    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated,]

    def delete(self,request,pk):

        answer = get_object_or_404(Answer, pk=pk)
        user = self.request.user

        answer.voters.remove(user)
        answer.save()

        serializer = self.serializer_class(answer, context={'request':request})

        return Response(serializer.data,status = status.HTTP_200_OK)


    def post(self, request, pk):

        answer = get_object_or_404(Answer, pk=pk)
        user = self.request.user

        answer.voters.add(user)
        answer.save()

        serializer = self.serializer_class(answer, context={'request':request})

        return Response(serializer.data,status = status.HTTP_200_OK)
