import mock

import pytest

import tests

import verzamelend


class RegisterCallbacksTestCase(tests.BaseTestCase):

    @mock.patch('verzamelend.collectd')
    def test(self, mock_collectd):
        """
        Test verzamelend.register_callbacks().
        """
        plugin = verzamelend.Plugin('test')
        verzamelend.register_callbacks(plugin)

        mock_collectd.register_config.called_once_with(plugin.configCallback)
        mock_collectd.register_flush(plugin.flushCallback)
        mock_collectd.register_init(plugin.initCallback)
        mock_collectd.register_log(plugin.logCallback)
        mock_collectd.register_notification(plugin.notificationCallback)
        mock_collectd.register_read(plugin.readCallback)
        mock_collectd.register_shutdown(plugin.shutdownCallback)
        mock_collectd.register_write(plugin.writeCallback)

    def test_none_plugin(self):
        """
        Test verzamelend.register_callbacks() when a None argument is passed.
        """
        with pytest.raises(ValueError):
            verzamelend.register_callbacks(None)
