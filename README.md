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
requests 2.6.0
```

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
# create correspondence data by dataset
dataset.create_correspondence_data()
```

That's it!

## Additional information for Nakayama lab members

Our lab created Japanese translation of Pascal Sentence Dataset.
Translation class is the utility to use parallel translation data, "pascal_sentence_numbers.csv".
You can get text files of two languages by the class.
To use the class, you have to install depencency libraries as follow:

```
mecab-python 0.996
```

To use mecab-python, you have to install MeCab in addition.

### Code Sample

```python
# import
from translation import Translation

# put parallel translation data somewhere in advance
csv_file = 'translations/pascal_sentence_numbers.csv'
# initialize instance
ps = Translation(csv_file)
# create text data from csv file
ps.read_csv_and_save_as_txt()
# create wakati-gaki text data (Japanese text data separated by space between each word)
ps.wakati()
```


