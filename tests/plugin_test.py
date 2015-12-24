import logging

import mock

import tests


from collectdbit import verzamelend

from collections import namedtuple

from tests import MockConfig


ConfigurationItem = namedtuple('ConfigurationItem', 'key value')


class PluginTestCase(tests.BaseTestCase):

    def setUp(self):

        item1 = ConfigurationItem('key1', True)
        self.config = MockConfig([item1])

    @mock.patch('collectdbit.verzamelend.Plugin.LOGGER')
    def test_config_callback(self, mock_logger):
        verzamelend.Plugin.configCallback(self.config)

        mock_logger.info.assert_called_once_with('configCallback()')
        self.assertEquals(verzamelend.Plugin.CONFIGURATION.values['key1'], True)

    @mock.patch('collectdbit.verzamelend.Plugin.LOGGER')
    def test_init_callback(self, mock_logger):
        verzamelend.Plugin.initCallback()

        mock_logger.info.assert_called_once_with('initCallback()')

    @mock.patch('collectdbit.verzamelend.Plugin.LOGGER')
    def test_flush_callback(self, mock_logger):
        verzamelend.Plugin.flushCallback()

        mock_logger.info.assert_called_once_with('flushCallback()')

    @mock.patch('collectdbit.verzamelend.Plugin.LOGGER')
    def test_log_callback(self, mock_logger):
        verzamelend.Plugin.logCallback(None, None)

        mock_logger.info.assert_called_once_with('logCallback()')

    @mock.patch('collectdbit.verzamelend.Plugin.LOGGER')
    def test_notification_callback(self, mock_logger):
        verzamelend.Plugin.notificationCallback(None)

        mock_logger.info.assert_called_once_with('notificationCallback()')

    @mock.patch('collectdbit.verzamelend.Plugin.LOGGER')
    def test_read_callback(self, mock_logger):
        verzamelend.Plugin.readCallback(data=None)

        mock_logger.info.assert_called_once_with('readCallback()')

    @mock.patch('collectdbit.verzamelend.Plugin.LOGGER')
    def test_shutdown_callback(self, mock_logger):
        verzamelend.Plugin.shutdownCallback()

        mock_logger.info.assert_called_once_with('shutdownCallback()')

    @mock.patch('collectdbit.verzamelend.Plugin.LOGGER')
    def test_write_callback(self, mock_logger):
        verzamelend.Plugin.writeCallback(None, data=None)

        mock_logger.info.assert_called_once_with('writeCallback()')


class TestPlugin(verzamelend.Plugin):
    """
    A test plugin implementation.
    """

    CONFIGURATION = {}
    NAME = 'TestPlugin'

    def __init__(self):
        """
        Constructs a Plugin instance.
        """
        super(TestPlugin, self).__init__(TestPlugin.NAME)

TestPlugin.LOGGER = logging.getLogger(TestPlugin.__class__.__name__)


class TestPluginTestCase(tests.BaseTestCase):
    """
    Test cases for the test plugin implementation.
    """

    def setUp(self):
        item1 = ConfigurationItem('key1', True)
        self.config = MockConfig([item1])

    @mock.patch('tests.plugin_test.TestPlugin', autoSpec=True)
    # @mock.patch('collectdbit.verzamelend.collectd')
    def test_config_callback(self, mock_plugin):
        verzamelend.register_callbacks(mock_plugin)

        mock_plugin.LOGGER.info.assert_called_once_with('configCallback()')
        self.assertEquals(TestPlugin.CONFIGURATION.values['key1'], True)
