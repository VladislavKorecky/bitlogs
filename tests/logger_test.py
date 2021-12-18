from unittest import TestCase

from message_types.debug_message import DebugMessage
from message_types.info_message import InfoMessage
from message_types.warning_message import WarningMessage
from message_types.error_message import ErrorMessage
from message_types.critical_message import CriticalMessage

from logger import Logger

from os.path import exists
from os import remove


class LoggerTest(TestCase):
    def test_get_message(self):
        self.assertEqual(Logger.get_message(DebugMessage(), "The code got here"),
                         "\033[92m[DEBUG] \033[0mThe code got here")
        self.assertEqual(Logger.get_message(InfoMessage(), "Initializing..."),
                         "\033[94m[INFO] \033[0mInitializing...")
        self.assertEqual(Logger.get_message(WarningMessage(), "Module x is deprecated"),
                         "\033[93m[WARNING] \033[0mModule x is deprecated")
        self.assertEqual(Logger.get_message(ErrorMessage(), "User connection ended unexpectedly"),
                         "\033[91m[ERROR] \033[0mUser connection ended unexpectedly")
        self.assertEqual(Logger.get_message(CriticalMessage(), "Cannot divide by 0"),
                         "\033[91m[CRITICAL] \033[0mCannot divide by 0")

    def test_log(self):
        Logger.log(DebugMessage(), "The code got here")
        Logger.log(InfoMessage(), "Initializing...")
        Logger.log(WarningMessage(), "Module x is deprecated")
        Logger.log(ErrorMessage(), "User connection ended unexpectedly")
        Logger.log(CriticalMessage(), "Syntax error on line x")

    def test_log_to_file(self):
        if exists("test.bitlog"):
            remove("test.bitlog")

        Logger.log_to_file(DebugMessage(), "Hello world!", "test.bitlog")
