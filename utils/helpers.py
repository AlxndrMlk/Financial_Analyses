from datetime import datetime as dt

def periods(start, end):
    start = start.split('-')
    end   = end.split('-')
    return dt(int(start[0]), int(start[1]), int(start[2])), dt(int(end[0]), int(end[1]), int(end[2]))