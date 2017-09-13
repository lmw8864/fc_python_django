import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail(from_email, to_email, text_cont, html_cont):
    message = MIMEMultipart('alternative')
    # alternative: html컨텐츠와 text컨텐츠를 함께 보낼 수 있는 양식
    # -> html을 해석할 수 있는 환경에서는 html을 보여주고, 그렇지 못한 환경에서는 text를 보여준다.
    message['Subject'] = "네이버 실시간 급등 검색어"  # Email Title
    message['From'] = from_email
    message['To'] = to_email

    part1 = MIMEText(text_cont, 'plain')  # 일반(text) 컨텐츠
    part2 = MIMEText(html_cont, 'html')  # html 컨텐츠

    message.attach(part1)  # 첨부
    message.attach(part2)

    # smtp서버 설정 시, 서버주소 및 포트는 각 mail서비스 사이트 참조 (지메일은 smtp.gmail.com:587)
    smtp_server = smtplib.SMTP('smtp.gmail.com:587')
    smtp_server.starttls()
    smtp_server.login("id", "pwd")
    smtp_server.sendmail(from_email, to_email, message.as_string())
    smtp_server.quit()
