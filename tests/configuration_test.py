import tests


from collections import namedtuple


ConfigurationItem = namedtuple('ConfigurationItem', 'key value')


class MockConfig(object):

    def __init__(self, children):
        self.children = children


class GetBoolTestCase(tests.BaseTestCase):

    def setUp(self):
        self.item1 = ConfigurationItem('key1', True)
        self.item2 = ConfigurationItem('key2', False)
        self.config = MockConfig([self.item1, self.item2])
