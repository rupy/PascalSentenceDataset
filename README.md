# PascalSentenceDataset

This program is utility to download pascal sentence dataset.

## Instalation

You can install by "git clone" command.

```
git clone https://github.com/rupy/PascalSentenceDataset.git
```

### Dependency

You must install some python libraries. Use pip command.

```
pyquery 1.2.9
mecab-python 0.996
requests 2.6.0
```

To use mecab-python, you have to install MeCab in addition.

## Usage

To download dataset, run program as follow:
```python
# import
from pascal_sentence_dataset import PascalSentenceDataSet

# create instance
dataset = PascalSentenceDataSet()
# download images
dataset.download_images()
# download sentences
dataset.download_sentences()
# create coresoindence data by dataset
dataset.create_correspondence_data()
```

That's it!

## Information for Nakayama lab members

Our lab created Japanese translation of Pascal Sentence.

Translation class is the utility to use parallel translation data, "pascal_sentence_numbers.csv".

```python
# import
from translation import Translation

# put parallel translation data somewhere
csv_file = 'translations/pascal_sentence_numbers.csv'
# initialize instance
ps = Translation(csv_file)
# create text data from csv file
ps.read_csv_and_save_as_txt()
# create wakati-gaki text data (Japanese text data separated by space between each word).
ps.wakati()
# create wakati-gaki text data retaining line break
ps.line_wakati()
# fix english data created by read_csv_and_save_as_txt() because the data contains weird line break
ps.fix_english()
# fix japanese data created by read_csv_and_save_as_txt() because the data contains weird line break
ps.fix_japanese()
```


