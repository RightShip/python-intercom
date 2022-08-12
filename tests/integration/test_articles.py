# -*- coding: utf-8 -*-

import os
import unittest
from intercom.client import Client
from intercom.article import Locale
from tests.integration import get_timestamp, create_help_center_collection, create_help_center_section

intercom = Client(
    os.environ.get('INTERCOM_PERSONAL_ACCESS_TOKEN'))


class ArticleTest(unittest.TestCase):

    @classmethod
    def setup_class(cls):
        cls.article = intercom.articles.create(
            title="Thanks for everything",
            description="English description",
            body="<p>This is the body in html</p>",
            author_id="39153",
            translated_content={
                "fr": {
                    "title": "Allez les verts",
                    "description": "French description",
                    "body": "<p>French body in html</p>",
                    "author_id": "39153",
                    "state": "published"
                }
            }
        )

    @classmethod
    def teardown_class(cls):
        intercom.articles.delete(cls.article)

    def setUp(self):
        self.collection = None

    def tearDown(self):
        if self.collection:
            intercom.help_center_collections.delete(self.collection)

    def test_create_article(self):
        self.assertIsNotNone(self.article)
        self.assertIsNotNone(self.article.id)

    def test_find_article(self):
        article = intercom.articles.find(id=self.article.id)
        self.assertEqual(article.body, self.article.body)

    def test_update_article(self):
        article = intercom.articles.find(id=self.article.id)
        now = get_timestamp()
        updated_title = f'{article.title} {now}'
        article.title = updated_title
        intercom.articles.save(article)
        article = intercom.articles.find(id=article.id)
        self.assertEqual(article.title, updated_title)

    def test_iterate_articles(self):
        for article in intercom.articles.all(per_page=2):
            self.assertIsNotNone(article.id)
            break

    def test_add_article_to_collection(self):
        self.collection = create_help_center_collection(intercom, get_timestamp())

        article = intercom.articles.find(id=self.article.id)
        article.parent_id = self.collection.id
        article.parent_type = 'collection'
        intercom.articles.save(article)
        article = intercom.articles.find(id=self.article.id)
        self.assertEqual(str(article.parent_id), self.collection.id)

    def test_add_article_to_section(self):
        self.collection = create_help_center_collection(intercom, get_timestamp())
        section = create_help_center_section(intercom, self.collection, get_timestamp())

        article = intercom.articles.find(id=self.article.id)
        article.parent_id = section.id
        article.parent_type = 'section'
        intercom.articles.save(article)
        article = intercom.articles.find(id=self.article.id)
        self.assertEqual(str(article.parent_id), section.id)
