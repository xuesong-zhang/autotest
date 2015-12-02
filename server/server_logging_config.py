try:
    import autotest.common as common  # pylint: disable=W0611
except ImportError:
    import common  # pylint: disable=W0611
import logging
import os
from autotest.client.shared import logging_config


class ServerLoggingConfig(logging_config.LoggingConfig):

    def add_debug_file_handlers(self, log_dir, log_name=None):
        if not log_name:
            log_name = 'autoserv'
        self._add_file_handlers_for_all_levels(log_dir, log_name)

    def configure_logging(self, results_dir=None, use_console=True,
                          verbose=False, no_console_prefix=False):
        if no_console_prefix:
            self.console_formatter = logging.Formatter()

        super(ServerLoggingConfig, self).configure_logging(use_console, verbose)

        if results_dir:
            log_dir = os.path.join(results_dir, 'debug')
            if not os.path.exists(log_dir):
                os.mkdir(log_dir)
            self.add_debug_file_handlers(log_dir)
