from django.views.generic import CreateView, DeleteView, DetailView, UpdateView

from ..models import Comment


class CommentCreateView(CreateView):
    model = Comment
    fields = ['title', 'description', 'image']
    template_name = 'plataforma/comment/comment_create.html'
    success_url = '/'


class CommentDetailView(DetailView):
    model = Comment
    template_name = 'plataforma/comment/comment_detail.html'


class CommentUpdateView(UpdateView):
    model = Comment
    fields = ['title', 'description', 'image']
    template_name = 'plataforma/comment/comment_update.html'
    success_url = '/'


class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'plataforma/comment/comment_delete.html'
    success_url = '/'
