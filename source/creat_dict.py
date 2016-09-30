import os
import jieba
import jieba.analyse

# jieba.analyse.extract_tags
# allowPOS 仅包括指定词性的词，默认值为空，即不筛选
# https://gist.github.com/luw2007/6016931 ('eng' for English)


original = '../original_file'
dict_loct = '../dict/new_userdict.txt'
jieba.set_dictionary('../dict/extra_dict/dict.txt.big')
jieba.analyse.set_stop_words('../dict/extra_dict/stop_words.txt')
jieba.analyse.set_idf_path('../dict/extra_dict/idf.txt.big')

tmp = []
for folder in os.listdir(original):
    for filename in os.listdir(original + '/' + folder):
        fr = open(original + '/' + folder + '/' + filename)
        content_list = fr.read().splitlines()
        for index, content in enumerate(content_list):
            if index % 4 == 1:
                words = jieba.analyse.extract_tags(content_list[index + 1],
                                                   topK=3,
                                                   withWeight=False,
                                                   allowPOS=('n', 's', 'f',
                                                             'v', 'a', 'b',
                                                             'z', 'r', 'eng'))
                for word in words:
                    tmp.append(word)
                    # with open(dict_loct, 'a') as f:
                    #     f.write(word + "\n")
        fr.close()
new_dict = list(set(tmp))
# print(new_dict)
with open(dict_loct, 'w') as f:
    for word in new_dict:
        f.write(word + "\n")
