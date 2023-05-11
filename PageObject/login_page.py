"""
页面对象类，用于实现登录业务流程，是整个POM设计核心
模板：URL 核心元素 核心业务

1.不同页面是不同URL来区分的 URL就是每个页面的地址
2.把定位方式写在配置文件里面

登陆页面，用于实现登陆流程
"""
from time import sleep

from selenium import webdriver

from Base.basePage import BasePage
from Util.ParseConfFile import ParseConfigFile


class LoginPage(BasePage):
    # 页面URL地址
    # url = "http://test.albcoininworld.com:9100/"

    # def __init__(self,driver):
    #     self.driver = driver
    #     self.parse = ParseConfigFile()
    #     self.loginOptions = self.parse.getSection("login_page")

    # 调用解析ini配置文件方法
    par = ParseConfigFile()
    login_page_options = par.get_section("login_page")

    # 从ini文件中读取定位元素，并切分
    location_type_user, location_express_user = login_page_options["login_page.username"].split(":")
    location_type_pwd, location_express_pwd = login_page_options["login_page.password"].split(":")
    location_type_button, location_express_button = login_page_options["login_page.button"].split(":")

    # 核心元素 输入框输入内容
    element_username = (location_type_user, location_express_user)
    element_password = (location_type_pwd, location_express_pwd)
    element_button = (location_type_button, location_express_button)

    # print(element_username, element_password)

    # 原来的写法 被弃用了 改成写在ini配置文件中了
    # element_username = ('name', 'username')
    # element_password = ('name', 'password')
    # element_frame = ('tag name', 'iframe')

    # 打开URL地址
    def open_url(self, url):
        self.open(url)

    # 输入用户名
    def input_username(self, txt):
        self.input(self.element_username, txt)

    # 输入密码
    def input_password(self, txt):
        self.input(self.element_password, txt)

    # 点击登陆按钮
    def click_button(self):
        self.click(self.element_button)

    # 核心业务 登录页面输入账号和密码 不会写 换方法了
    # def login(self, txt):
    #     self.open(self.url)
    #     sleep(2)
    #     self.input(self.element_username, txt)
    #     # self.input(self.element_password, txt)
    #     self.click(self.element_button)
    #     sleep(1)
    #     # self.switch_iframe(self.element_frame)


# 调试
# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     lg = LoginPage(driver)
#     # lg.login("admin") 不会写 换方法了
#     # lg.login("123456") 不会写 换方法了
#     lg.openUrl("http://test.albcoininworld.com:9100/")
#     lg.input_username("admin")
#     lg.input_password("123456")
#     lg.click_button()
