"""
from datetime import datetime

text = "Single tracking at Sunnyvale and Lawrence until 3:45pm. Trains will board on northbound platform."


if "am" in text.lower() or "pm" in text.lower():
    # Time, not date
    date = datetime.now()
    if ":" in text:
        hours = int(text.split('until')[1].split(':')[0])
        if "pm" in text.lower():
            hours += 12
        mins = int(text.split(':')[1].split('am' if 'am' in text.lower() else 'pm')[0])
        new_period = date.replace(hour=hours, minute=mins).strftime('%Y-%m-%d-%H:%M')
        print(new_period)

text2 = "Single tracking at 22nd St and Bayshore beginning with NB407, all trains will board on southbound platform until 4pm."
date = datetime.now()
hours = int(text2.split('until')[1].split('.')[0].split('pm' if 'pm' in text2.lower() else 'am')[0])
if "pm" in text2.lower():
    hours += 12
new_period2 = date.replace(hour=hours, minute=00).strftime('%Y-%m-%d-%H:%M')
print(new_period2)"""

"""import requests
resp = requests.head("https://t.co/EW9KVx2yka")
print(resp.status_code)
print(resp.headers["Location"])"""

"""t = []
print("none" if t is None else "not none")
print("none" if t is [] else "not none")
print("none" if not t else "not none")"""

text = "southbound is in this text but not the opposite!"
print(text.replace("NBD", "northbound"))
text.replace("southbound", "haha")
print(text)