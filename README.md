# PascalSentenceDataset

This program is utility to download pascal sentence dataset.

## Instalation

You can install by "git clone" command

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

