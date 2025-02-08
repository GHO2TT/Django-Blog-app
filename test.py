# # import os

# # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# # EMAIL_HOST = 'smtp.gmail.com'
# # EMAIL_PORT = 587
# # EMAIL_USE_TLS = True
# # EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
# # EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
# # DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', EMAIL_HOST_USER)

# # print(f"EMAIL_HOST_USER: {EMAIL_HOST_USER}")
# # print(f"EMAIL_HOST_PASSWORD: {EMAIL_HOST_PASSWORD}")
# # print(f"DEFAULT_FROM_EMAIL: {DEFAULT_FROM_EMAIL}")

# import os
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

# def send_email():
#     # Get environment variables
#     email_host_user = os.environ.get('EMAIL_HOST_USER')
#     email_host_password = os.environ.get('EMAIL_HOST_PASSWORD')
    
#     if not email_host_user or not email_host_password:
#         print("Please set the environment variables EMAIL_HOST_USER and EMAIL_HOST_PASSWORD.")
#         return

#     # Email details
#     from_email = email_host_user
#     to_email = 'ndavidabjc@gmail.com'
#     subject = 'Test Email'
#     body = 'This is a test email sent from a Python script.'

#     # Create MIME message
#     msg = MIMEMultipart()
#     msg['From'] = from_email
#     msg['To'] = to_email
#     msg['Subject'] = subject
#     msg.attach(MIMEText(body, 'plain'))

#     try:
#         # Connect to Gmail's SMTP server
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.starttls()
#         server.login(email_host_user, email_host_password)
        
#         # Send email
#         server.send_message(msg)
#         server.quit()
        
#         print("Email sent successfully!")
#     except Exception as e:
#         print(f"Failed to send email: {e}")

# if __name__ == "__main__":
#     send_email()

