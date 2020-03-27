🏞 pyaare - A python wrapper round the AareGuru API
===============================

![Upload Python Package](https://github.com/eliabieri/pyaare/workflows/Upload%20Python%20Package/badge.svg?branch=master)

[![PyPI version](https://badge.fury.io/py/pyaare.svg)](https://badge.fury.io/py/pyaare)

[![DeepSource](https://static.deepsource.io/deepsource-badge-light-mini.svg)](https://deepsource.io/gh/eliabieri/pyaare/?ref=repository-badge)

pyaare makes it easy to access the [AareGuru](https://aare.guru/) API in your own Python projects.

Quick Start
-----------
    $ pip install pyaare

Examples
-----------

```python
from pyaare.pyaare import PyAare

aare = PyAare(city="Bern")
print(aare.tempC)
print(aare.tempText)
print(aare.flow)
print(aare.flowText)
aare.refresh()        # get the newest data
```

Getting Help
------------

* Open a issue on GitHub if you run into any problems

* Contact me on [Twitter](https://twitter.com/eliabieri)

Todo
------------

 * API documentation
