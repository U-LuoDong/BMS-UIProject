"""
脚本层
使用pytest管理测试用例
"""
import ddt
import pytest
from selenium import webdriver

from PageObject.login_page import LoginPage

# 测试数据都是通过读取Excel获得，此处先写成这样，后面改造
testdata = [{"username": "admin", "password": "123456"}]


@ddt.ddt
class TestLoginCase:

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.lg = LoginPage(self.driver)
        print("这是前置动作")

    def teardown_class(self):
        self.driver.quit()
        print("这是后置动作")

    @ddt.data(*testdata)  # 星号是拆包的操作 不加星号会把整个列表当作测试数据
    @pytest.fixture(scope="class")
    def test_login(self, data):  # data代表传进来的每一条数据
        username = data['username']
        password = data['password']
        self.lg.open_url("http://test.albcoininworld.com:9100/")
        self.lg.input_username(username)
        self.lg.input_password(password)
        self.lg.click_button()


if __name__ == '__main__':
    pytest.main(["-v", "-s", "login_page.py"])
