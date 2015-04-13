__author__ = 'mosassy'
def sleep_in(weekday, vacation):
    if vacation or not weekday:
        return True
    else:
        return False
print sleep_in(False, False)
print sleep_in(True, False)
print sleep_in(False, True)

