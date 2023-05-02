#!/usr/bin/python3

'''
Log Parsing
'''

import sys

status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

total_size = 0
count = 0

try:
    for line in sys.stdin:
        count += 1
        data = line.split()
        if len(data) > 2:
            status = data[-2]
            file_size = data[-1]
            if status in status_codes:
                status_codes[status] += 1
            total_size += int(file_size)
        if count == 10:
            print('File size: {}'.format(total_size))
            for key, value in sorted(status_codes.items()):
                if value > 0:
                    print('{}: {}'.format(key, value))
            count = 0
except KeyboardInterrupt:
    pass
finally:
    print('File size: {}'.format(total_size))
    for key, value in sorted(status_codes.items()):
        if value > 0:
            print('{}: {}'.format(key, value))
