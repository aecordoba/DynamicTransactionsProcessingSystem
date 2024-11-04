#  		tasks.py			Nov 1, 2024
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

from abc import ABC, abstractmethod


class Task(ABC):
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier

    @abstractmethod
    def initialize(self): pass

    @abstractmethod
    def execute(self): pass

    @abstractmethod
    def complete(self): pass


class Job:
    def __init__(self, identifier, task, data, status):
        self.identifier = identifier
        self.task = task
        self.data = data
        self.status = status
