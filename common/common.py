#coding= utf-8
import os
import readConfig as readConfig
from xlrd import open_workbook
from xml.etree import ElementTree as ElementTree
from Log import MyLog as Log
import configHttp
import json


localReadConfig = readConfig.ReadConfig()
proDir = readConfig.proDir
localConfigHttp = configHttp.ConfigHttp()
log = Log.get_log()
logger = log.get_logger()

caseNo = 0


# def get_visitor_token():
#     """
#     create a token for visitor
#     :return:
#     """
#     host = localReadConfig.get_http("BASEURL")
#     response = requests.get(host+"/v2/User/Token/generate")
#     info = response.json()
#     token = info.get("info")
#     logger.debug("Create token:%s" % (token))
#     return token


# def set_visitor_token_to_config():
#     """
#     set token that created for visitor to config
#     :return:
#     """
#     token_v = get_visitor_token()
#     localReadConfig.set_headers("TOKEN_V", token_v)


# def get_value_from_return_json(json, name1, name2):
#     """
#     get value by key
#     :param json:
#     :param name1:
#     :param name2:
#     :return:
#     """
#     info = json['info']
#     group = info[name1]
#     value = group[name2]
#     return value


def show_return_msg(response):
    """
    show msg detail
    :param response:
    :return:
    """
    url = response.url
    msg = response.text
    print("\n请求地址："+url)
    # 可以显示中文
    print("\n请求返回值："+'\n'+json.dumps(json.loads(msg), ensure_ascii=False, sort_keys=True, indent=4))
# ****************************** read testCase excel ********************************



# 从excel文件中读取测试用例
def get_xls(xls_name, sheet_name):
    cls = []
    # 获取xls文件路径
    xlsPath = os.path.join(proDir, "testFile", xls_name)
    # 打开xls文件
    file = open_workbook(xlsPath)
    # get sheet by name
    sheet = file.sheet_by_name(sheet_name)
    # get one sheet's rows
    nrows = sheet.nrows
    for i in range(nrows):
        if sheet.row_values(i)[0] != u'casename':
            cls.append(sheet.row_values(i))
    return cls

# 从xml文件中读取sql语句
database = {}
def set_xml():
    if len(database) == 0:
        sql_path = os.path.join(proDir, "testFile", "SQL.xml")
        tree = ElementTree.parse(sql_path)
        for db in tree.findall("database"):
            db_name = db.get("name")
            # print(db_name)
            table = {}
            for tb in db.getchildren():
                table_name = tb.get("name")
                # print(table_name)
                sql = {}
                for data in tb.getchildren():
                    sql_id = data.get("id")
                    # print(sql_id)
                    sql[sql_id] = data.text
                table[table_name] = sql
            database[db_name] = table

def get_xml_dict(database_name, table_name):
    set_xml()
    database_dict = database.get(database_name).get(table_name)
    return database_dict

def get_sql(database_name, table_name, sql_id):
    db = get_xml_dict(database_name, table_name)
    sql = db.get(sql_id)
    return sql