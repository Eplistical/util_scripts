#!/usr/bin/env python3

import sys
from datetime import datetime
from pprint import pprint


commitStamps = list()

for line in sys.stdin:
    line = line.replace('Date:', '').strip()
    if line:
        try:
            obj = datetime.strptime(line, '%a %b %d %H:%M:%S %Y')
            commitStamps.append(obj)
        except:
            pass

Ncommit = len(commitStamps)

# analyze
Ystat = {}
Mstat = [0] * 12
Hstat = [0] * 24
DoWstat = [0] * 7

for stamp in commitStamps:
    Ystat[stamp.year] = Ystat.get(stamp.year, 0) + 1
    Hstat[stamp.hour] += 1
    Mstat[stamp.month-1] += 1
    DoWstat[stamp.weekday()] += 1


print(f'{Ncommit} commits found')
print('Y percent')
pprint({ key : '%.1f' % (val / Ncommit * 100) + '%' for key, val in Ystat.items() })
print('M percent')
pprint({ key+1 : '%.1f' % (val / Ncommit * 100) + '%' for key, val in enumerate(Mstat) })
print('H percent')
pprint({ key : '%.1f' % (val / Ncommit * 100) + '%' for key, val in enumerate(Hstat) })
print('DoW percent')
pprint({ key+1 : '%.1f' % (val / Ncommit * 100) + '%' for key, val in enumerate(DoWstat) })
