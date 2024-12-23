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
from model.jobstatus import JobStatusService


logger = logging.getLogger(config.environment)


def config_status():
    job_status_list = JobStatusService().get_job_status_list()
    config.job_status = {n: i for (i, n) in job_status_list}
    logger.debug('Loaded {0} job status.'.format(len(config.job_status)))
    print(config.job_status)
