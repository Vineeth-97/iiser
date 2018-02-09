print('+-----------+----------+')
print('|{:^11s}|{:^10s}|'.format("Farenheit", "Celsius"))
print('+-----------+----------+')

for f in range(0, 110, 10):
    print('|{:^11d}|{: 7.2f}   |'.format(f, (f-32)*(5/9)))
    print('+-----------+----------+')
