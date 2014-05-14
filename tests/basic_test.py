import tests


class ATestCase(tests.BaseTestCase):

    def test_logging_configuration_loaded(self):
        self.assertTrue(self.logger is not None)

    def test_configuration_loaded(self):
        self.assertTrue(self.configuration is not None)

    def test_configuration_contents(self):
        self.assertTrue('vermazelend' in self.configuration)
        self.assertTrue('key' in self.configuration['vermazelend'])
        self.assertEquals(self.configuration['vermazelend']['key'], 'value')
