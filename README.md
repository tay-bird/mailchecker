# MAILCHECKER.
This is the code that handles mail for **http://skybird.taybird.com/**.
It can be run locally, or through Apache with WSGI.

## Usage.
Import the **EmailChecker** class from mailchecker. Initialize it by providing
a **mail server**, **address**, and **password**.

### Get the mail.

    conn = mailchecker.EmailChecker(server, userid, passwd)
    mail = conn.read()

### Iterate through the mail.

    for message in mail:
        print 'Message from: ', message['from']

### Write the mail.

    for message in mail:
        is_write = conn._write(mail, json_path)
        
        if is_write:
            print 'Email written to file'
