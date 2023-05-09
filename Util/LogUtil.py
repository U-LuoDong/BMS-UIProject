"""
logging库提供日志打印功能
logging日志一般分为5个常用等级
1.debug：最详细的日志信息，程序调试bug时使用
2.info：信息详细程度仅限于debug，程序正常运行时使用
3.warning：某些不期望的事情发生时记录的信息，但并不是错误
4.error：由于严重的问题导致不能正常运行时记录的信息，即出错时使用
5.critical：特别严重的问题，导致程序不能再继续运行时使用，很少使用该等级
"""
from loguru import logger
import logging
import os.path
import time

from Conf.VarConfig import log_path


# logging.debug("这是debug级别的日志")
# logging.info("这是info级别的日志")
# logging.warning("这是warning级别的日志")
# logging.error("这是error级别的日志")
# logging.critical("这是critical级别的日志")

class LogUtil:
    def __int__(self):
        logger.add(log_path + "/runtime_{time}.log")

    def debug(self, message):
        logger.debug(message)

    def info(self, message):
        logger.info(message)

    def warning(self, message):
        logger.warning(message)


# if __name__ == '__main__':
#     log = LogUtil()
#     log.debug("这是debug级别的日志")
