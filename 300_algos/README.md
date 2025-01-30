## 300 Algos in Python

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/300_algos/images/01/300plusPyAlgo01%20-%20page%201.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/300_algos/images/01/300plusPyAlgo01%20-%20page%202.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/300_algos/images/01/300plusPyAlgo01%20-%20page%203.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/300_algos/images/01/300plusPyAlgo01%20-%20page%204.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/300_algos/images/01/300plusPyAlgo01%20-%20page%205.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/300_algos/images/01/300plusPyAlgo01%20-%20page%206.png" width="80%" height="80%">
</a>

```Python

def find_equilibrium_index(arry):
    total_sum = sum(arry)
    left_sum = 0

    for i, num in enumerate(arry):
        right_sum = total_sum = left_sum - num

        if left_sum == right_sum:
            return i
        left_sum += num
    return - 1  #no equilibrium index found

arry = [-7, 1, 5, 2, -4, 3, 0]
index = find_equilibrium_index(arry)
print("Equilibrium index is:", {index})

```

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/300_algos/images/01/300plusPyAlgo01%20-%20page%207.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/300_algos/images/01/300plusPyAlgo01%20-%20page%208.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/300_algos/images/01/300plusPyAlgo01%20-%20page%209.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/300_algos/images/01/300plusPyAlgo01%20-%20page%2010.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/300_algos/images/01/300plusPyAlgo01%20-%20page%2011.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/300_algos/images/01/300plusPyAlgo01%20-%20page%2012.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/300_algos/images/01/300plusPyAlgo01%20-%20page%2013.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/300_algos/images/01/300plusPyAlgo01%20-%20page%2014.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/300_algos/images/01/300plusPyAlgo01%20-%20page%2015.png" width="80%" height="80%">
</a>
