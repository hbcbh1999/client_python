from ..resource import Resource
from .preference import Preference
from .schedule_shift import ScheduleShift
from .schedule_timeclock import ScheduleTimeclock


class Schedule(Resource):
    PATH = "organizations/{organization_id}/locations/{location_id}/roles/{role_id}/schedules/{schedule_id}"
    ID_NAME = "schedule_id"

    def get_preferences(self, **kwargs):
        return Preference.get_all(parent=self, **kwargs)

    def get_preference(self, id):
        """ Get a worker's preference for a given week"""
        return Preference.get(parent=self, id=id)

    def create_preference(self, **kwargs):
        return Preference.create(parent=self, **kwargs)

    def get_schedule_shifts(self, **kwargs):
        return ScheduleShift.get_all(parent=self, **kwargs)

    def get_schedule_timeclocks(self, **kwargs):
        return ScheduleTimeclock.get_all(parent=self, **kwargs)
