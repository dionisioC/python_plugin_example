from configparser import ConfigParser
from importlib import import_module
from os import listdir
from sys import path
from plugins.plugin import Plugin


class Calculator(object):

    @staticmethod
    def __get_plugins():
        config_parser = ConfigParser()
        config_parser.read('properties.ini')
        plugin_path = config_parser.get("paths", "plugins")
        plugin_files = [plugin_file[:-3] for plugin_file in listdir(plugin_path) if plugin_file.endswith(".py")]
        path.insert(0, plugin_path)
        for plugin_file in plugin_files:
            import_module(plugin_file)

    def __register_plugin(self):
        for plugin in Plugin.__subclasses__():
            self.__operations[plugin.op] = plugin

    def __init__(self, num_1, num_2, op):
        self.__operations = {}
        self.__num_1 = num_1
        self.__num_2 = num_2
        self.__op = op
        self.__get_plugins()
        self.__register_plugin()

    def calc(self):
        try:
            return self.__operations[self.__op].calc(self.__num_1, self.__num_2)
        except KeyError:
            return "Operation not supported"
