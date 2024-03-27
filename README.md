# learning_materials

Python package for comfortable cramming of searching and sorting algorithms, data structures (DS) and design patterns. It contains base implementations for most common algorithms and DS.

For now, it has mostly consists of the sorting and searching algorithms, several DS, but they don't have any validation system, and design patterns will be added soon.

## Installation
```sh
git clone https://github.com/lumpsoid/learning_materials
pip install ./learning_materials
```

## Cramming

You need to create a separate `.py` or `.ipynb` file for your training. 
In that file you should import this package:
```python
import learning_materials as lm
```
After this you can choose the algorithm to cram and implement it. (IDE should help you to generate a method call).
In search algorithms, the endpoint method is called `search()`, in sorting -> `sort()`
```python
class BinarySearchTraining(lm.BinarySearch):
  def search() # ...
    pass
```
When you've completed you implementation, you can test it with `BinarySearchTraining.search_test()` 
(IDE should help to find the right method for it).
If you need to look up the base implementation, you can jump to the class declaration.

complete example would be:
```python
import learning_materials as lm

class BinarySearchTraining(lm.BinarySearch):
  def search()
    pass

BinarySearchTraining.search_test()
```