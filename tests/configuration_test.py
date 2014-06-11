import tests

import verzamelend


from collections import namedtuple


ConfigurationItem = namedtuple('ConfigurationItem', 'key value')


class MockConfig(object):

    def __init__(self, children):
        self.children = children


class GetBoolTestCase(tests.BaseTestCase):

    def setUp(self):
        self.item1 = ConfigurationItem('key1', True)
        self.item2 = ConfigurationItem('key2', False)
        self.item3 = ConfigurationItem('key3', 'true')
        self.item4 = ConfigurationItem('key4', 'false')
        self.config = MockConfig([self.item1, self.item2, self.item3, self.item4])

    def test(self):
        Config = verzamelend.Configuration(self.config)
        self.assertTrue(Config.getBool('key1'))
        self.assertFalse(Config.getBool('key2'))
        self.assertTrue(Config.getBool('key3'))
        self.assertFalse(Config.getBool('key4'))


class GetIntTestCase(tests.BaseTestCase):

    def setUp(self):
        self.item1 = ConfigurationItem('key1', 1)
        self.item2 = ConfigurationItem('key2', '2')
        self.config = MockConfig([self.item1, self.item2])

    def test(self):
        Config = verzamelend.Configuration(self.config)
        self.assertEquals(Config.getInt('key1'), 1)
        self.assertEquals(Config.getInt('key2'), 2)
