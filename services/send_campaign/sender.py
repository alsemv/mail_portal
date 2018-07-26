from O365 import Message


class Sender(object):
    @staticmethod
    def send_email(email, subject,  message):
        o365_auth = ('noreply_lyb@lyb.it', 'Notreset2017!')
        m = Message(auth=o365_auth)
        m.setRecipients(email)
        m.setSubject(subject)
        m.setBodyHTML(message)
        m.sendMessage()
        print("Email was send on {}, with message: {}".format(email, message))
