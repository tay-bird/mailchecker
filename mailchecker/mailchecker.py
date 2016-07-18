#!/usr/bin/env python

import imaplib, email, json

class EmailChecker:
    """ Create an EmailChecker instance.
    
    This tool uses a less secure channel to log in and
    read emails. Avoid passing valuable assets through
    this tool.
    
    Initialize the EmailChecker with:
     > server -- the email server address.
     > userid -- the account to connect to.
     > passwd -- the account's passwor.
    """
    
    def __init__ (self, server, userid, passwd):
        """ Initialize the EmailChecker. """
        self.mail = imaplib.IMAP4_SSL(server)
        self.mail.login(userid, passwd)
    
    def _write(self, mail, path):
        """ Write messages to json file. """
        data = json.dumps(mail)
        
        try:
            f = open(path,"w")
            f.write(data)
            f.close()
            status = 1
        except:
            status = 0
        
        return status

    def _parse(self, raw):
        """ Parse messages passed by the read method. """
        message = email.message_from_string(raw)
        
        # Get headers.
        recip = message['To']
        sender = email.utils.parseaddr(message['From'])
        sub = message['subject']
        attach = None
        time = None
        body = None
        
        # Parse individual payloads to retrieve body of email.
        maintype = message.get_content_maintype()
        if maintype == 'multipart':
            for part in message.get_payload():
                if part.get_content_maintype() == 'text':
                    body = part.get_payload()
                else:
                    pass
        elif maintype == 'text':
            body = message.get_payload()
        else:
            body = None
        
        result = {'to': recip,
                  'from': sender,
                  'time': time,
                  'subject': sub,
                  'body': body,
                  'attachment': attach
                  }
        
        return result
    
    def read(self, i=10):
        """ Get recent mail from the inbox.
        
        This method returns a list of messages in the
        inbox. A maximum number of messages to be
        returned can be specified. Default is 10.
        """
        self.mail.select("inbox")
        mail = []
        
        # Get list of email message IDs.
        result, data = self.mail.uid('search', None, "ALL")
        ids = data[0]
        id_list = ids.split()
        
        # Iterate through messages starting with most recent.
        for i in range(0, i):
            id = i + 1
            try:
                email_id = id_list[-id]  # get the latest.
            except IndexError:
                break
            
            result, data = self.mail.uid('fetch', email_id, '(RFC822)')
            message = self._parse(data[0][1])
            mail.append(message)
        
        return mail
