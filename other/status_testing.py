
import discord
from zone import Zone_1, Zone_2, Zone_3, Zone_4, Zone_5, Zone_6


status_embed = discord.Embed(
    title="Caltrain Status"
)

def zone_txt(zone):
    z = ""
    # Structure: <emoji of train type> <Limiteds> <Name in bold>: <Events>
    for station in zone.stations:
        s = ""
        if station.is_baby_bullet_stop:
            s += "🔴 "
        if station.is_reduced_hours:
            s += "🔵 "
        if station.is_limited_stop != []:
            s += "🟡 " if s == "" else ""
            s += f"{str(station.is_limited_stop)} "
        else:
            s += "⚪ "

        s += f"**{station.name}**: Nothing!"
        s += "\n\n"
        z += s
    return z


status_embed.add_field(name="Zone 1", value=zone_txt(Zone_1))
status_embed.add_field(name="Zone 2", value=zone_txt(Zone_2))
status_embed.add_field(name="Zone 3", value=zone_txt(Zone_3))
status_embed.add_field(name="Zone 4", value=zone_txt(Zone_4))
status_embed.add_field(name="Zone 5", value=zone_txt(Zone_5))
status_embed.add_field(name="Zone 6", value=zone_txt(Zone_6))