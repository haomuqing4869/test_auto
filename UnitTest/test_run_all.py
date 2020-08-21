from UnitTest.HTMLTestRunner_cn import HTMLTestRunner
import os
import unittest


cur_path = os.path.dirname(os.path.realpath(__file__))
dicover = unittest.defaultTestLoader.discover(cur_path)
rpath = os.path.join(cur_path, 'report.html')
fp = open(rpath, 'wb')
runner = HTMLTestRunner(stream=fp,title='自动化测试报告',description='简单的自动化测试',retry=1,verbosity=2)
runner.run(dicover)
