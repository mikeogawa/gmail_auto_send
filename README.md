# Simple Mail Sender

There are times where you want to send a bunch of emails to multiple people using a template.

This repo gives you an example of how you can send multiple mails with the same context, and modify some messages depend on the user you are sending to.


## Description
- **data2text.py** - Script that writes csv to text file for sending message.
- **sending.py** - Sends mails using mail_list data.

## Note
- Modifications of python files are required.
- specified for Gmail.
- Python 3.

## How to Use
### Preparation
1. Edit the template script at `source/script.txt`.
1. Modify `source/name.csv` for data.
1. Modify `data2text.py` to write the template in your desired format.
1. Modify `sending.py`.

### Commands
```
python data2text.py
python sending.py
```

## License
MIT