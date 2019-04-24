# -*- coding: utf-8 -*-
# @Time    : 2019/4/24 15:12
# @Author  : WHS
# @File    : Csv2kml.py
# @Software: PyCharm
import pandas as pd
import os
"""格式
<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://earth.google.com/kml/2.0">
<Document>
<Placemark>
<description>2</description>
<Point><coordinates>116.56184,39.566791,0</coordinates></Point>
</Placemark>
<Placemark>
<description>2</description>
<Point><coordinates>116.557926,39.5619,0</coordinates></Point>
</Placemark>
</Document>
</kml>
"""
def csvtokml(filename,savepath,cavfilepath):
    df = pd.read_csv(cavfilepath, header=None, usecols=[0, 1, 2])  # 读经纬度，标记
    fullname = filename+'.kml'
    with open(os.path.join(savepath,fullname), 'a') as file:
        file.write('<?xml version="1.0" encoding="UTF-8"?>' +'\n')
        file.write('<kml xmlns="http://earth.google.com/kml/2.0">' +'\n')
        file.write('<Document>' +'\n')
        for num in range(df.shape[0]):
            file.write('<Placemark>' +'\n')
            des = "<description>"+ str(df.iloc[num,2])+"</description>"
            coordinate = "<Point><coordinates>"+str(df.iloc[num,0])+","+str(df.iloc[num,1])+",0</coordinates></Point>"#此处0代表海拔，如果有海拔，可更改
            file.write(des +'\n')
            file.write(coordinate +'\n')
            file.write('</Placemark>' +'\n')
        file.write('</Document>' +'\n')
        file.write('</kml>' +'\n')
#示例
#csvtokml('text','H:\GPS_Data\\20170901\Top20\KML','H:\GPS_Data\\20170901\Top20\FilledRoute\\036f3c48-fed9-4acc-80ac-61fbad58b1c2Filled.csv')