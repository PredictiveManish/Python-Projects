import smtplib
from email.message import EmailMessage

sender_email = "" 
receiver_email = " " 

id_password = "" # Enter your own password 

msg = EmailMessage()
msg['Subject'] = 'Test Email from Python'
msg['From'] = sender_email
msg['To'] = receiver_email
msg.set_content("Hello, hope you're doing well, this is to inform you that for the next 6 months you've to daily tasks as you decide in the morning a little change in the schedule is okk but 50% change is failure of the day! You'll feel tired nobody cares, you'll feel alone nobody cares, nobody will come and save you so start grinding as much as you can because this time will help you to save your upcoming three semesters and allow you to enjoy and build something useful and scale it in college and not only get hired but have a product.")
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.starttls()
    smtp.login(sender_email, id_password)
    smtp.send_message(msg)
    
print("Email sent successfully!!")


