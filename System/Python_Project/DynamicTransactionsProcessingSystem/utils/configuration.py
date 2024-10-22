#  		configuration.py			Oct 22, 2024
#  				Adrián E. Córdoba [software.dynamicmcs@gmail.com]
#
#  Copyright (C) 2024
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
import yaml

dtps_config = None

def config_setup():
    global dtps_config
    with open('config/dtps.yaml', 'r') as dtps_file:
        dtps_config = yaml.safe_load(dtps_file)

def get_config():
    if dtps_config is None:
        config_setup()
    return dtps_config

