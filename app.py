import getpass
import smtplib
import sys
import time


remetente = '"Seu nome" <seu@email.com>'
msg = '''Subject: Assunto do e-mail
From: %s
To: {email}
Aqui vai a sua mensagem...
Voce pode substituir com os "campos" de cada entrada na lista de e-mails.
Por exemplo: {gentilico}
Atenciosamente,
    Diretoria da Associacao Python Brasil''' % remetente


class EmailConnection(object):
    def __init__(self, host, port, username, password):
        self.username = username
        self.password = password
        self.host = host
        self.port = port

    def connect(self):
        self.connection = smtplib.SMTP(self.host, self.port)
        self.connection.ehlo()
        self.connection.starttls()
        self.connection.ehlo()
        self.connection.login(self.username, self.password)

    def send_mail(self, from_, to, message):
        return self.connection.sendmail(from_, to, message)

    def close(self):
        self.connection.close()


if __name__ == '__main__':
    host = 'smtp.gmail.com'
    port = 587
    username = 'thaislimadiasoriginal@gmail.com'
    password = ''
    email_connection = EmailConnection(host, port, username, password)
    email_connection.connect()
    i = 0

    emails = [
              {'gentilico': 'Princesas e Imperatrizes',
               'email': 'thais_lmdias@hotmail.com'},
              {'gentilico': 'De outro Planeta',
               'email': 'thaislimadiasoriginal@gmail.com'},           
    ]

    for row in emails:
        mensagem = msg
        for key, value in row.items():
            # TODO: usar format ao inves de replace
            mensagem = mensagem.replace('{%s}' % key, value)

        i += 1
        sys.stdout.write('Enviando email %02d para <%s> ... ' % \
                         (i, row['email']))
        response = email_connection.send_mail(remetente, row['email'], mensagem)
        print('OK' if response == {} else response)
        time.sleep(0.1) # alguns servidores de e-mail fecham a conexão quando a
                        # taxa de e-mails enviados é grande
    email_connection.close()