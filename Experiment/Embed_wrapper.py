import keras
import numpy as np
from keras_wc_embd import WordCharEmbd

sentences = [
    ['All', 'work', 'and', 'no', 'play'],
    ['makes', 'Jack', 'a', 'dull', 'boy', '.'],
]
wc_embd = WordCharEmbd(
    word_min_freq=0,
    char_min_freq=0,
    word_ignore_case=False,
    char_ignore_case=False,
)
for sentence in sentences:
    wc_embd.update_dicts(sentence)

inputs, embd_layer = wc_embd.get_embedding_layer()
lstm_layer = keras.layers.LSTM(units=5, name='LSTM')(embd_layer)
softmax_layer = keras.layers.Dense(units=2, activation='softmax', name='Softmax')(lstm_layer)
model = keras.models.Model(inputs=inputs, outputs=softmax_layer)
model.compile(
    optimizer='adam',
    loss=keras.losses.sparse_categorical_crossentropy,
    metrics=[keras.metrics.sparse_categorical_accuracy],
)
model.summary()


def batch_generator():
    while True:
        yield wc_embd.get_batch_input(sentences), np.asarray([0, 1])

model.fit_generator(
    generator=batch_generator(),
    steps_per_epoch=200,
    epochs=1,
)