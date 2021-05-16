# TSorted

![Test status](https://github.com/bartfeenstra/tsorted/workflows/Test/badge.svg) [![Code coverage](https://codecov.io/gh/bartfeenstra/tsorted/branch/master/graph/badge.svg)](https://codecov.io/gh/bartfeenstra/tsorted) [![PyPI releases](https://badge.fury.io/py/tsorted.svg)](https://pypi.org/project/tsorted/) [![Supported Python versions](https://img.shields.io/pypi/pyversions/tsorted.svg?logo=python&logoColor=FBE072)](https://pypi.org/project/tsorted/) [![Recent downloads](https://img.shields.io/pypi/dm/tsorted.svg)](https://pypi.org/project/tsorted/) 

**TSorted** lets you sort your data topologically, such as for dependency resolution or task management.

## Usage

Before sorting your data, transform it into a *Directed Acyclic Graph* (*DAG*). Graph dictionary keys are the (hashable)
starting vertices, and their values are sets of destination vertices, defining unidirectional edges.

A standard topological sort:
```python
from tsorted import tsorted
graph = {
    1: {2, 3},
    2: {4},
    4: {3},
}
tsorted(graph)
# >>> OrderedSet([1, 2, 4, 3])
```

A grouped topological sort:
```python
from tsorted import tsorted_grouped
graph = {
    1: {2, 3},
    2: {4},
    3: {4},
}
tsorted_grouped(graph)
# >>> OrderedSet([frozenset({1}), frozenset({2, 3}), frozenset({4})])
```

## Development
First, [fork and clone](https://guides.github.com/activities/forking/) the repository, and navigate to its root directory.

### Requirements
- Bash (you're all good if `which bash` outputs a path in your terminal)

### Installation
If you have [tox](https://pypi.org/project/tox/) installed on your machine, `tox --develop` will create the necessary
virtual environments and install all development dependencies. 

Alternatively, in any existing Python environment, run `./bin/build-dev`.

### Testing
In any existing Python environment, run `./bin/test`.

### Fixing problems automatically
In any existing Python environment, run `./bin/fix`.

## Contributions 🥳
TSorted is Free and Open Source Software. As such you are welcome to
[report bugs](https://github.com/bartfeenstra/tsorted/issues) or
[submit improvements](https://github.com/bartfeenstra/tsorted/pulls).

## Copyright & license
TSorted is copyright [Bart Feenstra](https://twitter.com/BartFeenstra/) and contributors, and released under the
[MIT License](./LICENSE.txt). In short, that means **you are free to use TSorted**, but **if you
distribute TSorted yourself, you must do so under the exact same license** and provide that license.
