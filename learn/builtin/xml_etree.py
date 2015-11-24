#!/usr/bin/env python
#-*- encoding=utf-8  -*-

'ElementTree Test including namesspace'

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

#root = ET.fromstring(xml_content)
tree=ET.parse('shanghai.xml')
root=tree.getroot()
#print root[0][2]
NSMAP = {'yweather':"http://xml.weather.yahoo.com/ns/rss/1.0"}

print "shanghai weather belows here:"

for elem in tree.findall(".//yweather:forecast",namespaces=NSMAP):#root[0][12]:
    #if elem.tag=="title":
    #    print elem.text
    #elif elem.tag=="yweather:forecast":
    print "%s is %s,temperature low:%s,high:%s" % (elem.attrib['day'],elem.attrib['text'],elem.attrib['low'],elem.attrib['high'])
