"""
脚本层，用于编写自动化测试用例

unittest用来管理测试用例：1.每一个测试用例都是unittest的一个实例 2.测试方法需要以test开头
ddt用来实现数据驱动：1.首先测试数据准备好 2.在类前面写上@ddt.ddt 3.在测试方法前写上@ddt.data(*testdata)
"""
import unittest

import ddt
from selenium import webdriver

from PageObject.SearchPlayer_page import SearchPlayerPage

testdata = [{"ID": "1001269", "AddExp": "100"}]


class SearchPlayerCase(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        # 前置操作 1.打开浏览器 2.登陆成功
        cls.driver = webdriver.Chrome()
        # 创建实例
        cls.sp = SearchPlayerPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    @ddt.ddt(*testdata)  # 星号是拆包的操作 不加星号会把整个列表当作测试数据
    # data代表传进来的每一条数据
    def test_search_player(self, data):
        id = data["ID"]
        addExp = data["AddExp"]
        self.sp.click_homePage()  # 点击首页
        self.sp.click_PlayerManagement()  # 点击玩家管理
        self.sp.click_searchPlayer()  # 点击查询玩家
        self.sp.input_playerMessage(id)  # 输入玩家ID或者手机号
        self.sp.click_search()  # 点击查询按钮
        self.sp.input_exp(addExp)  # 给玩家添加经验
        self.sp.add_exp_button()  # 点击增加按钮


if __name__ == '__main__':
    unittest.main()
