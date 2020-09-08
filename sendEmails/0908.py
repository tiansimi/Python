import smtplib  # 用于邮件的发信动作
from email.mime.text import MIMEText  # 用于构建邮件的内容
from email.header import Header  # 用于构建邮件头
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr


# 发送附件图片方法
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(Header(name, 'utf-8'), addr)


# 邮件对象
msg = MIMEMultipart()
from_addr = "970280628@qq.com"
password = "666"
to_addr = "qi.tian@iconbow.com"
# msg = MIMEText("hello,你好啊，我是米宝爸爸！", "plain", "utf-8")
msg["From"] = Header(from_addr)
msg["To"] = Header(to_addr)
msg["Subject"] = Header("Test_TQ")
msg.attach(MIMEText("hello,你好啊，我是米宝爸爸！", "plain", "utf-8"))
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
                    '<p><img src="cid:0"></p>' +
                    '</body></html>', 'html', 'utf-8'))
with open("/Users/tiansimi/Desktop/爱接力/图片/IMG_6271.JPG", "rb+") as f:
    mime = MIMEBase("image", "jpg", filename="IMG_6271.JPG")
    mime.add_header('Content-Disposition', 'attachment', filename='IMG_6271.JPG')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)

smtp_server = "smtp.qq.com"
server = smtplib.SMTP(smtp_server, 25)  # smtp协议默认端口是25
server.set_debuglevel(1)  # 打印出和SMTP服务器交互的日志信息
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())  # 发件人由于可以一次发给多个人，所以传入一个list
server.quit()
