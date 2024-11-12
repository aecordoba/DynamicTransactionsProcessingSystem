#  		queuesmanager.py			Nov 12, 2024
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

from queue import Queue
import config


class QueueManager:
    def __init__(self):
        self.created_queue = Queue(config.queues_size['created'])
        self.initialized_queue = Queue(config.queues_size['initialized'])
        self.executed_queue = Queue(config.queues_size['executed'])

    def put_created_job(self, job):
        self.created_queue.put(job)

    def get_create_job(self):
        return self.created_queue.get()

    def put_initialized_job(self, job):
        self.initialized_queue.put(job)

    def get_initialized_job(self):
        return self.initialized_queue.get()

    def put_executed_job(self, job):
        self.executed_queue.put(job)

    def get_executed_job(self):
        return self.executed_queue.get()
