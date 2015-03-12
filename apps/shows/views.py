from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from djpj import pjax_block
from apps.shows.models import Show, ShowCategory


class IndexView(ListView):
    model = Show
    template_name = 'index.html'

    # @method_decorator(pjax_block(title_variable="blog_post_title"))
    @method_decorator(pjax_block('content'))
    def dispatch(self, request, *args, **kwargs):
        return super(IndexView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return super(IndexView, self).get_queryset()[:4]


class ShowsList(ListView):
    model = Show
    template_name = 'shows/list.html'
    category = None

    # @method_decorator(pjax_block(title_variable="blog_post_title"))
    @method_decorator(pjax_block('content'))
    def dispatch(self, request, *args, **kwargs):
        return super(ShowsList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        qs = super(ShowsList, self).get_queryset()

        if self.kwargs.get('category'):
            self.category = get_object_or_404(ShowCategory, title=self.kwargs.get('category'))
            qs = qs.filter(category=self.category)

        return qs

    def get_context_data(self, **kwargs):
        context = super(ShowsList, self).get_context_data(**kwargs)
        context['categories'] = ShowCategory.objects.all()
        context['category'] = self.category

        return context

