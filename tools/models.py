from django.db import models
from taggit.managers import TaggableManager
from django.template.defaultfilters import slugify
class Tool(models.Model):
    name = models.CharField(verbose_name='Software name', max_length=100)
    slug = models.SlugField(editable=False)
    description = models.CharField(verbose_name='Description', max_length=1024)
    website = models.URLField(verbose_name='Website', default='', blank=True)
    source = models.URLField(verbose_name='Source Code Repository', default='', blank=True)
    paper = models.URLField(verbose_name='Link To Paper', default='', blank=True)
    tags = TaggableManager(blank=True)

    capture = models.BooleanField(verbose_name='Capture', default=False)
    capture_os = models.BooleanField(verbose_name='OS-Based Capture', default=False)
    capture_code = models.BooleanField(verbose_name='Code-Based Capture', default=False)
    capture_workflow = models.BooleanField(verbose_name='Workflow-Based Capture',
                                      default=False)
    capture_data = models.BooleanField(verbose_name='Data-Based Capture',
                                  default=False)
    capture_note = models.CharField(verbose_name='Note', max_length=200,
                                    default='', blank=True)

    representation = models.BooleanField(verbose_name='Representation', default=False)
    representation_descriptive_only = models.BooleanField(verbose_name='Descriptive-Only',
                                                     default=False)
    representation_executable = models.BooleanField(verbose_name='Executable',
                                               default=False)
    representation_note = models.CharField(verbose_name='Note', max_length=1024,
                                           default='', blank=True)

    replicability = models.BooleanField(verbose_name='Replicability', default=False)
    replicability_note = models.CharField(verbose_name='Note', max_length=1024,
                                          default='', blank=True)

    modifiability = models.BooleanField(verbose_name='Modifiability', default=False)
    modifiability_note = models.CharField(verbose_name='Note', max_length=1024,
                                          default='', blank=True)

    PORTABILITY_CHOICES = (
        ('NONE', 'None'),
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
    )
    portability = models.CharField(verbose_name='Portability',
                                   choices=PORTABILITY_CHOICES,
                                   max_length=6, default='NONE')
    portability_note = models.CharField(verbose_name='Note', max_length=1024,
                                        default='', blank=True)

    longevity = models.BooleanField(verbose_name='Longevity', default=False)
    longevity_archiving = models.BooleanField(verbose_name='Archiving', default=False)
    longevity_upgrading = models.BooleanField(verbose_name='Upgrading', default=False) 
    longevity_note = models.CharField(verbose_name='Note', max_length=1024,
                                      default='', blank=True)

    document_linkage = models.BooleanField(verbose_name='Document Linkage',
                                      default=False)
    document_linkage_by_reference = models.BooleanField(verbose_name='By Reference',
                                                   default=False)
    document_linkage_inline = models.BooleanField(verbose_name='Inline', default=False)
    document_linkage_note = models.CharField(verbose_name='Note', max_length=1024,
                                             default='', blank=True)

    experiment_sharing = models.BooleanField(verbose_name='Experiment Sharing',
                                        default=False)
    experiment_sharing_archival = models.BooleanField(verbose_name='Archival',
                                                 default=False)
    experiment_sharing_hosted_execution = \
        models.BooleanField(verbose_name='Hosted Execution', default=False)
    experiment_sharing_note = models.CharField(verbose_name='Note', max_length=1024,
                                               default='', blank=True)

    supports_osx = models.BooleanField(verbose_name='Support for OSX', default=False)
    supports_windows = models.BooleanField(verbose_name='Support for Windows',
                                      default=False)
    supports_linux = models.BooleanField(verbose_name='Support for Linux',
                                    default=False)
    supports_web_based = models.BooleanField(verbose_name='Support for Web-based access',
                                    default=False)
    supports_note = models.CharField(verbose_name='Note', max_length=1024,
                                     default='', blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        # Auto-set main categories if not set (Only main set is still possible)
        if self.capture_os or self.capture_code or self.capture_workflow or self.capture_data:
            self.capture = True
        if self.representation_descriptive_only or self.representation_executable:
            self.representation = True
        if self.longevity_archiving or self.longevity_upgrading:
            self.longevity = True
        if self.document_linkage_by_reference or self.document_linkage_inline:
            self.document_linkage = True
        if self.experiment_sharing_archival or self.experiment_sharing_hosted_execution:
            self.experiment_sharing = True
        return super(Tool, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name
