
from datetime import datetime

date1 = "2026-01-01"
date2 = "2026-11-25"

d1 = datetime.strptime(date1, "%Y-%m-%d")
d2 = datetime.strptime(date2, "%Y-%m-%d")

difference = abs((d2 - d1).days)

print("Number of days:", difference)
