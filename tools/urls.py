from django.conf.urls import patterns, url, include
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from tools.views import ToolList
from tools.models import Tool
from taggit.models import Tag

from haystack.views import SearchView, FacetedSearchView
from haystack.forms import SearchForm, FacetedSearchForm
from haystack.query import SearchQuerySet, EmptySearchQuerySet

from django.forms import ModelForm, ChoiceField, CharField
from django.db.models.query import EmptyQuerySet


class TagListView(ListView):
    model = Tool
    template_name = 'tool_list.html'
    def get_queryset(self):
        """ Only include entries tagged with the selected tag """
        return Tool.objects.filter(tags__slug=self.kwargs['tag_slug']).\
               extra(select={'lname':'lower(tools_tool.name)'}).order_by('lname')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ListView, self).get_context_data(**kwargs)
        # Add in the publisher
        tag = self.kwargs['tag_slug']
        context['tag'] = Tag.objects.get(slug=tag)
        print context['tag']
        return context


choice_tf = [['', ''], ['False', 'False'], ['True', 'True']]
class BoolField(ChoiceField):
    def __init__(self):
        super(BoolField, self).__init__(required=False, choices=choice_tf)

class SimpleForm(SearchForm):
    def search(self):
        if not hasattr(self, 'cleaned_data'):
            return self.no_query_found()
        elif not self.cleaned_data['q']:
            sqs = SearchQuerySet()
        else:
            sqs = super(SimpleForm, self).search()
        return sqs

class ToolForm(SearchForm):

    name = CharField()
    supports_osx = BoolField()
    supports_windows = BoolField()
    supports_linux = BoolField()
    supports_web_based = BoolField()

    capture = BoolField()
    capture_os = BoolField()
    capture_code = BoolField()
    capture_workflow = BoolField()
    capture_data = BoolField()

    representation = BoolField()
    representation_descriptive_only = BoolField()
    representation_executable = BoolField()

    replicability = BoolField()

    modifiability = BoolField()

    PORTABILITY_CHOICES = (
        ('', ''),
        ('NONE', 'None'),
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
    )
    portability = ChoiceField(required=False,choices=PORTABILITY_CHOICES)

    longevity = BoolField()
    longevity_archiving = BoolField()
    longevity_upgrading = BoolField()

    document_linkage = BoolField()
    document_linkage_by_reference = BoolField()
    document_linkage_inline = BoolField()

    experiment_sharing = BoolField()
    experiment_sharing_archival = BoolField()
    experiment_sharing_hosted_execution = BoolField()

    def search(self):
        if not hasattr(self, 'cleaned_data'):
            return self.no_query_found()
        elif not self.cleaned_data['q']:
            sqs = SearchQuerySet()
        else:
            sqs = super(ToolForm, self).search()

        bool_fields = [
            'supports_osx', 'supports_windows', 'supports_linux', 'supports_web_based',
            'capture', 'capture_os', 'capture_code', 'capture_workflow', 'capture_data',
            'representation', 'representation_descriptive_only', 'representation_executable',
            'replicability',
            'modifiability',
#            'portability',
            'longevity', 'longevity_archiving', 'longevity_upgrading',
            'document_linkage', 'document_linkage_by_reference', 'document_linkage_inline',
            'experiment_sharing', 'experiment_sharing_archival', 'experiment_sharing_hosted_execution'
            ]
        for field in bool_fields:
            if field in self.cleaned_data and self.cleaned_data[field]:
                sqs = sqs.filter(**{field:self.cleaned_data[field]=='True'})

        if 'portability' in self.cleaned_data and self.cleaned_data['portability']:
            sqs = sqs.filter(portability=self.cleaned_data['portability'])
        return sqs

fqs = SearchQuerySet().facet('capture').facet('capture_os').facet('capture_code').facet('capture_workflow').facet('capture_data').\
    facet('representation').facet('representation_descriptive_only').facet('representation_executable').\
    facet('replicability').facet('modifiability').\
    facet('portability').\
    facet('longevity').facet('longevity_archiving').facet('longevity_upgrading').\
    facet('document_linkage').facet('document_linkage_by_reference').facet('document_linkage_inline').\
    facet('experiment_sharing').facet('experiment_sharing_archival').facet('experiment_sharing_hosted_execution').\
    facet('supports_osx').facet('supports_windows').facet('supports_linux').facet('supports_web_based').\
    order_by('name')
    #extra(select={'lname':'lower(tools_tool.name)'}).order_by('lname')


class FacetedToolSearchForm(FacetedSearchForm):

    def no_query_found(self):
        return fqs

    def search(self):
        if not hasattr(self, 'cleaned_data'):
            return EmptySearchQuerySet()
        sqs = super(FacetedToolSearchForm, self).search()
        return sqs

urlpatterns = patterns('tools.views',
                       url(r'^$', ListView.as_view(model=Tool), name='tool-list'),
                       url(r'^tool/(?P<slug>[-_\w]+)/$', DetailView.as_view(model=Tool),
                           name='tool-detail'),
                       url(r'^tag/(?P<tag_slug>[-_\w]+)/$', TagListView.as_view(),
                           name='tool-tag-list'),
#                       url(r'^search/', SearchView(template='search/search.html',
#                                        form_class=SimpleForm)),
                       url(r'^search/', FacetedSearchView(template='search/search.html',
                                        form_class=FacetedToolSearchForm, searchqueryset=fqs)),
                       url(r'^search_table/', FacetedSearchView(template='search/search_table.html',
                                    form_class=FacetedToolSearchForm, searchqueryset=fqs,
                                    results_per_page=1000))
#                       url(r'^task_search/', SearchView(template='search/search_task.html',
#                                        form_class=ToolForm))
)
