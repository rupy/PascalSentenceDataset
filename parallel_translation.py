#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = 'rupy'

import csv
import os
import MeCab
from urlparse import urljoin
import re

# parallel translation (Jaoanese & English) file is needed in this program

class ParallelTranslation():

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
            output_en = 'english/%s.txt' % i
            print "Saving: %s" % output_en
            with open(output_en, 'w') as f:
                f.write(row[0])

            # Japanese
            output_jp = 'japanese/%s.txt' % i
            print "Saving: %s" % output_jp
            with open(output_jp, 'w') as f:
                f.write(row[1])

    def wakati(self):

        # directories existence check
        if not os.path.isdir('wakati'):
            os.mkdir('wakati')

        files = os.listdir('japanese')
        for file in files:
            with open('japanese/' + file) as f1:
                txt = f1.read()

                tagger = MeCab.Tagger("-Owakati")
                wakati_result = tagger.parse(txt)

                output_wak = urljoin('wakati/', file)
                print "Saving: %s" % output_wak
                with open(output_wak, 'w') as f2:
                    f2.write(wakati_result)

    def line_wakati(self):

        # directories existence check
        if not os.path.isdir('line_wakati'):
            os.mkdir('line_wakati')

        files = os.listdir('japanese')
        for file in files:
            with open('japanese_fixed/' + file) as f1:
                output_wak = urljoin('line_wakati/', file)
                with open(output_wak, 'w') as f2:
                    for txt in f1.readlines():

                        tagger = MeCab.Tagger("-Owakati")
                        wakati_result = tagger.parse(txt)

                        print "Saving: %s" % output_wak
                        f2.write(wakati_result)

    def fix_english(self):

        files = os.listdir("english/")
        for file in files:
            with open("english/" + file, "r") as f1:
                txt_fixed = f1.read()
                # txt_fixed = re.sub(r"(\s|\s[a-zA-Z]+)\.\s", "\\1.\n", txt)
                if not txt_fixed.endswith("\n"):
                    txt_fixed += "\n"
                with open("english_fixed/" + file, "w") as f2:
                    print "Saving: %s" % file
                    f2.write(txt_fixed)

    def fix_japanese(self):
        files = os.listdir("japanese/")
        for file in files:
            with open("japanese/" + file, "r") as f1:
                txt = f1.read()
                txt_fixed = txt.replace("。 ", "。\n")
                # delete lines which is only tab
                txt_fixed = re.sub(r"\n[\t]*$", "\n", txt_fixed)
                if not txt_fixed.endswith("\n"):
                    txt_fixed += "\n"
                with open("japanese_fixed/" + file, "w") as f2:
                    print "Saving: %s" % file
                    f2.write(txt_fixed)

if __name__=="__main__":

    csv_file = 'parallel_translation/pascal_sentence_numbers.csv'
    ps = ParallelTranslation(csv_file)
    # ps.read_csv_and_save_as_txt()
    # ps.wakati()
    ps.line_wakati()
    # ps.fix_english()
    # ps.fix_japanese()