#  		databasemanager.py			Nov 15, 2024
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

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from config import db_conn_pool


class DatabaseManager:
    _engine = None

    @classmethod
    def _create_engine(cls):
        cls._engine = create_engine(f'mysql://{db_conn_pool['user']}:{db_conn_pool['password']}@{
            db_conn_pool['host']}:{db_conn_pool['port']}/{db_conn_pool['database']}',
            pool_size=db_conn_pool['pool_size'], max_overflow=db_conn_pool['max_overflow'],
            echo_pool=False)

    @classmethod
    def get_session(cls):
        if cls._engine is None:
            cls._create_engine()
        return Session(cls._engine)
