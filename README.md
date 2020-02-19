🏞 pyaare - A python wrapper round the AareGuru API
===============================

pypublibike makes it easy to access the [AareGuru](https://aare.guru/) API in your own Python projects.

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
