from message_type import MessageType
from terminal_colors import TerminalColors


class WarningMessage(MessageType):
    def get_name(self):
        return "WARNING"

    def get_color_code(self):
        return TerminalColors.WARNING
