import random
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from djpj import pjax_block
from apps.accounts.models import SubscriptionBanner
from apps.shows.models import Show, ShowCategory


class CategoryMixin(object):
    category = None
    category_url_name = None
    all_url_name = None

    def get_queryset(self):
        qs = super(CategoryMixin, self).get_queryset()

        if self.kwargs.get('category'):
            self.category = get_object_or_404(ShowCategory, title=self.kwargs.get('category'))
            qs = qs.filter(category=self.category)

        return qs

    def get_context_data(self, **kwargs):
        context = super(CategoryMixin, self).get_context_data(**kwargs)
        context['category'] = self.category
        context['category_url_name'] = self.category_url_name
        context['all_url_name'] = self.all_url_name

        return context


class IndexView(ListView):
    model = Show
    template_name = 'index.html'

    # @method_decorator(pjax_block(title_variable="blog_post_title"))
    @method_decorator(pjax_block('pjax-content', title_block='head_title'))
    def dispatch(self, request, *args, **kwargs):
        return super(IndexView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return super(IndexView, self).get_queryset()[1:6]

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        if self.request.user.is_authenticated():
            subscription_banners = SubscriptionBanner.objects.filter(type=SubscriptionBanner.UPGRADE)
        else:
            subscription_banners = SubscriptionBanner.objects.filter(type=SubscriptionBanner.SIGNUP)

        if subscription_banners:
            context['subscription_banner'] = random.choice(subscription_banners)

        return context


class ShowsList(CategoryMixin, ListView):
    model = Show
    template_name = 'shows/list.html'
    category_url_name = 'shows:archive_category'
    all_url_name = 'shows:archive'

    # @method_decorator(pjax_block(title_variable="blog_post_title"))
    @method_decorator(pjax_block('pjax-content', title_block='head_title'))
    def dispatch(self, request, *args, **kwargs):
        return super(ShowsList, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ShowsList, self).get_context_data(**kwargs)
        context['categories'] = ShowCategory.objects.all()

        return context


class SearchView(CategoryMixin, ListView):
    model = Show
    template_name = 'shows/search.html'
    category_url_name = 'shows:search_category'
    all_url_name = 'shows:search'
    q = None

    # @method_decorator(pjax_block(title_variable="blog_post_title"))
    @method_decorator(pjax_block('pjax-content', title_block='head_title'))
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

        if self.kwargs.get('category'):
            qs = qs.filter(category=self.category)

        self.queryset = qs
        return qs

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        context['categories'] = ShowCategory.objects.filter(shows__in=self.queryset).distinct()
        context['q'] = self.q

        return context

