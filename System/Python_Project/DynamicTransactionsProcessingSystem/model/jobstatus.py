#  		jobstatus.py			Nov 15, 2024
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

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from sqlalchemy import String, select

from services.databasemanager import DatabaseManager


class Base(DeclarativeBase):
    pass


class JobStatus(Base):
    __tablename__ = "Job_Status"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(15))

    # def __repr__(self) -> str:
    #     return f"JobStatus(id={self.id!r}, name={self.name!r})"


class JobStatusService:
    def __init__(self):
        self.session = DatabaseManager.get_session()

    def get_job_status_list(self):
        job_status_list = []
        stmt = select(JobStatus)
        for job_status in self.session.execute(stmt):
            job_status_list.append((job_status.JobStatus.id, job_status.JobStatus.name))
        return job_status_list
    