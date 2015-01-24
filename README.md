# MAILCHECKER.
Mailchecker connects with the specified server and provides a simple interface for incoming messages.

This utility was produced for **http://skybird.taybird.com/**. It provides a **mail.json** file.

## Usage.
Import the **EmailChecker** class from mailchecker. Initialize it by providing
a **mail server**, **address**, and **password**.

### Get the mail.

    conn = mailchecker.EmailChecker(server, userid, passwd)
    mail = conn.read()

### Iterate through the mail.

    for message in mail:
        print 'Message from:       ', message['from']
        print 'Message to:         ', message['to']
        print 'Message time:       ', message['time']
        print 'Message attachment: ', message['attachment']
        print 'Mesage body:        ', message['body']

### Write the mail.

    for message in mail:
        is_write = conn._write(mail, json_path)
        
        if is_write:
            print 'Email written to file'