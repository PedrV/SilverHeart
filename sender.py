import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class emailSender:
    def Email():
        try:

            user = 'origin@gmail.com'
            to = "destination@company.com"
            passwOrd = "plainTXT"

            msg = MIMEMultipart()

            msg["From:"] = user
            msg["To"] = to
            msg["Subject"] = 'OMG Super Important Message'
            body = 'Hey, what up'

            msg.attach( MIMEText( body, "plain" ) )
            filename = "Key.txt"
            attachment = open( 'C:\\Users\\File.log', "rb" )

            part = MIMEBase( "application", "octet-stream" )
            part.set_payload( (attachment).read() )
            encoders.encode_base64( part )
            part.add_header( "Content-Disposition", "attachment; filename= %s" % filename )

            msg.attach( part )

            server = smtplib.SMTP_SSL( 'smtp.company.com',
                                       'ConnectionPort (465 - gmail)' )  # using smtplib.SMTP_SSL instead to ensure secure connection
            # server.ehlo() <- command to create a insecure connection
            # server.starttls() <- make the connection secure (Google doesn't support this method)

            server.login( user, passwOrd )
            Text = msg.as_string()
            server.sendmail( user, to, Text )
            server.quit()

        except smtplib.SMTPConnectError:
            print( "Error Connection" )
        except smtplib.SMTPServerDisconnected:
            print( 'Server refused' )
        else:
            print( "Job done" )

emailSender.Email()