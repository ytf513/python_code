import urllib
import urllib2
def get_taobao_api_data(app_para_dct):
  content = ""
  if app_para_dct:
    para_dct = {}
    para_dct['a'] = 'a'
    para_dct['b'] = 'b'
    url = """http://gw.api.taobao.com/router/rest"""
    para_data = urllib.urlencode(para_dct)
    f = urllib2.urlopen(url, para_data)
    content = f.read()
  return content
