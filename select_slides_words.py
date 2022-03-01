import sys, os
import json


with open('full_rare_word_list.txt') as fin:
    wordset = {line.strip() for line in fin}

meeting_KB = {}
for dirname in os.listdir('OCR_raw'):
    dirpath = os.path.join('OCR_raw', dirname)
    meeting_KB[dirname] = []
    print(dirpath)
    for filename in os.listdir(dirpath):
        if 'txt' in filename:
            filepath = os.path.join(dirpath, filename)
            with open(filepath) as fin:
                for line in fin:
                    line = line.replace(',', ' ')
                    line = line.replace('.', ' ')
                    line = line.replace('!', ' ')
                    line = line.replace('?', ' ')
                    line = line.replace('"', ' ')
                    for word in line.split():
                        word = word.upper()
                        if len(word) > 2 and word in wordset and word not in meeting_KB[dirname]:
                            meeting_KB[dirname].append(word)

with open('meeting_KB.json', 'w') as fout:
    json.dump(meeting_KB, fout, indent=4)
for meeting, words in meeting_KB.items():
    with open('Biasing_lists/{}'.format(meeting), 'w') as fout:
        for word in words:
            fout.write(word + '\n')
