# PyLogs
**Version 1.0.0**

This python library allows you to easily create logs for your code.

## Installation instructions
1. Open up your terminal
2. Run ```pip install pylogs```
3. Import it to your project (```import pylogs```)

## Example code
Code:
```python
from pylogs import Logger
from pylogs.message_types.debug_message import DebugMessage

Logger.log(DebugMessage(), "Hello world!")
```
Output:
```
[DEBUG] Hello world!
```
---
Code:
```python
from pylogs import Logger
from pylogs.message_types.critical_message import CriticalMessage


def add(a, b):
    if (not isinstance(a, float)) or (not isinstance(a, float)):
        Logger.log(CriticalMessage(), "A and B have to be of the type float.")
        # you should probably raise an error here
    return a + b

add(1, 2)
```
Output:
```
[CRITICAL] A and B have to be of the type float.
```
---
```python
from pylogs import Logger
from pylogs.message_types.debug_message import DebugMessage

Logger.log_to_file(DebugMessage(), "Hello world!", "example.pylog")
```
You can display the content of the file by running: ```cat example.pylog``` on macOS + Linux and ```type example.pylog``` on Windows
