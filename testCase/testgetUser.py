#coding= utf-8
from common import getsign
import sys
import unittest
import paramunittest
import readConfig as readConfig
from common import Log as Log
from common import common
from common import configHttp as ConfigHttp
import json

reload(sys)
sys.setdefaultencoding('utf-8')
getUser_xls = common.get_xls("casedemo.xlsx", "getUser")
localReadConfig = readConfig.ReadConfig()
configHttp = ConfigHttp.ConfigHttp()


@paramunittest.parametrized(*getUser_xls)
class GetUser(unittest.TestCase):
    def setParameters(self, casename, appKey, locale, method, v, messageFormat, userId, merchantId, loginName, password, name, mobile, userType, code, message):

        self.case_name = str(casename)
        self.appKey = str(appKey)
        self.locale = str(locale)
        self.method = str(method)
        self.v = str(v)
        self.messageFormat = str(messageFormat)
        self.userId = str(userId)
        self.merchantId = str(merchantId)
        self.loginName = str(loginName)
        self.password = str(password)
        self.name = str(name)
        self.mobile = str(mobile)
        self.userType = str(userType)
        self.code = str(code)
        self.message = str(message)
        self.info = None

    def description(self):
        """

        :return:
        """
        self.case_name

    def setUp(self):
        """

        :return:
        """
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()
        # self.login_token = businessCommon.login()

    def testgetUser(self):
        """
        test body
        :return:
        """
        configHttp.set_url()


        # set headers
        header = {"Content-Type": "application/x-www-form-urlencoded"}
        configHttp.set_headers(header)

        # set params
        data = {
		'appKey':self.appKey,
		'method':self.method,
		'v':self.v,
		'messageFormat':self.messageFormat,
		'locale':self.locale,
		'userId':self.userId,
		'sign':getsign.get_sign('123456789',appKey=self.appKey,method=self.method,v=self.v,messageFormat=self.messageFormat,locale=self.locale,userId=self.userId)}
        configHttp.set_data(data)

        # test interface
        self.return_json = configHttp.post()

        # check result
        self.checkResult()

    def tearDown(self):
        """

        :return:
        """
        self.log.build_case_line(self.case_name, self.info['code'], self.info['message'])

    def checkResult(self):
        """
        check test result
        :return:
        """
        self.info = self.return_json.json()
        # print self.info
        common.show_return_msg(self.return_json)

        self.assertEqual(self.info['code'], self.code)
        self.assertEqual(self.info['message'], self.message)








# class Test1(unittest.TestCase):
# 	def setUp(self):
# 		# test_url = 'http://120.27.189.1:18002/octopus-op/router'
# 		#访问接口的url地址
#
# 		test_url = 'http://op.ejcop.com/router'
# #将参数添加到需求post的data中
# # datalist = {
# # 	'appKey':'20001',
# # 	'method':'systemService.getUser',
# # 	'v':'1.0',
# # 	'messageFormat':'json',
# # 	'locale':'zh_CN',
# # 	'userId':'24',
# # 	'sign':getsign.get_sign()
# # }
#
# def test_get_success(self):
# 	datalist = 'appKey=20001&method=systemService.getUser&v=1.0&messageFormat=json&locale=zh_CN&userId=24&sign=%s' % getsign.get_sign()
# 	#定义头文件
#
# 	head = {"Content-Type": "application/x-www-form-urlencoded"}
# 	response = requests.post(self.test_url, data=datalist,headers=head)
# 	result = response.text
# 	print result
# 	resultjson = json.loads(result)
# 	print resultjson
# 	print resultjson['code']
# 	self.assertEqual(resultjson['code'],00000000)
