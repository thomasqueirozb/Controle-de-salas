from datetime import time
import datetime

def time_in_range(times, x):
    '''Retorna se o tempo está ou não dentro de um determinado tempo'''

    start, end = times
    return start <= x <= end

def time_to_num(time):
    '''Converte o objeto time em número'''

    return time.hour + time.minute / 60 + time.second / 3600

def time_difference(time1,time2):
    '''Dá a diferença de tempo entre dois objetos time em outro objeto time'''

    new_time = abs(time_to_num(time2) - time_to_num(time1))
    h, ms = divmod(new_time, 1)
    m, s = divmod(ms*60, 1)
    return time(round(h),round(m),round(s*60))

# def time_difference_num(time1,time2):
#     '''Dá a diferença de tempo entre dois objetos time em um número'''
#
#     new_time = abs(time_to_num(time2) - time_to_num(time1))
#     return new_time


def passou(times, x):
    return x >= times[1]
