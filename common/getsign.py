#coding= utf-8
import hashlib
#获取sign值
def get_sign(secretValue,**kargs):
    # 列出公共参数和私有参数列表
    datalist = kargs
    # 按字典中的key升序排序,并转换成元祖
    asc_datalist = sorted(datalist.iteritems())
    # print asc_datalist
    # 将字典中所有请求参数、参数值、并在头部和尾部添加apkey对应的secret值进行连接组成一个字符串
    strlist = []
    for i in asc_datalist:
        str1 = ''.join(i)
        strlist.append(str1)
    # print strlist
    appkey_secret = secretValue
    # 在已该数组中的头部和尾部分别添加appkey对应的secret值
    strlist.insert(0,appkey_secret)
    strlist.append(appkey_secret)
    # print 'strlist= %s'%strlist
    # 连接成完整的字符串
    str = ''.join(strlist)
    # print str
    # 将字符串转成十六进制的编码串
    hash_sha1_16 = hashlib.sha1(str).hexdigest()
    # print hash_sha1_16
    # 再转成大写字符
    sign_value = hash_sha1_16.upper()
    # print sign_value
    return sign_value





