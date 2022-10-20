
class Station:
    """
    Caltrain Station object
    """
    def __init__(self, data):
        self.data = data
        self.single_tracking = None
        self._delays = None

    @property
    def name(self) -> str:
        """The name of the station"""
        return self.data['name']

    @property
    def abbrev(self) -> str:
        """Abbreviation of the station"""
        return self.data['abbrev']

    @property
    def zone(self) -> int:
        """Zone of the station"""
        return self.data['zone']

    @property
    def is_baby_bullet_stop(self) -> bool:
        """If the station is a baby bullet stop"""
        return self.data['is_baby_bullet_stop']

    @property
    def is_limited_stop(self):
        """If the station is a limited station"""
        return self.data['is_limited_stop']

    @property
    def is_transfer_stop(self) -> bool:
        """If the station has connections to other transits"""
        return self.data['is_transfer_stop']

    @property
    def is_reduced_hours(self):
        """If the station has reduced times"""
        return self.data['is_reduced_hours']


    @property
    def delays(self):
        """Delays for the station"""
        return self._delays

    