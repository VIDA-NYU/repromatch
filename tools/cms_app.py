from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

class ToolsAppHook(CMSApp):
    name = _('Tools')
    urls = ['tools.urls']

apphook_pool.register(ToolsAppHook)
