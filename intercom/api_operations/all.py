# -*- coding: utf-8 -*-
"""Operation to retrieve all instances of a particular resource."""

from intercom import utils
from intercom.collection_proxy import CollectionProxy


class All(object):
    """A mixin that provides `all` functionality."""

    def all(self):
        """Return a CollectionProxy for the resource."""
        collection = utils.resource_class_to_collection_name(
            self.collection_class)
        finder_url = "/%s" % (collection)
        return CollectionProxy(
            self.client, self.collection_class, collection, finder_url)

class AllPaged(object):
    """A mixin that provides `all` functionality with paging support."""

    def all(self, per_page=25, page=1):
        """Return a CollectionProxy for the resource."""
        collection = utils.resource_class_to_collection_name(
            self.collection_class)
        finder_url = "/%s" % (collection)
        finder_params = {
            "per_page": per_page,
            "page": page
        }
        return CollectionProxy(
            self.client, self.collection_class, collection, finder_url, finder_params)