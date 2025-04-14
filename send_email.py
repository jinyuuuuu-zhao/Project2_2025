import smtplib
from email.message import EmailMessage
#Set the sender email and password and recipient emails
from_email_addr = "yuxin610729@outlook.com"
from_email_pass = "ZhaoYuJin060710"
to_email_addr = "2577839182@qq.com"
#Create a message object
msg = EmailMessage()
#Set the email body
body = "Hello from Raspberry Pi"
msg.set_content(body)
#Set sender and recipient
msg['From'] = from_email_addr
msg['To'] = to_email_addr
#Set your email subject
msg['Subject'] = 'TEST EMAIL'
#Connecting to server and sending email
#Edit the following Line with your provider's SMTP server details
server = smtplib.SMTP('smtp.office365.com', 587)
#Comment out the next Line if your email provider doesn't use TLS
server.starttls()
#Login to the SMTP server
server.login(from_email_addr,from_email_pass)
#Send the message
server.send_message(msg)
print("Email sent")
#Disconnect from the Server
server.quit()
