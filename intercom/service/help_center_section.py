# -*- coding: utf-8 -*-

from intercom import help_center_section
from intercom.api_operations.all import AllPaged
from intercom.api_operations.delete import Delete
from intercom.api_operations.find import Find
from intercom.api_operations.save import Save
from intercom.service.base_service import BaseService


class HelpCenterSection(BaseService, AllPaged, Find, Save, Delete):

    @property
    def collection_class(self):
        return help_center_section.HelpCenterSection
