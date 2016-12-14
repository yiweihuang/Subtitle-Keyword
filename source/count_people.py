# -*- coding: utf-8 -*-

import sys
import os
import pandas as pd

if len(sys.argv) < 2:
    print('Usage: python3 [].py contents')
    sys.exit()
else:
    cid = sys.argv[1]

def create_dir_ifNotExist(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

if __name__ == '__main__':
    student_log = 'Subtitle-Keyword/to_weeks/' + cid + '/'
    count_people = 'Subtitle-Keyword/count_people/' + cid + '/'
    for chid in os.listdir(student_log):
        student_log_chap = student_log + chid
        count_people_chap = count_people + chid
        create_dir_ifNotExist(count_people_chap)
        for vid in os.listdir(student_log_chap):
            # df1 = DataFrame(columns=['a', 'b'])
            complete_student_log = student_log_chap + '/' + vid
            complete_count_people = count_people_chap + '/' + vid
            try:
                if os.stat(complete_student_log).st_size != 0:
                    df = pd.read_csv(complete_student_log, header=None, usecols=[0])
                    count_freq = df[0].value_counts()
                    count_people_freq = count_freq.value_counts()
                    sort_count = count_people_freq.sort_index()
                    df_count = pd.DataFrame(data=sort_count.index, columns=['Count'])
                    df_population = pd.DataFrame(data=sort_count.values, columns=['Population'])
                    df_ = pd.merge(df_count, df_population, left_index=True, right_index=True)
                    df_.to_csv(complete_count_people, sep=',', index=False)

            except StopIteration:
                print('=====%s/%s no content=====' % (chid, vid))
                pass
