from flask import Flask
from daemonize import Daemonize
import smtplib
import email.message
import os, sys

app = Flask(__name__)

server = smtplib.SMTP('smtp.gmail.com:587')

def main():
  while True:
    email_content = """
    <html>
    
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        
      <title>Tutsplus Email Newsletter</title>
      <style type="text/css">
        a {color: #d80a3e;}
      body, #header h1, #header h2, p {margin: 0; padding: 0;}
      #main {border: 1px solid #cfcece;}
      img {display: block;}
      #top-message p, #bottom p {color: #3f4042; font-size: 12px; font-family: Arial, Helvetica, sans-serif; }
      #header h1 {color: #ffffff !important; font-family: "Lucida Grande", sans-serif; font-size: 24px; margin-bottom: 0!important; padding-bottom: 0; }
      #header p {color: #ffffff !important; font-family: "Lucida Grande", "Lucida Sans", "Lucida Sans Unicode", sans-serif; font-size: 12px;  }
      h5 {margin: 0 0 0.8em 0;}
        h5 {font-size: 18px; color: #444444 !important; font-family: Arial, Helvetica, sans-serif; }
      p {font-size: 12px; color: #444444 !important; font-family: "Lucida Grande", "Lucida Sans", "Lucida Sans Unicode", sans-serif; line-height: 1.5;}
      </style>
    </head>
    
    <body>
    
    
    <table width="100%" cellpadding="0" cellspacing="0" bgcolor="e4e4e4"><tr><td>
    <table id="top-message" cellpadding="20" cellspacing="0" width="600" align="center">
        <tr>
          <td align="center">
            <p><a href="#">View in Browser</a></p>
          </td>
        </tr>
      </table>
    
    <table id="main" width="600" align="center" cellpadding="0" cellspacing="15" bgcolor="ffffff">
        <tr>
          <td>
            <table id="header" cellpadding="10" cellspacing="0" align="center" bgcolor="8fb3e9">
              <tr>
                <td width="570" align="center"  bgcolor="#d80a3e"><h1>Evanto Limited</h1></td>
              </tr>
              <tr>
                <td width="570" align="right" bgcolor="#d80a3e"><p>November 2017</p></td>
              </tr>
            </table>
          </td>
        </tr>
    
        <tr>
          <td>
            <table id="content-3" cellpadding="0" cellspacing="0" align="center">
              <tr>
                  <td width="250" valign="top" bgcolor="d0d0d0" style="padding:5px;">
                  <img src="https://thumbsplus.tutsplus.com/uploads/users/30/posts/29520/preview_image/pre.png" width="250" height="150"  />
                </td>
                  <td width="15"></td>
                <td width="250" valign="top" bgcolor="d0d0d0" style="padding:5px;">
                    <img src="https://cms-assets.tutsplus.com/uploads/users/30/posts/29642/preview_image/vue-2.png" width ="250" height="150" />
                </td>
              </tr>
            </table>
          </td>
        </tr>
        <tr>
          <td>
            <table id="content-4" cellpadding="0" cellspacing="0" align="center">
              <tr>
                <td width="200" valign="top">
                  <h5>How to Get Up and Running With Vue</h5>
                  <p>In the introductory post for this series we spoke a little about how web designers can benefit by using Vue. In this tutorial we will learn how to get Vue up..</p>
                </td>
                <td width="15"></td>
                <td width="200" valign="top">
                  <h5>Introducing Haiku: Design and Create Motion</h5>
                  <p>With motion on the rise amongst web developers so too are the tools that help to streamline its creation. Haiku is a stand-alone..</p>
                </td>
              </tr>
            </table>
          </td>
        </tr>
        
    
      </table>
      <table id="bottom" cellpadding="20" cellspacing="0" width="600" align="center">
        <tr>
          <td align="center">
            <p>Design better experiences for web & mobile</p>
            <p><a href="#">Unsubscribe</a> | <a href="#">Tweet</a> | <a href="#">View in Browser</a></p>
          </td>
        </tr>
      </table><!-- top message -->
    </td></tr></table><!-- wrapper -->
    
    </body>
    </html>
    
    
    """
    
    msg = email.message.Message()
    msg['Subject'] = 'Tutsplus Newsletter - Teste Envio E-mail'
    
    
    msg['From'] = 'thaislimadiasoriginal@gmail.com'
    msg['To'] = 'thais_lmdias@hotmail.com'
    password = "Thhais.."
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_content)
    
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    
    s.sendmail(msg['From'], [msg['To']], msg.as_string())

    print('Message Sent' + cont)

if __name__ == "__main__":
    myname=os.path.basename(sys.argv[0])
    pidfile='/tmp/%s' % myname       # any name
    daemon = Daemonize(app=myname,pid=pidfile, action=main)
    daemon.start()