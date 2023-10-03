import smtplib
import yaml
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

with open('config.yaml') as f:
    # читаем документ YAML
    data = yaml.safe_load(f)

msg = MIMEMultipart()
msg['From'] = data["email"]
msg['To'] = data["email"]
msg['Subject'] = "Test email"
text = f"Hello {data['name']} !!! How are you ?"

msg.attach(MIMEText(text))

with open("log.txt", "rb") as f:
    part = MIMEApplication(f.read(), Name=basename("log.txt"))
    part['Content-Disposition'] = f'attachment; filename="{basename("log.txt")}"'
    msg.attach(part)

body = "Test message body"
msg.attach(MIMEText(body, 'plain'))

# Настройка SMTP-сервера Mail.ru
smtp_server = 'smtp.mail.ru'
smtp_port = 465

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.login(data["email"], data["em_pwd"])
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    print("Email send")
except Exception as e:
    print(f"Ошибка: {str(e)}")
finally:
    server.quit()

