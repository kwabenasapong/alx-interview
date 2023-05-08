# 0x07. Rotate 2D Matrix

## Learning Objectives

+ Given an `n` x `n` 2D matrix, rotate it 90 degrees clockwise.
+ Do not return anything. The matrix must be edited **in-place**.
+ You can assume the matrix will have 2 dimensions and will not be empty.

## Prototype

```python
def rotate_2d_matrix(matrix):
    """Rotate 2D Matrix"""
```

## Resources

+ [Rotate a 2D Matrix](https://www.geeksforgeeks.org/rotate-a-matrix-by-90-degree-in-clockwise-direction-without-using-any-extra-space/)
+ [Transpose](https://en.wikipedia.org/wiki/Transpose)
+ [Rotate In-Place](https://www.youtube.com/watch?v=IdZlsG6P17w)

## Requirements

+ Allowed editors: `vi`, `vim`, `emacs`
+ All your files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
+ All your files should end with a new line
+ The first line of all your files should be exactly `#!/usr/bin/python3`
+ A `README.md` file, at the root of the folder of the project, is mandatory
+ Your code should be documented
+ Your code should use the `PEP 8` style (version 1.7.x)
+ You are not allowed to import any module
+ All modules and functions must be documented
+ All your files must be executable

## Tasks

### [0. Rotate 2D Matrix](./0-rotate_2d_matrix.py)

Given an `n` x `n` 2D matrix, rotate it 90 degrees clockwise. Do not return anything. The matrix must be edited **in-place**. You can assume the matrix will have 2 dimensions and will not be empty.

```sh
$ cat main_0.py
#!/usr/bin/python3
"""
Test 0x07. Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    rotate_2d_matrix(matrix)
    print(matrix)   
$ ./main_0.py
[[7, 4, 1], [8, 5, 2], [9, 6, 3]]
$
```
