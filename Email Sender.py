import smtplib

sender = "your@mail.com"
password = "your_password"
receiver = "receiver@mail.com"

message = "Subject: Test\n\nThis is a test email"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender, password)
server.sendmail(sender, receiver, message)
server.quit()
