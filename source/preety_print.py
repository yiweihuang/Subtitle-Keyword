import os
import json
import os

path = 'hot_word/933/'
weekList = os.listdir(path)
for week in weekList:
    name = week.split('.')[0]
    fp = open(path + week, 'rb')
    content = fp.read()
    # print(json.dump(content))
    with open('hot_word/933_p/' + name + '.json', 'w') as f:
        # json.dump(content, f,ensure_ascii=False, indent=4)
        # json.dump(content, f, ensure_ascii=False)
        json.dump(content, f, indent = 4,
               ensure_ascii = False)
