#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = 'rupy'

import csv
import os
import MeCab
from urlparse import urljoin
import re

# translation (Jaoanese & English) file is needed in this program

class Translation():

    def __init__(self, csv_file_path):
        self.translation_path = csv_file_path


    def read_csv_and_save_as_txt(self):

        # directories existence check
        if not os.path.isdir('english'):
            os.mkdir('english')
        if not os.path.isdir('japanese'):
            os.mkdir('japanese')

        reader = csv.reader(open(self.translation_path, 'r'))
        for i, row in enumerate(reader):

            # header
            if i == 0:
                continue

            # English
            en_txt_fixed = row[0]
            # fix text
            if not en_txt_fixed.endswith("\n"):
                en_txt_fixed += "\n"
            output_en = 'english/%s.txt' % i
            print "Saving: %s" % output_en
            with open(output_en, 'w') as f:
                f.write(en_txt_fixed)

            # Japanese
            jp_txt = row[1]
            # fix text
            jp_txt_fixed = jp_txt.replace("。 ", "。\n")
            # delete lines which is only tab
            jp_txt_fixed = re.sub(r"\n[\t]*$", "\n", jp_txt_fixed)
            if not jp_txt_fixed.endswith("\n"):
                jp_txt_fixed += "\n"
            output_jp = 'japanese/%s.txt' % i
            print "Saving: %s" % output_jp
            with open(output_jp, 'w') as f:
                f.write(jp_txt_fixed)

    def wakati(self):

        # directories existence check
        if not os.path.isdir('wakati'):
            os.mkdir('wakati')

        files = os.listdir('japanese')
        for file in files:
            with open('japanese/' + file) as f1:
                output_wak = urljoin('wakati/', file)
                with open(output_wak, 'w') as f2:
                    for txt in f1.readlines():

                        tagger = MeCab.Tagger("-Owakati")
                        wakati_result = tagger.parse(txt)

                        print "Saving: %s" % output_wak
                        f2.write(wakati_result)


if __name__=="__main__":

    # put parallel translation data somewhere in advance
    csv_file = 'translations/pascal_sentence_numbers.csv'
    # initialize instance
    ps = Translation(csv_file)
    # create text data from csv file
    ps.read_csv_and_save_as_txt()
    # create wakati-gaki text data (Japanese text data separated by space between each word) retaining line break
    ps.wakati()
