#!/usr/bin/python3
#  		main.py			Oct 18, 2024
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

import logging.config
import yaml

with open('config/logging.yaml', 'r') as f:
    config = yaml.safe_load(f)

# Configure logging
logging.config.dictConfig(config)

# Create a logger
logger = logging.getLogger(__name__)


def run():
    logger.info('Dynamic Transactions Processing System is starting...')


if __name__ == '__main__':
    run()
