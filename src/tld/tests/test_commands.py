# -*- coding: utf-8 -*-

import logging
import unittest

import shlex
import subprocess

from .base import log_info

__title__ = 'tld.tests.test_commands'
__author__ = 'Artur Barseghyan'
__copyright__ = '2013-2019 Artur Barseghyan'
__license__ = 'MPL-1.1 OR GPL-2.0-only OR LGPL-2.0-or-later'
__all__ = ('TestCommands',)

LOGGER = logging.getLogger(__name__)


class TestCommands(unittest.TestCase):
    """Tld commands tests."""

    def setUp(self):
        """Set up."""

    @log_info
    def test_1_update_tld_names_command(self):
        """Test updating the tld names (re-fetch mozilla source)."""
        res = subprocess.check_output(shlex.split('update-tld-names')).strip()
        self.assertEqual(res, b'True')
        return res


if __name__ == '__main__':
    unittest.main()
