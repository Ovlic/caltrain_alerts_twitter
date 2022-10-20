from stations_base import Station

stations_raw = {
   "": {
      "abbrev": "",
      "zone": 0,
      "is_baby_bullet_stop": False,
      "is_limited_stop": [
         
      ],
      "is_transfer_stop": False,
      "is_reduced_hours": False,
      "name": ""
   },
   "San Francisco": {
      "abbrev": "SFK",
      "zone": 1,
      "is_baby_bullet_stop": True,
      "is_limited_stop": [
         3,
         4,
         5
      ],
      "is_transfer_stop": True,
      "is_reduced_hours": False,
      "name": "San Francisco"
   },
   "Twenty Second Street": {
      "abbrev": "TWE",
      "zone": 1,
      "is_baby_bullet_stop": True,
      "is_limited_stop": [
         4,
         5
      ],
      "is_transfer_stop": False,
      "is_reduced_hours": False,
      "name": "Twenty Second Street"
   },
   "Bayshore": {
      "abbrev": "BAY",
      "zone": 1,
      "is_baby_bullet_stop": False,
      "is_limited_stop": [
         
      ],
      "is_transfer_stop": False,
      "is_reduced_hours": False,
      "name": "Bayshore"
   },
   "South San Francisco": {
      "abbrev": "SSF",
      "zone": 1,
      "is_baby_bullet_stop": False,
      "is_limited_stop": [
         
      ],
      "is_transfer_stop": False,
      "is_reduced_hours": False,
      "name": "South San Francisco"
   },
   "San Bruno": {
      "abbrev": "SBR",
      "zone": 1,
      "is_baby_bullet_stop": False,
      "is_limited_stop": [
         4
      ],
      "is_transfer_stop": False,
      "is_reduced_hours": False,
      "name": "San Bruno"
   },
   "Milbrae": {
      "abbrev": "MIL",
      "zone": 2,
      "is_baby_bullet_stop": True,
      "is_limited_stop": [
         3,
         4,
         5
      ],
      "is_transfer_stop": True,
      "is_reduced_hours": False,
      "name": "Milbrae"
   },
   "Broadway": {
      "abbrev": "BWY",
      "zone": 2,
      "is_baby_bullet_stop": False,
      "is_limited_stop": [
         
      ],
      "is_transfer_stop": False,
      "is_reduced_hours": True,
      "name": "Broadway"
   },
   "Burlingame": {
      "abbrev": "BUR",
      "zone": 2,
      "is_baby_bullet_stop": False,
      "is_limited_stop": [
         4
      ],
      "is_transfer_stop": False,
      "is_reduced_hours": False,
      "name": "Burlingame"
   },
   "San Mateo": {
      "abbrev": "SMT",
      "zone": 2,
      "is_baby_bullet_stop": False,
      "is_limited_stop": [
         4,
         5
      ],
      "is_transfer_stop": False,
      "is_reduced_hours": False,
      "name": "San Mateo"
   },
   "Hayward Park": {
      "abbrev": "HPK",
      "zone": 2,
      "is_baby_bullet_stop": False,
      "is_limited_stop": [
         
      ],
      "is_transfer_stop": False,
      "is_reduced_hours": False,
      "name": "Hayward Park"
   },
   "Hillsdale": {
      "abbrev": "HIL",
      "zone": 2,
      "is_baby_bullet_stop": True,
      "is_limited_stop": [
         3,
         5
      ],
      "is_transfer_stop": False,
      "is_reduced_hours": False,
      "name": "Hillsdale"
   },
   "Belmont": {
      "abbrev": "BEL",
      "zone": 2,
      "is_baby_bullet_stop": False,
      "is_limited_stop": [
         3
      ],
      "is_transfer_stop": False,
      "is_reduced_hours": False,
      "name": "Belmont"
   },
   "San Carlos": {
      "abbrev": "SCS",
      "zone": 2,
      "is_baby_bullet_stop": False,
      "is_limited_stop": [
         4
      ],
      "is_transfer_stop": False,
      "is_reduced_hours": False,
      "name": "San Carlos"
   },
   "Redwood City": {
      "abbrev": "RWC",
      "zone": 2,
      "is_baby_bullet_stop": True,
      "is_limited_stop": [
         3,
         4,
         5
      ],
      "is_transfer_stop": False,
      "is_reduced_hours": False,
      "name": "Redwood City"
   },
   "Menlo Park": {
      "abbrev": "MPK",
      "zone": 3,
      "is_baby_bullet_stop": False,
      "is_limited_stop": [
         3,
         5
      ],
      "is_transfer_stop": False,
      "is_reduced_hours": False,
      "name": "Menlo Park"
   },
   "Palo Alto": {
      "abbrev": "PAL",
      "zone": 3,
      "is_baby_bullet_stop": True,
      "is_limited_stop": [
         3,
         4,
         5
      ],
      "is_transfer_stop": False,
      "is_reduced_hours": False,
      "name": "Palo Alto"
   },
   "Stanford": {
      "abbrev": "STF",
      "zone": 3,
      "is_baby_bullet_stop": False,
      "is_limited_stop": [
         
      ],
      "is_transfer_stop": False,
      "is_reduced_hours": True,
      "name": "Stanford"
   },
   "California Avenue": {
      "abbrev": "CAL",
      "zone": 3,
      "is_baby_bullet_stop": False,
      "is_limited_stop": [
         3
      ],
      "is_transfer_stop": False,
      "is_reduced_hours": False,
      "name": "California Avenue"
   },
   "San Antonio": {
      "abbrev": "SAT",
      "zone": 3,
      "is_baby_bullet_stop": False,
      "is_limited_stop": [
         3
      ],
      "is_transfer_stop": False,
      "is_reduced_hours": False,
      "name": "San Antonio"
   },
   "Mountain View": {
      "abbrev": "MVW",
      "zone": 3,
      "is_baby_bullet_stop": True,
      "is_limited_stop": [
         3,
         4,
         5
      ],
      "is_transfer_stop": True,
      "is_reduced_hours": False,
      "name": "Mountain View"
   },
   "Sunnyvale": {
      "abbrev": "SUN",
      "zone": 3,
      "is_baby_bullet_stop": False,
      "is_limited_stop": [
         3,
         4,
         5
      ],
      "is_transfer_stop": False,
      "is_reduced_hours": False,
      "name": "Sunnyvale"
   },
   "Lawrence": {
      "abbrev": "LAW",
      "zone": 4,
      "is_baby_bullet_stop": False,
      "is_limited_stop": [
         3
      ],
      "is_transfer_stop": False,
      "is_reduced_hours": False,
      "name": "Lawrence"
   },
   "Santa Clara": {
      "abbrev": "SCL",
      "zone": 4,
      "is_baby_bullet_stop": False,
      "is_limited_stop": [
         4,
         5
      ],
      "is_transfer_stop": True,
      "is_reduced_hours": False,
      "name": "Santa Clara"
   },
   "College Park": {
      "abbrev": "CPK",
      "zone": 4,
      "is_baby_bullet_stop": False,
      "is_limited_stop": [
         3,
         4
      ],
      "is_transfer_stop": False,
      "is_reduced_hours": True,
      "name": "College Park"
   },
   "San Jose Diridon": {
      "abbrev": "SJD",
      "zone": 4,
      "is_baby_bullet_stop": True,
      "is_limited_stop": [
         3,
         4,
         5
      ],
      "is_transfer_stop": True,
      "is_reduced_hours": False,
      "name": "San Jose Diridon"
   },
   "Tamien": {
      "abbrev": "TAM",
      "zone": 4,
      "is_baby_bullet_stop": False,
      "is_limited_stop": [
         3,
         4,
         5
      ],
      "is_transfer_stop": True,
      "is_reduced_hours": False,
      "name": "Tamien"
   },
   "Capitol": {
      "abbrev": "CAP",
      "zone": 5,
      "is_baby_bullet_stop": False,
      "is_limited_stop": [
         3,
         4
      ],
      "is_transfer_stop": False,
      "is_reduced_hours": False,
      "name": "Capitol"
   },
   "Blossom Hill": {
      "abbrev": "BHL",
      "zone": 5,
      "is_baby_bullet_stop": False,
      "is_limited_stop": [
         3,
         4
      ],
      "is_transfer_stop": False,
      "is_reduced_hours": False,
      "name": "Blossom Hill"
   },
   "Morgan Hill": {
      "abbrev": "MHL",
      "zone": 6,
      "is_baby_bullet_stop": False,
      "is_limited_stop": [
         3,
         4
      ],
      "is_transfer_stop": False,
      "is_reduced_hours": False,
      "name": "Morgan Hill"
   },
   "San Martin": {
      "abbrev": "SMR",
      "zone": 6,
      "is_baby_bullet_stop": False,
      "is_limited_stop": [
         3,
         4
      ],
      "is_transfer_stop": False,
      "is_reduced_hours": False,
      "name": "San Martin"
   },
   "Gilroy": {
      "abbrev": "CAP",
      "zone": 6,
      "is_baby_bullet_stop": False,
      "is_limited_stop": [
         3,
         4
      ],
      "is_transfer_stop": False,
      "is_reduced_hours": False,
      "name": "Gilroy"
   }
}

