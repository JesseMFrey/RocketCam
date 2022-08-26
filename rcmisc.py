#functions used for system status

import humanize

from datetime import timedelta

def human_readable_size(size, decimal_places=2):
    for unit in ['B','kB','MB','GB','TB']:
        if size < 1024.0:
            break
        size /= 1024.0
    return f"{size:.{decimal_places}f} {unit}"

def human_readable_frequency(freq):
    step = 1e3
    for unit in ['MHz','GHz','THz']:
        if freq < step:
            break
        freq /= step
    return f"{freq:.{0}f} {unit}"

def get_uptime():
    #get uptime from proc
    with open('/proc/uptime','r') as f:
        #read file and convert to float
        uptime_s = float(f.readline().split()[0])

    uptime_str = humanize.naturaltime(timedelta(seconds=uptime_s))

    uptime_str = uptime_str.removesuffix(' ago')

    return uptime_str

