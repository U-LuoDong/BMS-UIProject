"""
用来解析ini配置文件
"""
import configparser
from Conf.VarConfig import element_location_path


class ParseConfigFile:
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(element_location_path, encoding="utf-8")

    def get_section(self, sectionName):
        # 得到sectionName名下所有的parameter
        """
        sections()：得到所有的section，并以列表的形式返回
        options(section)：得到section所有的option
        items(section)：得到section所有的键值对
        """
        result = dict(self.cf.items(sectionName))
        return result

    def get_parameter_value(self, sectionName, parameterName):
        # 得到sectionName中某个parameterName对应的值
        # get()方法的第一个参数是section，第二个参数是option，得到的结果默认是字符串类型
        return self.cf.get(sectionName, parameterName)

# 调试
# if __name__ == '__main__':
#     par = ParseConfigFile()
#     # print(par.getSection("login_page"))
#     # print(par.getParameterValue('login_page', 'login_page.username'))
#     loginOptions = par.getSection("login_page")
#     location_type, location_express = loginOptions["login_page.username"].split(":")
#     print(location_type, location_express)
