from message_type import MessageType
from terminal_colors import TerminalColors


class ErrorMessage(MessageType):
    def get_name(self):
        return "ERROR"

    def get_color_code(self):
        return TerminalColors.FAIL
