import unittest

from selenium import webdriver

from PageObject.SearchPlayer_page import SearchPlayerPage


class searchPlayerCase(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.sp = SearchPlayerPage(cls.driver)
        print("前置条件")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        print("后置条件")

    def test_search_player(self):
        # 登陆成功
        lo

        # 调用方法

        self.assertEqual("1=2")




if __name__ == '__main__':
    unittest.main()
