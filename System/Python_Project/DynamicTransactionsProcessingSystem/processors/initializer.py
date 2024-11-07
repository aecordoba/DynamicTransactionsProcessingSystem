#  		initializer.py			Nov 5, 2024
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
import logging
import config
from services.databaseconnectionspool import DatabaseManager

logger = logging.getLogger(config.environment)


def config_status():
    cursor = DatabaseManager.get_conn().cursor()
    cursor.execute('SELECT * FROM Job_Status;')
    record = cursor.fetchall()

    logger.debug('Loaded {0} job status.'.format(len(record)))
    config.job_status = {n: i for (i, n) in record}
    print(config.job_status)
