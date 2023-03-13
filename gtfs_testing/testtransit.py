
import gtfs_functions as gtfs
import folium

routes, stops, stop_times, trips, shapes, feed = gtfs.import_gtfs("Caltrain_GTFS.zip")


minlon, minlat, maxlon, maxlat = feed.stops.total_bounds
line_coordinates = [
    (minlat, minlon),
    (maxlat, maxlon),
]
print(line_coordinates)

cutoffs = [0,6,9,15,19,22,24]
line_freq = gtfs.lines_freq(stop_times, trips, shapes, routes, cutoffs = cutoffs)
stop_freq = gtfs.stops_freq(stop_times, stops, cutoffs = cutoffs)
#segments_gdf = gtfs.cut_gtfs(stop_times, stops, shapes)
#speeds = gtfs.speeds_from_gtfs(routes, stop_times, segments_gdf, cutoffs = list(range(24)))
#seg_freq = gtfs.segments_freq(segments_gdf, stop_times, routes, cutoffs = cutoffs)


def get_gdf(freq):
    condition_dir = freq.dir_id == 'Inbound'
    condition_window = freq.window == '6:00-9:00'
    return freq.loc[(condition_dir & condition_window),:].reset_index()

# Line frequencies
gdf = get_gdf(line_freq)

m = gtfs.map_gdf(
    gdf = gdf,
    variable = 'ntrips', 
    #colors = ["#d13870", "#e895b3" , '#55d992', '#3abe71', '#08955', '#066a40'],
    tooltip_var = ['route_name'],
    tooltip_labels = ['Route: '],
    breaks = [5, 10, 20, 50])

#m = folium.Map(location=[45.5236, -122.6750])
    
folium.PolyLine(line_coordinates, tooltip="Coast").add_to(m)

m.save("index.html")