San_Francisco = Station(stations_raw['San Francisco'])
Twenty_Second_Street = Station(stations_raw['Twenty Second Street'])
Bayshore = Station(stations_raw['Bayshore'])
South_San_Francisco = Station(stations_raw['South San Francisco'])
San_Bruno = Station(stations_raw['San Bruno'])
Milbrae = Station(stations_raw['Milbrae'])
Broadway = Station(stations_raw['Broadway'])
Burlingame = Station(stations_raw['Burlingame'])
San_Mateo = Station(stations_raw['San Mateo'])
Hayward_Park = Station(stations_raw['Hayward Park'])
Hillsdale = Station(stations_raw['Hillsdale'])
Belmont = Station(stations_raw['Belmont'])
San_Carlos = Station(stations_raw['San Carlos'])
Redwood_City = Station(stations_raw['Redwood City'])
Menlo_Park = Station(stations_raw['Menlo Park'])
Palo_Alto = Station(stations_raw['Palo Alto'])
Stanford = Station(stations_raw['Stanford'])
California_Avenue = Station(stations_raw['California Avenue'])
San_Antonio = Station(stations_raw['San Antonio'])
Mountain_View = Station(stations_raw['Mountain View'])
Sunnyvale = Station(stations_raw['Sunnyvale'])
Lawrence = Station(stations_raw['Lawrence'])
Santa_Clara = Station(stations_raw['Santa Clara'])
College_Park = Station(stations_raw['College Park'])
San_Jose_Diridon = Station(stations_raw['San Jose Diridon'])
Tamien = Station(stations_raw['Tamien'])
Capitol = Station(stations_raw['Capitol'])
Blossom_Hill = Station(stations_raw['Blossom Hill'])
Morgan_Hill = Station(stations_raw['Morgan Hill'])
San_Martin = Station(stations_raw['San Martin'])
Gilroy = Station(stations_raw['Gilroy'])

