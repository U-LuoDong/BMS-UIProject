"""
定时发送邮件功能
"""

import smtplib  # 负责发送邮件
from email.mime.text import MIMEText  # 构造文本
from email.mime.image import MIMEImage  # 构造图片
from email.mime.multipart import MIMEMultipart  # 将多个集合对象集合起来
from email.header import Header
import datetime
import warnings

from Conf.VarConfig import report_path

warnings.filterwarnings('ignore')


# 输入发件人昵称、收件人昵称、主题，正文，附件地址,附件名称生成一封邮件
def create_email(sender_name, receiver_name, email_subject, email_body, attachment_file, attachment_name):
    # 生成一个空的带附件的邮件实例
    message = MIMEMultipart()

    # 将正文以text的形式插入邮件中(参数1：正文内容，参数2：文本格式，参数3：编码方式)
    message_text = MIMEText(email_body, _subtype='plain', _charset='utf-8')  # _subtype有plain,html等格式，避免使用错误
    message.attach(message_text)

    # 生成发件人名称
    message['From'] = sender_name

    # 生成收件人名称
    message['To'] = Header(receiver_name, 'utf-8')

    # 生成邮件主题
    message['Subject'] = Header(email_subject, 'utf-8')

    # 读取附件的内容
    att = MIMEText(open(attachment_file, 'rb').read(), 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'

    # 生成附件的名称
    att["Content-Disposition"] = 'attachment; filename=' + attachment_name

    # 将附件内容插入邮件中
    message.attach(att)
    # 返回邮件
    return message


# 一个输入邮箱、密码、收件人、邮件内容发送邮件的函数
def send_email(sender, password, receiver, msg, mail_host="smtp.qq.com"):
    try:
        # 找到你的发送邮箱的服务器地址，已加密的形式发送
        server = smtplib.SMTP_SSL(mail_host)  # 发件人邮箱中的SMTP服务器
        server.connect(mail_host, port=465)
        server.ehlo()
        # 登录你的账号
        server.login(sender, password)  # 括号中对应的是发件人邮箱账号、邮箱密码
        # 发送邮件
        server.sendmail(sender, receiver, msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号（是一个列表）、邮件内容
        print("邮件发送成功" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        # 关闭SMTP对象
        server.quit()
    except Exception as e:
        print('邮件发送失败' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        print(e)


if __name__ == '__main__':
    # SMTP服务器,这里使用qq邮箱
    # mail_host = "smtp.qq.com"
    # 发件人邮箱
    sender = "2670626792@qq.com"
    sender_name = "2670626792@qq.com"
    # 邮箱授权码,注意这里不是邮箱密码！！
    mail_license = "lcduhjehwwhuebei"
    # 收件人邮箱（前面的昵称一定要用英文的）
    # ToDo：此处只能成功发送到第一个收件人邮箱，后续解决一下
    receiver_name = "ld<1559980806@qq.com>"+"lsq<18743172435@163.com>"
    # 邮件主题
    subject_content = """TEST-自动邮件发送"""
    # 邮件正文
    body_content = """你好，这是一个自动发送邮件代码！"""+"""请问你是罗小狗吗？"""
    attachment_file = report_path+'/test_pic.JPG'
    attachment_name = "test_pic.JPG"
    message = create_email(sender_name=sender_name, receiver_name=receiver_name, email_subject=subject_content,
                           email_body=body_content, attachment_file=attachment_file, attachment_name=attachment_name)
    send_email(sender=sender, password=mail_license, receiver=receiver_name, msg=message)
