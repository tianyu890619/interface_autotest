#coding= utf-8
#获取公共参数


def get_pubparm(appKeyValue,version,messageFormatValue,localeValue,methodName):
    return 'appKey=%s&v=%s&messageFormat=%s&locale=%s'%(appKeyValue,version,messageFormatValue,localeValue,methodName)