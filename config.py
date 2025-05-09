import configparser

_config = configparser.ConfigParser()
_config.read("config.ini")

col_terminal = int(_config["Terminal"]["columns"])
lin_terminal = int(_config["Terminal"]["lines"])
lin_message = int(_config["Terminal"]["message_line"])
col_message = int(_config["Terminal"]["message_col"])
size_message_lin = int(_config["Terminal"]["size_message_lin"])