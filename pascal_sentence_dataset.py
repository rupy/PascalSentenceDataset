# -*- coding: utf-8 -*-

from urlparse import urljoin
from pyquery import PyQuery as pq
from pprint import pprint
import os
import requests

__author__ = 'rupy'

class PascalSentenceDataSet():

    DATASET_DIR = 'dataset/'
    SENTENCE_DIR = 'sentence/'

    def __init__(self, url):
        self.url = url

    def download_images(self):
        dom = pq(self.url)
        for img in dom('img').items():
            img_src = img.attr['src']
            category, img_file_name = os.path.split(img_src)

            # make category directories
            output_dir = PascalSentenceDataSet.DATASET_DIR + category
            if not os.path.isdir(output_dir):
                os.mkdir(output_dir)

            # download image
            output = os.path.join(output_dir, img_file_name)
            print output
            if img_src.startswith('http'):
                img_url = img_src
            else:
                img_url = urljoin(url, img_src)
            if os.path.isfile(output):
                print "Already downloaded, Skipping: %s" % output
                continue
            print "Downloading: %s" % output
            with open(output,'wb') as f:
                raw = requests.get(img_url).content
                f.write(raw)

    def download_sentences(self):
        dom = pq(self.url)
        # tbody disappears in pyquery DOM
        for tr in dom('body>table>tr').items():
            img_src = tr('img').attr['src']
            category, img_file_name = os.path.split(img_src)

            # make category directories
            output_dir = PascalSentenceDataSet.SENTENCE_DIR + category
            if not os.path.isdir(output_dir):
                os.mkdir(output_dir)

            # dowonload sentences
            head, tail = os.path.splitext(img_file_name)
            sentence_file_name = head + "txt"
            output = os.path.join(output_dir, sentence_file_name)
            if os.path.isfile(output):
                print "Already downloaded, Skipping: %s" % output
                continue
            print "Downloading: %s" % output
            with open(output,'w') as f:
                for td in tr('table tr td').items():
                    f.write(td.text() + "\n")

if __name__=="__main__":

    url = "http://vision.cs.uiuc.edu/pascal-sentences/"
    dataset = PascalSentenceDataSet(url)
    # dataset.download_images()
    dataset.download_sentences()
