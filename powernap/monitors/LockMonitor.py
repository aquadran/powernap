#    powernapd plugin - Monitors process file lock
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3 of the License.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os, re, commands
from logging import error, debug, info, warn

class LockMonitor():

    # Initialise
    def __init__(self, config):
        self._type = config['monitor']
        self._name = config['name']
        self._absent_seconds = 0
        self._lock = config['lock']

    def active(self):
	if not os.path.exists(self._lock):
		return False
	file_lock = open(self._lock, "r")
	state = file_lock.read(1)
	file_lock.close()
        if state == 'y':
		return True
	else:
		return False

    def start(self):
        pass

# ###########################################################################
# Editor directives
# ###########################################################################

# vim:sts=4:ts=4:sw=4:et
