"""
Cutplace API documentation
--------------------------

This is the API documentation for cutplace, a tool to validate that tabular and
flat data conform to an interface control document (ICD).

For more information about cutplace, visit https://github.com/roskakori/cutplace.
"""
# Copyright (C) 2009-2012 Thomas Aglassinger
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License
# for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import version

__version_info__ = (version.VERSION, version.RELEASE, version.REVISION)
__version__ = version.VERSION_NUMBER

DESCRIPTION = "validate data stored in CSV, PRN, ODS or Excel files"

