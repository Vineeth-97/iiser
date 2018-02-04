s = int(input("Enter number of seconds : "))

temp = s

days = int(s/86400)
s = s - days*86400

hrs = int(s/3600)
s = s - hrs*3600

mins = int(s/60)
s = s - mins*60

secs = int(s)

print('{:d} seconds are equivalent to : {:d} days {:d} hours {:d} minutes and {:d} seconds'.format(
    temp, days, hrs, mins, secs))
