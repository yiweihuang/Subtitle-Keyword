# -*- coding: utf-8 -*-
# ==============================
# chapter_video_dir is dump from mysql v_chapter_video table format is
# cid,chid,chapter_order,content-order,vid,v_name
#
# in_file_path is dumpform mongodb format is
# userId,videoStartTime,videoEndTime,videoTotalTime,videoId,time
# ==============================
import csv
import os
import sys

if len(sys.argv) < 2:
    print('Usage: python3 [].py contents')
    sys.exit()
else:
    cid = sys.argv[1]

video_file = 'Subtitle-Keyword/video_file/' + cid
chapter_video_dir = video_file + '/v_chapter_video.csv'
in_file_path = video_file + '/video_record_filtered.csv'
out_path = 'Subtitle-Keyword/to_weeks/' + cid

if not os.path.exists(out_path):
    os.makedirs(out_path)

title = []
weeks_vid = {}
with open(chapter_video_dir, 'r') as f:
    reader = csv.reader(f)
    # next(reader)  # skip title
    for line in reader:
        chid = int(line[1])
        content_order = int(line[3])
        vid = int(line[4])
        order_vid = (content_order, vid)
        if weeks_vid.get(chid) is None:
            weeks_vid[chid] = [order_vid]
        else:
            weeks_vid[chid].append(order_vid)

# sort vid by content_order every week
# for chid in weeks_vid:
#     a = sorted(weeks_vid[chid], key=lambda x: x[0])
#     print(a)
# write week video to file
for chid in weeks_vid:
    print(chid)
    dir_path = out_path+'/'+str(chid)
    # create week folder if not exists
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    vid_list = []
    for video in weeks_vid[chid]:
        vid = video[1]
        vid_list.append(vid)
        for index, vid in enumerate(vid_list):
            out_file_name = '/'+str(vid)+'.csv'
            out_file_path = dir_path+out_file_name
            out = []
            with open(in_file_path, 'r') as f:
                reader = csv.reader(f)
                next(reader)  # skip the first line
                for line in reader:
                    if int(line[4]) == vid:  # catch video records by video id
                        out.append(line)
            with open(out_file_path, 'w') as f:
                w = csv.writer(f)
                w.writerows(out)
