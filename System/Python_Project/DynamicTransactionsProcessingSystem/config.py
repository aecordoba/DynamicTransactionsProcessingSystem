#  		config.py			Oct 23, 2024
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

environment = 'development'     # development | staging | production
logging = {
    'config_file': 'logging.yaml',
}
queues_size = {
    'created': 10,
    'initialized': 10,
    'executed': 10,
}
db_conn_pool = {
    'host': 'localhost',
    'port': 5432,
    'database': 'dtps',
    'user': 'dtpsapp',
    'password': 'dtpsapp123',
    'minconn': 2,
    'maxconn': 32
}
