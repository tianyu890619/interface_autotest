#coding= utf-8
import requests
import readConfig as readConfig
from Log import MyLog as Log
import json
import urllib2
localReadConfig = readConfig.ReadConfig()

class ConfigHttp:
    def __init__(self):
        global host, port, url, timeout
        #读取配置文件中http字段
        host = localReadConfig.get_http("baseurl")
        port = localReadConfig.get_http("port")
        url = localReadConfig.get_http("url")
        timeout = localReadConfig.get_http("timeout")

        self.log = Log.get_log()
        self.logger = self.log.get_logger()
        self.headers = {}
        self.params = {}
        self.data = {}
        self.url = None
        # self.files = {}

    def set_url(self):
        self.url = host+port+url

    def set_headers(self, header):
        self.headers = header

    def set_params(self, param):
        self.params = param

    def set_data(self, data):
        self.data = data

    # def set_files(self, file):
    #     self.files = file

    # defined http get method
    def get(self):
        try:
            response = requests.get(self.url, params=self.params, headers=self.headers, timeout=float(timeout))
            # response.raise_for_status()
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None

    # defined http post method
    def post(self):
        try:
            response = requests.post(self.url, headers=self.headers, data=self.data,  timeout=float(timeout))
            # response.raise_for_status()
            return response
        except urllib2.URLError:
            self.logger.error("Time out!")
            return None