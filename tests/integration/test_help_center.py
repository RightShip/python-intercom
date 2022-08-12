# -*- coding: utf-8 -*-

import os
import unittest
from intercom.client import Client
from tests.integration import get_timestamp, create_help_center_collection, create_help_center_section

intercom = Client(
    os.environ.get('INTERCOM_PERSONAL_ACCESS_TOKEN'))


class HelpCenterTest(unittest.TestCase):

    @classmethod
    def setup_class(cls):
        cls.timestamp = get_timestamp()
        cls.collection = create_help_center_collection(intercom, cls.timestamp)
        cls.section = None

    @classmethod
    def teardown_class(cls):
        intercom.help_center_collections.delete(cls.collection)

        if cls.section:
            intercom.help_center_sections.delete(cls.section)

    def test_create_collection(self):
        self.assertIsNotNone(self.collection)
        self.assertIsNotNone(self.collection.id)

    def test_find_collection(self):
        collection = intercom.help_center_collections.find(id=self.collection.id)
        self.assertEqual(collection.url, self.collection.url)

    def test_update_collection(self):
        collection = intercom.help_center_collections.find(id=self.collection.id)
        now = get_timestamp()
        updated_name = f'{collection.name} {now}'
        collection.name = updated_name
        intercom.help_center_collections.save(collection)
        collection = intercom.help_center_collections.find(id=collection.id)
        self.assertEqual(collection.name, updated_name)

    def test_iterate_collections(self):
        for collection in intercom.help_center_collections.all(per_page=2):
            self.assertIsNotNone(collection.id)
            break

    def test_create_section(self):
        self.section = create_help_center_section(intercom, self.collection, self.timestamp)

        self.assertIsNotNone(self.section)
        self.assertIsNotNone(self.section.id)
        self.assertEqual(self.section.parent_id, self.collection.id)

    def test_find_section(self):
        self.section = create_help_center_section(intercom, self.collection, self.timestamp)

        section = intercom.help_center_sections.find(id=self.section.id)
        self.assertEqual(section.url, self.section.url)

    def test_update_section(self):
        self.section = create_help_center_section(intercom, self.collection, self.timestamp)

        section = intercom.help_center_sections.find(id=self.section.id)
        now = get_timestamp()
        updated_name = f'{section.name} {now}'
        section.name = updated_name
        intercom.help_center_sections.save(section)
        section = intercom.help_center_sections.find(id=section.id)
        self.assertEqual(section.name, updated_name)

    def test_iterate_sections(self):
        for section in intercom.help_center_sections.all(per_page=2):
            self.assertIsNotNone(section.id)
            break
