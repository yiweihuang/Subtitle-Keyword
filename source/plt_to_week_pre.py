# -*- coding=utf-8 -*-
import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

if len(sys.argv) < 2:
    print('Usage: python3 [].py contents')
    sys.exit()
else:
    cid = sys.argv[1]

count_people = 'Subtitle-Keyword/count_people/' + cid + '/'
for chid in os.listdir(count_people):
    count_people_chap = count_people + chid
    for vid in os.listdir(count_people_chap):
        complete_count_people = count_people_chap + '/' + vid
        if os.stat(complete_count_people).st_size != 0:
            df = pd.DataFrame.from_csv(complete_count_people, parse_dates=False)
            plt.figure()
            df.plot()
            plt.show()
