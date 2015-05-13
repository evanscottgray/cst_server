import os.path
import ConfigParser

CONFIG_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                           'config.ini'))


def parse_config():
    config_parser = ConfigParser.RawConfigParser()
    config_parser.read(CONFIG_FILE)
    config = {}
    for name, value in config_parser.items('cst_server'):
        if ',' in value:
            config[name] = value.split(',')
        else:
            config[name] = value
    return config
