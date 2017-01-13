# -*- coding=utf-8 -*-

import pandas as pd
import os

path = '../to_weeks/'
video_file = '../video_file/'
data = {}
df_ = pd.DataFrame()
for cid in os.listdir(path):
    data['cid'] = cid
    total_cid_time = []
    for chid in os.listdir(path + cid):
        for filename in os.listdir(path + cid + '/' + chid):
            if os.stat(path + cid + '/' + chid + '/' + filename).st_size != 0:
                df = pd.read_csv(path + cid + '/' + chid + '/' + filename, header=None, usecols=[1,2])
                total_time = df[1].sub(df[2], axis=0).abs().sum()
                total_cid_time.append(total_time)
    sum_time = sum(total_cid_time)
    m, s = divmod(sum_time, 60)
    h, m = divmod(m, 60)
    data['time'] = "%d:%02d:%02d" % (h, m, s)
    df_ = df_.append(data, ignore_index=True)
df_.to_csv('out.csv', sep=',', encoding='utf-8')
