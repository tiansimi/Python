import smtplib  # 用于邮件的发信动作
from email.mime.text import MIMEText  # 用于构建邮件的内容
from email.header import Header  # 用于构建邮件头
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr
import schedule
import time


# 引入schedule和time

# 发送附件图片方法
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def send_emails():
    # 邮件对象
    msg = MIMEMultipart()
    from_addr = "970280628@qq.com"
    password = "666"
    to_addr = "qi.tian@iconbow.com"
    # msg = MIMEText("hello,你好啊，我是米宝爸爸！", "plain", "utf-8")
    msg["From"] = _format_addr("Python爱好者<%s>" % from_addr)
    msg["To"] = _format_addr("未来的你<%s>" % to_addr)
    msg["Subject"] = Header("Test_TQ")  # 邮件主题
    msg.attach(MIMEText("hello,你好啊，我是普拉多！", "plain", "utf-8"))
    # 图片嵌入邮件内容
    msg.attach(MIMEText('<html><body><h1>Hello，你好啊，我是普拉多！</h1>' +
                        '<p><img src="cid:0"></p>' +
                        '</body></html>', 'html', 'utf-8'))
    # 添加一个附件：添加一个MIMEBase，从本地读取一个图片
    with open("/Users/tiansimi/Desktop/爱接力/图片/IMG_6271.JPG", "rb+") as f:
        # 设置附件的MIMEBase和文件名，这里的是jpg类型
        mime = MIMEBase("image", "jpg", filename="IMG_6271.JPG")
        # 加上必要的头信息
        mime.add_header('Content-Disposition', 'attachment', filename='IMG_6271.JPG')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件内容读取进来
        mime.set_payload(f.read())
        # 用base64编码
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart；
        msg.attach(mime)

    smtp_server = "smtp.qq.com"
    server = smtplib.SMTP(smtp_server, 25)  # smtp协议默认端口是25
    server.set_debuglevel(1)  # 打印出和SMTP服务器交互的日志信息
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())  # 发件人由于可以一次发给多个人，所以传入一个list
    server.quit()


schedule.every().wednesday.at("19:06").do(send_emails)
while True:
    schedule.run_pending()
    time.sleep(1)

