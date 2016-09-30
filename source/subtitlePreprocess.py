# -*- coding=utf-8 -*-

import os
import jieba
import datetime
import sys

if len(sys.argv) < 2:
    print('Usage: python3 [].py contents')
    sys.exit()
else:
    cid = sys.argv[1]


jieba.set_dictionary('Subtitle-Keyword/dict/extra_dict/dict.txt.big')
jieba.set_dictionary('Subtitle-Keyword/dict/keyword.txt')
keywords_dir = 'Subtitle-Keyword/dict/usrdict/' + cid + '.txt'
original = 'Subtitle-Keyword/subtitle_file/' + cid
done = 'Subtitle-Keyword/it_done/' + cid

# preprocess 原始字幕黨成 ((startTime,endTime):[wordList])
# original_file : 原始字幕黨
# it_done : 處理好的字幕黨


def create_dir_ifNotExist(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def preprocessSubtitle():
    with open(keywords_dir) as f:
        key_list = f.read().splitlines()

    for folder in os.listdir(original):
        print(folder + '============================')
        create_dir_ifNotExist(done + '/' + folder)
        for filename in os.listdir(original + '/' + folder):
            print(filename + '============================')
            fr = open(original + '/' + folder + '/' + filename)
            fw = open(done + '/' + folder + '/' + filename, 'w')
            content_list = fr.read().splitlines()
            for index, content in enumerate(content_list):
                if index % 4 == 1:
                    # time
                    time = content.split()
                    time.pop(1)
                    start = datetime.datetime.strptime(time[0], "%H:%M:%S,%f")
                    end = datetime.datetime.strptime(time[1], "%H:%M:%S,%f")
                    video_start = start.minute*60 + start.second
                    video_end = end.minute*60 + end.second
                    # keywords
                    words = jieba.cut(content_list[index + 1], cut_all=False)
                    tmp_word = []
                    for word in words:
                        tmp_word.append(word)
                    key = set(tmp_word).intersection(set(key_list))
                    fw.write('(' + str(video_start) + ',' + str(video_end)
                                 + ')' + ' : ' + str(key) + '\n')
            fr.close()

# preprocess 原始字幕黨
preprocessSubtitle()
