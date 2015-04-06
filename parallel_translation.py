__author__ = 'rupy'

import csv

# parallel translation (Jaoanese & English) file is needed in this program

class ParallelTranslation():

    def __init__(self, csv_file_path):
        self.translation_path = csv_file_path


    def read_csv_and_save_as_txt(self):
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

if __name__=="__main__":

    csv_file = 'parallel_translation/pascal_sentence_numbers.csv'
    ps = ParallelTranslation(csv_file)
    ps.read_csv_and_save_as_txt()