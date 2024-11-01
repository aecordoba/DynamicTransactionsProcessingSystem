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
import config
from processors import processor


def run():
    logger.info('Application is running in {0} mode.'.format(config.environment))
    processor.process()


if __name__ == '__main__':
    with open(config.logging['config_file'], 'r') as logging_file:
        logging_config = yaml.safe_load(logging_file)

    logging.config.dictConfig(logging_config)
    logger = logging.getLogger(config.environment)
    logger.info('Dynamic Transactions Processing System is starting...')

    run()
