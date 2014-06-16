import pytest

import tests

import verzamelend


from collections import namedtuple

from tests import MockConfig


ConfigurationItem = namedtuple('ConfigurationItem', 'key value')


class GetBoolTestCase(tests.BaseTestCase):

    def setUp(self):
        item1 = ConfigurationItem('key1', True)
        item2 = ConfigurationItem('key2', False)
        item3 = ConfigurationItem('key3', 'true')
        item4 = ConfigurationItem('key4', 'false')
        mock_config = MockConfig([item1, item2, item3, item4])
        self.config = verzamelend.Configuration(mock_config)

    def test(self):
        self.assertTrue(self.config.getBool('key1'))
        self.assertFalse(self.config.getBool('key2'))
        self.assertTrue(self.config.getBool('key3'))
        self.assertFalse(self.config.getBool('key4'))


class GetIntTestCase(tests.BaseTestCase):

    def setUp(self):
        item1 = ConfigurationItem('key1', 1)
        item2 = ConfigurationItem('key2', '2')
        mock_config = MockConfig([item1, item2])
        self.config = verzamelend.Configuration(mock_config)

    def test(self):
        self.assertEquals(self.config.getInt('key1'), 1)
        self.assertEquals(self.config.getInt('key2'), 2)


class GetStrTestCase(tests.BaseTestCase):

    def setUp(self):
        item1 = ConfigurationItem('key1', 1)
        item2 = ConfigurationItem('key2', '2')
        mock_config = MockConfig([item1, item2])
        self.config = verzamelend.Configuration(mock_config)

    def test(self):
        self.assertEquals(self.config.getStr('key1'), '1')
        self.assertEquals(self.config.getStr('key2'), '2')


class GetValueTestCase(tests.BaseTestCase):

    def setUp(self):
        self.parameter = 'key1'
        item1 = ConfigurationItem('key1', [1, 3])
        mock_config = MockConfig([item1])
        self.config = verzamelend.Configuration(mock_config)

    def test_get_value_from_list(self):
        self.assertEquals(1, self.config.getValue(self.parameter, 1))
        self.assertEquals(3, self.config.getValue(self.parameter, 2))

    def test_invalid_parameter(self):
        with pytest.raises(ValueError):
            self.config.getValue(None)

        with pytest.raises(KeyError):
            self.config.getValue('unknown')

    def test_invalid_position(self):
        with pytest.raises(ValueError):
            self.config.getValue(parameter=self.parameter, position=-1)

        with pytest.raises(IndexError):
            self.config.getValue(parameter=self.parameter, position=3)
