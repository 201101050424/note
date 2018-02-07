# encoding=utf-8
import numpy as np
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences


all_tex = np.array(['a', 'b', 'c', 'd', 'e', 'f'])
tokenizer = Tokenizer(num_words=100)
tokenizer.fit_on_texts(all_tex)

seq = np.array(['e f', 'c d e'])
seq = tokenizer.texts_to_sequences(seq)
print seq
"""
[[5, 6], [3, 4, 5]]
"""

seq = pad_sequences(seq, maxlen=5)
print seq
"""
[[0 0 0 5 6]
 [0 0 0 3 4]]
"""
