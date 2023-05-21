"""
让所有的测试用例都一次性执行完成
1.通过suite.add方法这样需要一条条加进去 比较麻烦
2.通过discover方法来加载测试用例（推荐使用）
"""
import time
import unittest

from Conf.VarConfig import test_case_path, report_path
from TestCases.test_login_case_unittest import LoginCase
from TestCases.test_searchplayer_case import searchPlayerCase

if __name__ == '__main__':
    # 实例化一个测试套件
    suit = unittest.TestSuite()

    # 通过suite.add方法 把需要执行的测试用例加到测试套件中（不推荐，被弃用了）
    # unittest和ddt有冲突/执行用例很多的时候，需要把用例一条条加进来
    # # suit.addTest(LoginCase('test_Login'))
    # suit.addTest(searchPlayerCase('test_searchPlayer1'))
    # suit.addTest(searchPlayerCase('test_searchPlayer2'))

    # 通过discover方法来加载测试用例
    # discover(start_dir,pattern = "test_*.py")
    loader = unittest.TestLoader()
    suit.addTests(loader.discover(test_case_path))

    # 产生测试报告
    # now = time.strftime("%Y")
    # with (open(reportPath + '/' + now + "_report.html", "wb")) as fp:
    #     runner = HtmlTestRunner(
    #         stream=fp,
    #         title="测试报告",
    #         description="这是一份测试报告"
    #     )
    #     runner.run(suit)

    # 执行测试套件
    # runner = unittest.TextTestRunner()
    # runner.run(suit)
