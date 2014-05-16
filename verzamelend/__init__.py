"""
.. module:: verzamelend
    :platform: Unix
    :synopsis: Verzamelend package.

.. moduleauthor:: Pedro Salgado <steenzout@ymail.com>
"""


from __future__ import absolute_import


import collectd

import logging


LOGGER = logging.getLogger(__name__)

TYPE_ABSOLUTE = 'absolute'
TYPE_COUNTER = 'counter'
TYPE_DERIVE = 'derive'
TYPE_GAUGE = 'gauge'


def register_callbacks(plugin):
    """
    Registers all Collectd callbacks for the given plugin.

    This method will look for the following static methods to register callbacks:
    - configCallback() for register_config()
    - flushCallback() for register_flush
    - initCallback() for register_init()
    - logCallback() for register_log()
    - notificationCallback() for register_notification()
    - readCallback() for register_read()
    - shutdownCallback() for register_shutdown()
    - writeCallback() for register_write()

    :param plugin: the plugin instance which have the callbacks defined.
    :type plugin: object (verzamelend.Plugin)
    """
    if plugin is None:
        error_message = 'register_callbacks() plugin argument is None!'
        LOGGER.error(error_message)
        raise ValueError(error_message)

    LOGGER.info('register_callbacks for plugin %s' % plugin.name)
    collectd.register_config(plugin.configCallback)
    collectd.register_flush(plugin.flushCallback())
    collectd.register_init(plugin.initCallback())
    collectd.register_log(plugin.logCallback())
    collectd.register_notification(plugin.notificationCallback())
    collectd.register_read(plugin.readCallback())
    collectd.register_shutdown(plugin.shutdownCallback())
    collectd.register_write(plugin.writeCallback())


class Configuration:
    """
    Class to hold Collectd plugin configuration.
    """

    LOGGER = None

    def __init__(self, config):
        """
        Initializes a Configuration instance.

        :param config: the Collectd configuration for this plugin.
        :type config: object (Config)
        """
        self.values = dict([(node.key, node.value) for node in config.children])

    def getBool(self, parameter, position=1):
        """
        Returns the boolean value of the given parameter.

        :param parameter: the configuration parameter.
        :type parameter: str
        :param position: if parameter values are a list, the position of the value being retrieved.
        :type position: int
        """
        value = self.getValue(parameter, position)
        if isinstance(value, bool):
            return value

        if value is not None and isinstance(value, basestring) and value.upper() == 'TRUE':
            return True
        else:
            return False

    def getInt(self, parameter, position=1):
        """
        Returns the integer value of the given parameter.

        :param parameter: the configuration parameter.
        :type parameter: str
        :param position: if parameter values are a list, the position of the value being retrieved.
        :type position: int
        """
        return int(self.getValue(parameter, position))

    def getStr(self, parameter, position=1):
        """
        Returns the string value of the given parameter.

        :param parameter: the configuration parameter.
        :type parameter: str
        :param position: if parameter values are a list, the position of the value being retrieved.
        :type position: int
        """
        value = self.getValue(parameter, position)
        if isinstance(value, basestring):
            return value
        else:
            return str(value)

    def getValue(self, parameter, position=None):
        """
        Returns the value of the given parameter.

        :param parameter: the configuration parameter.
        :type parameter: str
        :param position: if parameter values are a list, the position of the value being retrieved
                         (1 means 1st element on the list of values).
        :type position: int
        """
        if parameter is None:
            error_message = 'getValue() parameter argument is None!'
            Configuration.__logger.error(error_message)
            raise ValueError(error_message)

        if position is None or position <= 0:
            error_message = 'getValue() position argument %s must be a positive integer!'
            Configuration.__logger.error(error_message, position)
            raise ValueError(error_message % position)

        if position is None:
            self.values[parameter][position - 1]
        else:
            return self.values[parameter]

Configuration.LOGGER = logging.getLogger('%s.%s' % Configuration.__module__, Configuration.__name__)


class Plugin:
    """
    Class to build Collectd plugins.
    """

    LOGGER = None

    def __init__(self, name):
        """
        Constructs a Plugin instance.

        :param name: the plugin name.
        :type name: str
        """
        self.name = name

    @staticmethod
    def configCallback(config):
        """
        Plugin callback for the configuration event.

        :param config: the Collectd configuration for this plugin.
        :type config: object (Config)
        """
        __logger.info('configCallback()')
        configuration = Configuration(config)

    @staticmethod
    def initCallback():
        """
        Plugin callback for the init event.
        """
        __logger.info('initCallback()')

    @staticmethod
    def flushCallback():
        """
        Plugin callback for flush events.
        """
        __logger.info('flushCallback()')

    @staticmethod
    def logCallback(level, message):
        """
        Plugin callback for log events.

        :param level: the severity level of the message.
        :param message: the message to be sent to the log.
        :type message: str
        """
        __logger.info('logCallback()')

    @staticmethod
    def notificationCallback(notification):
        """
        Plugin callback for notification events.

        :param notification: the Collectd notification.
        :type notification: object (Notification)
        """
        __logger.info('notificationCallback()')

    @staticmethod
    def readCallback(data=None):
        """
        Plugin callback for read events.
        """
        __logger.info('readCallback()')

    @staticmethod
    def shutdownCallback():
        """
        Plugin callback for the shutdown event.
        """
        __logger.info('shutdownCallback()')

    @staticmethod
    def writeCallback(measurements, data=None):
        """
        Plugin callback for write events.
        """
        __logger.info('writeCallback()')

Plugin.LOGGER = logging.getLogger('%s.%s' % Plugin.__module__, Plugin.__name__)
