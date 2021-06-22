"""
SMTP PROTOCOL
-Simple Mail Transfer Protocol (SMTP) is the protocol to send emails.
-SMTP just deals with sending emails to others.
-It requires to configure a server and a port (almost always 587)

SMTP Providers and domain names:
-Gmail           - smtp.gmail.com (port 587)
-Outlook/Hotmail - smtp-mail.outlook.com (port 587)
-Yahoo Mail      - smtp.mail.yahoo.com (port 587)
"""

import smtplib



# -----------------SENDING EMAILS-----------------

# Create SMTP object and connect to host
smtp_obj = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)

# Call the ehlo() method first thing after getting the SMTP object
print(smtp_obj.ehlo())

# Start TLS encryption for port 587
smtp_obj.starttls()

# Login to SMTP server
smtp_obj.login('poncelas91@outlook.com', 'NIdHoGg_/4392&?')

# Send email
# Message string must start with 'Subject: subject_text \n' for the subject line
# The '\n' newline character separates the subject line from the main body
smtp_obj.sendmail(from_addr='poncelas91@outlook.com', to_addrs='aemgysuyslavqmyyoa@wqcefp.com',
                  msg='''Subject: Prueba Python\n\nFeliz miaaaurrrrrtes''')

# Disconnect from SMTP server
smtp_obj.quit()
