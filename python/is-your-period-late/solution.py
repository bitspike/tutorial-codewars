import datetime

def period_is_late(last,today,cycle_length):
    return last + datetime.timedelta(days=cycle_length) < today