"""
页面对象类，用于实现业务流程，是整个POM设计核心
模板：URL 核心元素 核心业务

1.不同页面是不同URL来区分的 URL就是每个页面的地址
2.把定位方式写在配置文件里面

查询玩家页面，用于实现查询玩家业务流程
"""
import time

from selenium import webdriver

from Base.base_page import BasePage
from PageObject.login_page import LoginPage
from Util.ParseConfFile import ParseConfigFile


class SearchPlayerPage(BasePage):
    # # 调用解析ini配置文件方法
    par = ParseConfigFile()
    searchPlayerPage_Options = par.get_section("searchPlayer_page")

    # 从ini文件中读取定位元素，并切分
    # 首页
    location_type_homepage, location_express_homepage = searchPlayerPage_Options["search_player_page.homepage"].split(
        ":")
    print(location_type_homepage, location_express_homepage)
    # 玩家管理
    location_type_playerManagement, location_express_playerManagement = searchPlayerPage_Options[
        "search_player_page.playermanagement"].split(":")
    # 查询玩家
    location_type_searchPlayer, location_express_searchPlayer = searchPlayerPage_Options[
        "search_player_page.searchplayer"].split(":")
    # 输入玩家ID
    location_type_inputPlayerID, location_express_inputPlayerID = searchPlayerPage_Options[
        "search_player_page.inputplayerid"].split(":")
    # 点击查询
    location_type_search, location_express_search = searchPlayerPage_Options[
        "search_player_page.search"].split(":")
    # 输入经验值

    # 点击增加

    element_homePageButton = (location_type_homepage, location_express_homepage)
    element_playerManagement = (location_type_playerManagement, location_express_playerManagement)
    element_searchPlayer = (location_type_searchPlayer, location_express_searchPlayer)
    element_inputPlayerID = (location_type_inputPlayerID, location_express_inputPlayerID)
    element_search = (location_type_search, location_express_search)

    # 点击首页按钮
    def click_homePageButton(self):
        try:
            self.click(self.element_homePageButton)
            time.sleep(5)
        except Exception as e:
            print(e)

    # 点击玩家管理
    def click_PlayerManagement(self):
        try:
            self.click(self.element_playerManagement)
            time.sleep(5)
        except Exception as e:
            print(e)

    # 点击查询玩家
    def click_searchPlayer(self):
        try:
            self.click(self.element_searchPlayer)
            time.sleep(5)
        except Exception as e:
            print(e)

    # 输入玩家ID或者手机号
    def input_playerMessage(self):
        self.input(self.element_inputPlayerID)
        time.sleep(5)

    # 点击查询
    def click_search(self):
        self.click(self.element_search)
        time.sleep(5)

    # 给玩家添加经验
    def input_exp(self):
        pass

    # 点击增加按钮
    def add_exp_button(self):
        pass


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://test.albcoininworld.com:9100/")
    login = LoginPage(driver)
    time.sleep(15)
    login.input_username("admin")
    login.input_password("123456")
    login.click_button()
    time.sleep(20)
    # todo: 网页加载成功后再调点击事件
    sp = SearchPlayerPage(driver)
    # sp.click_homePageButton()
    time.sleep(5)
    sp.click_PlayerManagement()
    time.sleep(5)
    sp.click_searchPlayer()
    time.sleep(30)
