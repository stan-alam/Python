## Python Fluency

# 05

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/flnt/chap/05/fluentPython05%20-%20page%2013.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/flnt/chap/05/fluentPython05%20-%20page%2014.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/flnt/chap/05/fluentPython05%20-%20page%2015.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/flnt/chap/05/fluentPython05%20-%20page%2016.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/flnt/chap/05/fluentPython05%20-%20page%2017.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/flnt/chap/05/fluentPython05%20-%20page%2018.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/flnt/chap/05/fluentPython05%20-%20page%2019.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/flnt/chap/05/fluentPython05%20-%20page%2020.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/flnt/chap/05/fluentPython05%20-%20page%201.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/flnt/chap/05/fluentPython05%20-%20page%202.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/flnt/chap/05/fluentPython05%20-%20page%203.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/flnt/chap/05/fluentPython05%20-%20page%204.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/flnt/chap/05/fluentPython05%20-%20page%205.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/flnt/chap/05/fluentPython05%20-%20page%206.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/flnt/chap/05/fluentPython05%20-%20page%207.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/flnt/chap/05/fluentPython05%20-%20page%208.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/flnt/chap/05/fluentPython05%20-%20page%209.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/flnt/chap/05/fluentPython05%20-%20page%2010.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/flnt/chap/05/fluentPython05%20-%20page%2011.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/flnt/chap/05/fluentPython05%20-%20page%2012.png" width="80%" height="80%">
</a>

# 01

<p align="center">
  <img src="https://github.com/stan-alam/Python/blob/develop/flnt/chap/01/fpyth%20-%200.png" width="70%" height="70%">
</p>

<p align="center">
  <img src="https://github.com/stan-alam/Python/blob/develop/flnt/chap/01/fpyth%20-%201.png" width="70%" height="70%">
</p>

<p align="center">
  <img src="https://github.com/stan-alam/Python/blob/develop/flnt/chap/01/fpyth%20-%202.png" width="70%" height="70%">
</p>

```python
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds hearts clubs'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
        for rank in self.ranks]

    def __len__(self):
        return len(self.__cards)

    def __getitem__(self, position):
        return self.__cards[position]
```

<p align="center">
  <img src="https://github.com/stan-alam/Python/blob/develop/flnt/chap/01/fpyth%20-%203.png" width="70%" height="70%">
</p>

<p align="center">
  <img src="https://github.com/stan-alam/Python/blob/develop/flnt/chap/01/fpyth%20-%204.png" width="70%" height="70%">
</p>

<p align="center">
  <img src="https://github.com/stan-alam/Python/blob/develop/flnt/chap/01/fpyth%20-%205.png" width="70%" height="70%">
</p>

<p align="center">
  <img src="https://github.com/stan-alam/Python/blob/develop/flnt/chap/01/fpyth%20-%206.png" width="70%" height="70%">
</p>

<p align="center">
  <img src="https://github.com/stan-alam/Python/blob/develop/flnt/chap/01/fpyth%20-%207.png" width="70%" height="70%">
</p>

<p align="center">
  <img src="https://github.com/stan-alam/Python/blob/develop/flnt/chap/01/fpyth%20-%208.png" width="70%" height="70%">
</p>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/flnt/chap/01/fpyth-9.svg" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/flnt/chap/01/fpyth-10.svg" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/flnt/chap/01/fpyth-11.svg" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/flnt/chap/01/fpyth-12.svg" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/flnt/chap/01/fpyth-13.svg" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/flnt/chap/01/fpyth-14.svg" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/flnt/chap/01/fpyth-15.svg" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/flnt/chap/01/fpyth-16.svg" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/flnt/chap/01/fpyth-17.svg" width="80%" height="80%">
</a>



