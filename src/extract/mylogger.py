import os
import sys
from datetime import datetime

class Logger:
    def __init__(self, script_name=None):
        # Get project root (parent of 'src')
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        log_dir = os.path.join(project_root, "data", "log")
        os.makedirs(log_dir, exist_ok=True)
        if script_name is None:
            script_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = os.path.join(log_dir, f"{script_name}_{timestamp}.log")
        self.terminal = sys.stdout
        self.log = open(log_file, "a", encoding="utf-8")
        sys.stdout = self

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
        self.log.flush()

    def flush(self):
        self.terminal.flush()
        self.log.flush()

    def close(self):
        sys.stdout = self.terminal
        self.log.close()