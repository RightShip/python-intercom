# -*- coding: utf-8 -*-

import unittest

from intercom.client import Client
from mock import patch
from nose.tools import eq_
from nose.tools import istest
from tests.unit import test_help_center_collection, test_help_center_section


class HelpCenterTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()

    @istest
    def it_gets_a_collection(self):
        with patch.object(Client, 'get', return_value=test_help_center_collection) as mock_method:  # noqa
            collection = self.client.help_center_collections.find(name=test_help_center_collection['name'])
            eq_(collection.name, test_help_center_collection['name'])
            mock_method.assert_called_once_with('/help_center/collections', {'name': test_help_center_collection['name']})

    @istest
    def it_creates_a_collection(self):
        with patch.object(Client, 'post', return_value=test_help_center_collection) as mock_method:  # noqa
            collection = self.client.help_center_collections.create(name=test_help_center_collection['name'])
            eq_(collection.name, test_help_center_collection['name'])
            mock_method.assert_called_once_with('/help_center/collections/', {'name': test_help_center_collection['name']})

    @istest
    def it_gets_a_section(self):
        with patch.object(Client, 'get', return_value=test_help_center_section) as mock_method:  # noqa
            section = self.client.help_center_sections.find(name=test_help_center_section['name'])
            eq_(section.name, test_help_center_section['name'])
            mock_method.assert_called_once_with('/help_center/sections', {'name': test_help_center_section['name']})

    @istest
    def it_creates_a_section(self):
        with patch.object(Client, 'post', return_value=test_help_center_section) as mock_method:  # noqa
            section = self.client.help_center_sections.create(name=test_help_center_section['name'])
            eq_(section.name, test_help_center_section['name'])
            mock_method.assert_called_once_with('/help_center/sections/', {'name': test_help_center_section['name']})

