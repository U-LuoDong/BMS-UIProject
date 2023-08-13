# 控件定位配置文件
import os.path

# 项目所在路径
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)



element_location_path = os.path.join(base_dir, 'Conf/locator.ini')
testData = os.path.join(base_dir, 'Data')

# 日志文件目录
log_path = os.path.join(base_dir, 'Log')

# 测试脚本目录
test_case_path = os.path.join(base_dir, "TestCases")

# 测试报告目录
report_path = os.path.join(base_dir, "Reports")
# print(report_path)

