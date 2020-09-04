import smtplib  # 用于邮件的发信动作
from email.mime.text import MIMEText  # 用于构建邮件的内容
from email.header import Header  # 用于构建邮件头

from_addr = "970280628@qq.com"
password = "cahiijpanwyfbehb"
to_addr = "qi.tian@iconbow.com"
msg = MIMEText("hello,你好啊，我是米宝爸爸！", "plain", "utf-8")
msg["From"] = Header(from_addr)
msg["To"] = Header(to_addr)
msg["Subject"] = Header("Test_TQ")

smtp_server = "smtp.qq.com"
server = smtplib.SMTP(smtp_server, 25)  # smtp协议默认端口是25
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()
