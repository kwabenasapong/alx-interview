#!/usr/bin/python3

'''
Minimum Operations

_**0. Minimum Operations**_

In a text file, there is a single character `H`. Your text editor can execute only two operations in this file: `Copy All` and `Paste`. Given a number `n`, write a method that calculates the fewest number of operations needed to result in exactly `n` `H` characters in the file.

- Prototype: `def minOperations(n)`

- Returns an integer

- If `n` is impossible to achieve, return `0`

```Bash
n = 9

H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6
```Bash

carrie@ubuntu:~/0x02-minoperations$ cat 0-main.py
```

```Python
#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
```

```Bash

carrie@ubuntu:~/0x02-minoperations$
carrie@ubuntu:~/0x02-minoperations$ ./0-main.py
Min number of operations to reach 4 characters: 4
Min number of operations to reach 12 characters: 7
carrie@ubuntu:~/0x02-minoperations$
```
'''

def minOperations(n):
    '''
    Method that calculates the fewest number of operations needed to result in exactly `n` `H` characters in the file.
    '''
    if n <= 1:
        return 0
    else:
        for i in range(2, n):
            if n % i == 0:
                return minOperations(int(n / i)) + i
        return n
