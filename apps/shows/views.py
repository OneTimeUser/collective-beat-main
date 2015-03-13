from django.core.urlresolvers import reverse
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
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


class SearchView(ListView):
    model = Show
    template_name = 'shows/search.html'
    q = None

    # @method_decorator(pjax_block(title_variable="blog_post_title"))
    @method_decorator(pjax_block('content'))
    def dispatch(self, request, *args, **kwargs):
        self.q = request.GET.get('q')
        if not self.q:
            return redirect(reverse('shows:archive'))

        return super(SearchView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        qs = super(SearchView, self).get_queryset()
        qs = qs.filter(
            Q(title__icontains=self.q)
            | Q(keywords__icontains=self.q)
            | Q(description__icontains=self.q)
        )

        return qs

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        context['q'] = self.q

        return context

