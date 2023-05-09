"""
基类：提供基础的工具方法，便于后续的测试对象的调用，以及页面对象的调用
封装常用的操作行为
"""


class BasePage:
    # 创建临时driver对象
    # driver = webdriver.Chrome()

    # 构造函数
    def __init__(self, driver):
        self.driver = driver

    # 访问url
    def open(self, url):
        self.driver.get(url)

    # 定位元素
    def locator(self, loc):
        return self.driver.find_element(*loc)

    # 输入
    def input(self, loc, txt):
        self.locator(loc).send_keys(txt)

    # 点击
    def click(self, loc):
        self.locator(loc).click()

    # 关闭浏览器
    def close(self):
        self.driver.close()

    # 切换句柄
    
    # 切换iframe
    def switch_iframe(self, loc):
        self.driver.switch_to.frame(self.locator(loc))
