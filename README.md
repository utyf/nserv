While developing this testing assignment I tried to keep everything 
as simple and light as possible. Result was tested with Python 2.7 only.


###Back-end

Following technologies are used:
* __Tornado__ is used to implement a websockets server. It's asynchronious and supports an event-loop inside.
* __Redis__ is used as a publish-subscribe bus. To make it compatible with Tornado coroutines [gredis](https://github.com/coldnight/gredis) is used as Python driver (which is a small async extension of standart [redis](https://github.com/andymccurdy/redis-py) package).

###API

API for usage from Python code consist of one function: notify. Usage:

```python
from nserv import notify

# level can be {success|info|warning|danger}
notify('A message', 'warning')
```

###Command-line tool
```
(env)utyf@utyf-ThinkPad-T420:~/work/viasto$ ./nserv_notify.py --help
usage: nserv_notify.py [-h] -m MESSAGE -l LEVEL

Post a notification.

optional arguments:
-h, --help            show this help message and exit
-m MESSAGE, --message MESSAGE
-l LEVEL, --level LEVEL
```

###Front-end

As front-end is not part of evaluation, I made a small experiment there, writing it in some kind of "functional" style. 
State is strictly separated from logic, every state transition is a pure function.

Following technologies are used:
* __React.js__ as library for visual components
* __Bootstrap__ as CSS framework

###Install and start
```bash
git clone https://github.com/utyf/nserv
cd nserv

# assuming, that python 2.7 is there
virtualenv env
. env/bin/activate
pip install -r requirements.txt
python nserv.py

# open http://localhost:8080/index.html
```
