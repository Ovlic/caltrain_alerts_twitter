
import stations

class Zone:
    def __init__(self, stations):
        self._stations = stations

    @property
    def stations(self):
        return self._stations


Zone_1 = Zone(stations=[stations.San_Francisco, stations.Twenty_Second_Street, stations.Bayshore, stations.South_San_Francisco, stations.San_Bruno,])
Zone_2 = Zone(stations=[stations.Milbrae, stations.Broadway, stations.Burlingame, stations.San_Mateo, stations.Hayward_Park, stations.Hillsdale, stations.Belmont, stations.San_Carlos, stations.Redwood_City,])
Zone_3 = Zone(stations=[stations.Menlo_Park, stations.Palo_Alto, stations.Stanford, stations.California_Avenue, stations.San_Antonio, stations.Mountain_View, stations.Sunnyvale,])
Zone_4 = Zone(stations=[stations.Lawrence, stations.Santa_Clara, stations.College_Park, stations.San_Jose_Diridon, stations.Tamien,])
Zone_5 = Zone(stations=[stations.Capitol, stations.Blossom_Hill,])
Zone_6 = Zone(stations=[stations.Morgan_Hill, stations.San_Martin, stations.Gilroy,])