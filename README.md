# InstanceCollector

This project provides a simple utility for collecting all instances of your Python classes. It offers easy integration into your projects with a decorator.

## Features

- Collecting instances using a decorator.
- Capability to iterate over instances of a class with optional filtering.

## Installation

You can install the package using poetry:

```sh
poetry add git+https://github.com/ulbwa/instance-collector
```

## Usage

1. Import InstanceCollector:

```python
from instance_collector import *
```

2. Decorate your class with `@InstanceCollector.collect`:

```python
@InstanceCollector.collect
class MyClass:
    def __init__(self, value: str):
        self.value = value
    
    def __repr__(self) -> str:
        return f'MyClass({self.value!r})'
```

3. Create instances of your class:

```python
obj1 = MyClass(value="First instance")
obj2 = MyClass(value="Second instance")
obj3 = MyClass(value="Third instance")
```

4. Access the instances through the collector:

```python
for obj in InstanceCollector.iter(MyClass):
    print(obj)
```

5. Iterate over instances with filtering:

```python
filter_fn = lambda x: "Second" in x.value
print(list(InstanceCollector.iter(MyClass, filter_fn)))
```
## Acknowledgements

Special thx to doil45 for providing the excellent Python penetration experience.