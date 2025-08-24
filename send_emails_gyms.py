import os
import csv
import time
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

TEST_MODE = True  # Set to False to actually send emails

subject = "Quick Survey for Gyms – Irish Startup for Gyms"

body_template = """<html>
<body>
<p>To whom it may concern from {gym_name},</p>

<p>Thanks in advance,<br>
Mario</p>
</body>
</html>"""

def send_email(subject, body, to_email):
    if TEST_MODE:
        print("="*50)
        print(f"To: {to_email}")
        print(f"Subject: {subject}")
        print("HTML Body:")
        print(body)
        print("="*50)
        return

    try:
        msg = MIMEMultipart('alternative')
        msg["Subject"] = subject
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = to_email

        # Create both HTML and plain text versions
        html_part = MIMEText(body, "html")
        msg.attach(html_part)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, [to_email], msg.as_string())
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Error sending email to {to_email}: {e}")

with open("/Users/mariofabelo/Downloads/gym list email.csv", newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Use lower() and strip() to allow for minor header variations
        gym_name = row.get('Gym')
        email = row.get('Contact Email')
        if not gym_name or not email:
            print(f"Skipping row with missing info: {row}")
            continue
        body = body_template.format(gym_name=gym_name)
        send_email(subject, body, email)
        time.sleep(2)  # To simulate real sending pace (optional in test mode)
