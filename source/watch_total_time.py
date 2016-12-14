# -*- coding=utf-8 -*-

import pandas as pd
import os

path = '../to_weeks/'
video_file = '../video_file/'
data = {}
df_ = pd.DataFrame()
for cid in os.listdir(path):
    for chid in os.listdir(path + cid):
        for filename in os.listdir(path + cid + '/' + chid):
            if os.stat(path + cid + '/' + chid + '/' + filename).st_size != 0:
                df = pd.read_csv(path + cid + '/' + chid + '/' + filename, header=None, usecols=[1,2])
                total_time = df[1].sub(df[2], axis=0).abs().sum()
                data['cid'] = cid
                data['chid'] = chid
                data['total_time'] = total_time
                v_df = pd.read_csv(video_file + cid + '/v_chapter_video.csv', header=None, usecols=[4,5])
                vid = int(filename.split('.')[0])
                name = v_df.loc[v_df[4] == vid]
                data['filename'] = name[5]
                df_ = df_.append(data, ignore_index=True)
df_.to_csv('out.csv', sep=',', encoding='utf-8')
