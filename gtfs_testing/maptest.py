
import gtfs_testing.gtfs as gtfs, folium, gtfs_testing.color_list as color_list, random

m = folium.Map(location=[37.389951149, -121.98964476585], 
    tiles='cartodbpositron', zoom_start=10
    )

shapes_raw = open("shapes.txt").read()
shapes = gtfs.convert_shape_gtfs_to_shape(shapes_raw)
shape_ids = sorted([*set([x.shape_id for x in shapes])])
shape_ids.pop(shape_ids.index("p_1425796"))
shape_ids.pop(shape_ids.index("p_1425704"))

stops_raw = open("stops.txt").read()
stops = gtfs.convert_stop_gtfs_to_stop(stops_raw)
for stop in stops:
    print(f"'{stop.stop_id}'")
    if stop.stop_id.isnumeric():
        stops.pop(stops.index(stop))


shape_ids = ["p_1425699"]
for shape_id in shape_ids:
    line = [x for x in shapes if x.shape_id == shape_id]
    line_coords = [(float(x.shape_pt_lat), float(x.shape_pt_lon)) for x in line]
    folium.PolyLine(line_coords, color="#dd1f29", tooltip=line[0].shape_id).add_to(m)

for stop in stops:
    folium.CircleMarker(
        location=[float(stop.stop_lat), float(stop.stop_lon)],
        radius=5,
        popup=stop.stop_name,
        color="#000000",
        fill=True,
        fill_color="#dd1f29",
    ).add_to(m)


m.save("index.html")
# ones that are bad: 1425796, 1425704
# good but not 1277432
# 1277433