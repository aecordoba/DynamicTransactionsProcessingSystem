#  		databaseconnectionspool.py			Nov 1, 2024
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

import config
from mysql.connector.pooling import MySQLConnectionPool


class DatabaseManager:
    _conn_pool = None

    @classmethod
    def _create_pool(cls):
        cls._conn_pool = MySQLConnectionPool(**config.db_conn_pool)

    @classmethod
    def _get_conn(cls):
        if cls._conn_pool is None:
            cls._create_pool()
        return cls._conn_pool.get_connection()

    @classmethod
    def _close(cls, conn, cursor):
        cursor.close()
        conn.close()

    @classmethod
    def execute(cls, query, args=None, commit=False):
        conn = cls._get_conn()
        cursor = conn.cursor()
        if args:
            cursor.execute(query, args)
        else:
            cursor.execute(query)
        if commit is True:
            conn.commit()
            cls._close(conn, cursor)
            return None
        else:
            result = cursor.fetchall()
            cls._close(conn, cursor)
            return result

    @classmethod
    def execute_many(cls, sql, args, commit=False):
        conn = cls._get_conn()
        cursor = conn.cursor()
        cursor.executemany(sql, args)
        if commit is True:
            conn.commit()
            cls._close(conn, cursor)
            return None
        else:
            result = cursor.fetchall()
            cls._close(conn, cursor)
            return result
