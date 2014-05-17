import verzamelend.config

import mock

import pytest

import unittest


from verzamelend.config import DEFAULT_CONFIG_FILE, Cache


class LoadConfigurationTestCase(unittest.TestCase):
    """
    Tests for the verzamelend.config.load_configuration() function.
    """

    def setUp(self):
        verzamelend.config.reset()

        # mock of logging.RootLogger
        self.patch_get_logger = mock.patch('verzamelend.config.logging.getLogger', autospec=True)
        self.mock_get_logger = self.patch_get_logger.start()

        self.patch_root_logger = mock.patch('verzamelend.config.logging.RootLogger', autospec=True)
        self.mock_root_logger = self.patch_root_logger.start()
        self.mock_get_logger.return_value = self.mock_root_logger

        self.patch_path_exists = mock.patch('os.path', autospec=True)
        self.mock_path = self.patch_path_exists.start()

        self.patch_config_read = mock.patch('verzamelend.config.ConfigParser.read')
        self.mock_read = self.patch_config_read.start()

    def tearDown(self):
        self.patch_get_logger.stop()
        self.patch_root_logger.stop()
        self.patch_path_exists.stop()
        self.patch_config_read.stop()

    def test(self):
        """
        Test verzamelend.config.load_configuration() when configuration file exists.
        """
        self.mock_path.exists.return_value = True
        self.mock_path.isfile.return_value = True
        self.mock_read.return_value = None

        verzamelend.config.load_configuration()

        self.mock_path.exists.assert_called_once_with(DEFAULT_CONFIG_FILE)
        self.mock_path.isfile.assert_called_once_with(DEFAULT_CONFIG_FILE)
        self.mock_read.assert_called_with(DEFAULT_CONFIG_FILE)

        self.assertTrue(self.mock_get_logger.called)
        self.mock_root_logger.info.assert_called_once_with(
            '%s configuration file was loaded.', DEFAULT_CONFIG_FILE)

    def test_nofile(self):
        """
        Test verzamelend.config.load_configuration() when the configuration file doesn't exist.
        """
        self.mock_path.exists.return_value = True
        self.mock_path.isfile.return_value = False
        self.mock_read.return_value = None

        with pytest.raises(ValueError):
            verzamelend.config.load_configuration()

        self.mock_path.exists.assert_called_once_with(DEFAULT_CONFIG_FILE)
        self.mock_path.isfile.assert_called_once_with(DEFAULT_CONFIG_FILE)

        self.assertFalse(self.mock_read.readConfig.called)

        self.assertTrue(self.mock_get_logger.called)
        self.mock_root_logger.error.assert_called_once_with(
            '%s configuration file does not exist!' % DEFAULT_CONFIG_FILE)

    def test_errors(self):
        """
        Test verzamelend.config.load_configuration() when errors are raised.
        """
        self.mock_path.exists.return_value = True
        self.mock_path.isfile.return_value = True
        self.mock_read.side_effect = ValueError(123)

        with pytest.raises(ValueError):
            verzamelend.config.load_configuration()

        self.mock_path.exists.assert_called_once_with(DEFAULT_CONFIG_FILE)
        self.mock_path.isfile.assert_called_once_with(DEFAULT_CONFIG_FILE)

        self.assertFalse(self.mock_read.readConfig.called)

        self.assertTrue(self.mock_get_logger.called)
        self.mock_root_logger.error.assert_called_once_with(
            'Failed to load configuration from %s!', DEFAULT_CONFIG_FILE)
        self.mock_root_logger.debug.assert_called_once_with(
            str(ValueError(123)), exc_info=True)


class GetTestCase(unittest.TestCase):
    """
    Tests for the verzamelend.config.get() function.
    """

    def setUp(self):
        verzamelend.config.reset()

    @mock.patch('verzamelend.config.load_configuration', autospec=True)
    def test(self, mock_load):
        """
        Tests verzamelend.config.get() when no settings have been loaded.
        """
        default = {'key1': 'value1'}
        mock_load.return_value = default

        self.assertEquals(default, verzamelend.config.get())
        mock_load.assert_called_once_with()

    @mock.patch('verzamelend.config.load_configuration', autospec=True)
    def test_with_preloaded_settings(self, mock_load):
        """
        Tests verzamelend.config.get() when settings have been loaded.
        """
        default = {'key2': 'value2'}
        Cache.SETTINGS = default

        self.assertEquals(default, verzamelend.config.get())
        self.assertFalse(mock_load.called)


class ResetTestCase(unittest.TestCase):
    """
    Tests for the verzamelend.config.reset() function.
    """

    def setUp(self):
        verzamelend.config.reset()

    def test(self):
        """
        Tests verzamelend.config.reset().
        """
        default = {'key2': 'value2'}
        Cache.SETTINGS = default

        self.assertEquals(default, verzamelend.config.get())
        self.assertTrue(verzamelend.config.reset() is None)
        self.assertTrue(Cache.SETTINGS is None)