Stations = {
   'San Francisco': San_Francisco,
   '22nd Street': Twenty_Second_Street,
   'Bayshore': Bayshore,
   'South San Francisco': South_San_Francisco,
   'San Bruno': San_Bruno,
   'Milbrae': Milbrae,
   'Broadway': Broadway,
   'Burlingame': Burlingame,
   'San Mateo': San_Mateo,
   'Hayward Park': Hayward_Park,
   'Hillsdale': Hillsdale,
   'Belmont': Belmont,
   'San Carlos': San_Carlos,
   'Redwood City': Redwood_City,
   'Menlo Park': Menlo_Park,
   'Palo Alto': Palo_Alto,
   'Stanford': Stanford,
   'California Avenue': California_Avenue,
   'San Antonio': San_Antonio,
   'Mountain View': Mountain_View,
   'Sunnyvale': Sunnyvale,
   'Lawrence': Lawrence,
   'Santa Clara': Santa_Clara,
   'College Park': College_Park,
   'San Jose Diridon': San_Jose_Diridon,
   'Tamien': Tamien,
   'Capitol': Capitol,
   'Blossom Hill': Blossom_Hill,
   'Morgan Hill': Morgan_Hill,
   'San Martin': San_Martin,
   'Gilroy': Gilroy,
}

def search_for_station_name(text: str):
   returned_stations = []
   for key in Stations:
      if Stations[key].name.lower() in text.lower():
         returned_stations.append(key)
      elif Stations[key].abbrev.lower() in text.lower():
         returned_stations.append(key)
      
   return returned_stations