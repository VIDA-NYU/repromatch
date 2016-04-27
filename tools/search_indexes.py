#import datetime
from haystack import indexes
from tools.models import Tool


class ToolIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    # index name lowercase for sorting
    name = indexes.CharField(model_attr='name', stored=True, indexed=True)
    def prepare_name(self, object):
        return object.name.lower()

    capture = indexes.BooleanField(model_attr='capture', faceted=True)
    capture_os = indexes.BooleanField(model_attr='capture_os', faceted=True)
    capture_code = indexes.BooleanField(model_attr='capture_code', faceted=True)
    capture_workflow = indexes.BooleanField(model_attr='capture_workflow', faceted=True)
    capture_data = indexes.BooleanField(model_attr='capture_data', faceted=True)

    representation = indexes.BooleanField(model_attr='representation', faceted=True)
    representation_descriptive_only = indexes.BooleanField(model_attr='representation_descriptive_only', faceted=True)
    representation_executable = indexes.BooleanField(model_attr='representation_executable', faceted=True)

    replicability = indexes.BooleanField(model_attr='replicability', faceted=True)

    modifiability = indexes.BooleanField(model_attr='modifiability', faceted=True)

    portability = indexes.CharField(model_attr='portability', faceted=True)

    longevity = indexes.BooleanField(model_attr='longevity', faceted=True)
    longevity_archiving = indexes.BooleanField(model_attr='longevity_archiving', faceted=True)
    longevity_upgrading = indexes.BooleanField(model_attr='longevity_upgrading', faceted=True)

    document_linkage = indexes.BooleanField(model_attr='document_linkage', faceted=True)
    document_linkage_by_reference = indexes.BooleanField(model_attr='document_linkage_by_reference', faceted=True)
    document_linkage_inline = indexes.BooleanField(model_attr='document_linkage_inline', faceted=True)

    experiment_sharing = indexes.BooleanField(model_attr='experiment_sharing', faceted=True)
    experiment_sharing_archival = indexes.BooleanField(model_attr='experiment_sharing_archival', faceted=True)
    experiment_sharing_hosted_execution = indexes.BooleanField(model_attr='experiment_sharing_hosted_execution', faceted=True)

    supports_osx = indexes.BooleanField(model_attr='supports_osx', faceted=True)
    supports_windows = indexes.BooleanField(model_attr='supports_windows', faceted=True)
    supports_linux = indexes.BooleanField(model_attr='supports_linux', faceted=True)
    supports_web_based = indexes.BooleanField(model_attr='supports_web_based', faceted=True)

    def get_model(self):
        return Tool

    def index_queryset(self, using=False):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
