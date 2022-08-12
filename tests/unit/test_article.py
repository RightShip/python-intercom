# -*- coding: utf-8 -*-

import unittest

from intercom.client import Client
from mock import patch
from nose.tools import eq_
from nose.tools import istest
from tests.unit import test_article


class ArticleTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()

    @istest
    def it_gets_an_article(self):
        with patch.object(Client, 'get', return_value=test_article) as mock_method:  # noqa
            article = self.client.articles.find(title=test_article['title'])
            eq_(article.title, test_article['title'])
            mock_method.assert_called_once_with('/articles', {'title': test_article['title']})

    @istest
    def it_creates_an_article(self):
        with patch.object(Client, 'post', return_value=test_article) as mock_method:  # noqa
            article = self.client.articles.create(title=test_article['title'])
            eq_(article.title, test_article['title'])
            mock_method.assert_called_once_with('/articles/', {'title': test_article['title']})
