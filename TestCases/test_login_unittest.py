"""
脚本层，用于编写自动化测试用例

unittest用来管理测试用例：1.每一个测试用例都是unittest的一个实例 2.测试方法需要以test开头
ddt用来实现数据驱动：1.首先测试数据准备好 2.在类前面写上@ddt.ddt 3.在测试方法前写上@ddt.data(*testdata)
"""
import time
import unittest
import ddt
from selenium import webdriver

from Conf.VarConfig import testData
from PageObject.Login_page import LoginPage
from Util.ExcelUtil import ExcelUtil

# TODO：测试数据都是通过读取Excel获得，此处先写成这样，后面改造
# testdata = [{"username": "admin", "password": "123456"}]
filename = (testData + "/BMSTestCase.xlsx")
test_data = ExcelUtil()
test_data.load_workbook(filename)
test_data.get_sheet_name("Login")
first_row = test_data.row_values(1)  # 首行
normal_row = test_data.row_values(2)  # 正常测试数据
testdata = [dict(zip(first_row, normal_row))]


@ddt.ddt
class LoginCase(unittest.TestCase):
    driver = None

    # 类级别，在所有测试用例执行之前只执行一次
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.lg = LoginPage(cls.driver)
        # print("111")

    # 后置动作，在所有测试用例执行之后只执行一次
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    # @unittest.skip("就是不想执行")
    @ddt.data(*testdata)  # 星号是拆包的操作 不加星号会把整个列表当作测试数据
    def test_Login(self, data):  # data代表传进来的每一条数据
        # username = data['username'] 换方法了 不会写这种
        # password = data['password']
        # self.lg.login(username)
        # self.lg.login(password)
        # self.lg.click()
        # 断言
        # self.assertIn("XXX", self.driver.page_source)

        # 新方法
        username = data['UserName']
        password = data['PassWord']
        # 调用login_page中openURL方法
        self.lg.open_url("http://test.albcoininworld.com:9100/")
        # 调用login_page中input_username方法
        self.lg.input_username(username)
        # 调用login_page中input_password方法
        self.lg.input_password(password)
        # 调用login_page中click_button方法
        # self.lg.click_button()
        # time.sleep(100)


if __name__ == '__main__':
    unittest.main()
