from enum import Enum
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_LOCATION = os.path.join(ROOT_DIR, "data/tagcounter.db")
LOG_LOCATION = os.path.join(ROOT_DIR, "data/log.txt")
PROMPT_LOCATION = os.path.join(ROOT_DIR, "data/prompt.txt")


class BadResultException(Exception):

    def __init__(self, public_msg="", debug_msg=""):
        super().__init__(public_msg)
        self.public_message = public_msg
        self.debug_message = debug_msg

    def get_public_message(self):
        return self.public_message

    def get_debug_message(self):
        return self.debug_message


class TagMethod(Enum):
    GET = 1
    VIEW = 2