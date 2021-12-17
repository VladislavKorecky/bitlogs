"""
This module allows you to easily create logs for your code.

Example:
    from pylogs import Logger
    from pylogs.message_types.critical_message import CriticalMessage


    def add(a, b):
        if (not isinstance(a, float)) or (not isinstance(a, float)):
            Logger.log(CriticalMessage(), "Syntax error on line x")
            raise TypeError("A and B have to be of the type float.")
        return a + b
"""


from message_type import MessageType
from terminal_colors import TerminalColors


class Logger:
    @staticmethod
    def get_message(message_type: MessageType, text: str):
        """
        Return log message.

        Args:
            message_type (MessageType): Type of the message.
            text (str): Content of the message.

        Returns:
            str: Log message
        """

        return f"{message_type.get_color_code()}[{message_type.get_name()}] {TerminalColors.ENDC}{text}"

    @staticmethod
    def log(message_type: MessageType, text: str):
        """
        Print log message.

        Args:
            message_type (MessageType): Type of the message.
            text (str): Content of the message.
        """

        print(Logger.get_message(message_type, text))

    @staticmethod
    def log_to_file(message_type: MessageType, text: str, filename: str):
        """
        Print (append) log message to a file.

        Args:
            message_type (MessageType): Type of the message.
            text (str): Content of the message.
            filename (str): Name of the file.
        """

        #
        message = Logger.get_message(message_type, text)
        with open(filename, "a") as f:
            f.write(f"{message}\n")
