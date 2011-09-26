from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from cms.models import Page
from cms.menu_bases import CMSAttachMenu
from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool

from . import views

class SurveyMenu(CMSAttachMenu):
    name = "Survey menu"

    def get_nodes(self, request):
        """
        This method is used to build the menu tree.
        """
        nodes = [
            NavigationNode(
                _("Weekly survey"),
                reverse(views.index),
                "views.index",
            ),
            NavigationNode(
                _("Manage household"),
                reverse(views.people),
                "views.people",
            ),
        ]

        return nodes

menu_pool.register_menu(SurveyMenu)
