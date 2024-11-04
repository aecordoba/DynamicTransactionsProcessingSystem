#  		processor.py			Oct 21, 2024
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
from services import databaseconnectionspool

logger = logging.getLogger(config.environment)


def process():
    logger.info('Processing...')
    pool = databaseconnectionspool.get_conn_pool()
    conn = pool.getconn()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM pg_catalog.pg_tables;')
    record = cursor.fetchall()

    print(record)
