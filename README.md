Inbox event listener for exchangelib
====================================
This library listens for events in the inbox and raises an event.

## Installation
`pip install git+https://gitlab.com/evan_brown/exchangelib-listener.git`


## Usage
Create listener:
```python
from exchangelib import DELEGATE, Account, Credentials, Configuration
from exchangelib.properties import NewMailEvent, MovedEvent
from exchangelib_listener import Listener

creds = Credentials(
    username='EMAIL_ADDRESS',
    password='PASSWORD'
)
config = Configuration(
    server='SERVER',
    credentials=creds
)
acct = Account(
    primary_smtp_address='EMAIL_ADDRESS',
    config=config,
    access_type=DELEGATE
)

listener = Listener(acct)
```

Create a method to call when events are raised:
```python
def events_received(events):
    for event in events:
        if isinstance(event, NewMailEvent):
            # Do something
        elif isinstance(event, MovedEvent):
            # Do something
```

Start listener:
```python
listener.streaming_events_received += events_received
listener.listen()
```


## Requirements
backports.zoneinfo==0.2.1\
cached-property==1.5.2\
certifi==2021.5.30\
cffi==1.14.6\
charset-normalizer==2.0.1\
cryptography==3.4.7\
defusedxml==0.7.1\
dnspython==2.1.0\
exchangelib==4.4.0\
idna==3.2\
isodate==0.6.0\
lxml==4.6.3\
ntlm-auth==1.5.0\
oauthlib==3.1.1\
pycparser==2.20\
Pygments==2.9.0\
python-dotenv==0.18.0\
pytz==2021.1\
requests==2.26.0\
requests-ntlm==1.1.0\
requests-oauthlib==1.3.0\
six==1.16.0\
tzdata==2021.1\
tzlocal==2.1\
urllib3==1.26.6
