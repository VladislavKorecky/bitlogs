from message_type import MessageType
from terminal_colors import TerminalColors


class CriticalMessage(MessageType):
    def get_name(self):
        return "CRITICAL"

    def get_color_code(self):
        return TerminalColors.FAIL
