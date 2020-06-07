'''
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
'''
def make_readable(seconds):
    ss=seconds % 60
    minutes=seconds // 60
    mm=minutes % 60
    hr=minutes //60
    print ("{:02}:{:02}:{:02}".format(hr,mm,ss))

make_readable(60)
make_readable(5)
make_readable(60)
make_readable(86399)
make_readable(359999)

