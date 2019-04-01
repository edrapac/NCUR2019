from keras_wc_embd import get_dicts_generator
#pip install --upgrade --force-reinstall numpy==1.16 if you get import errors
sentences = [
    ['All', 'work', 'and', 'no', 'play'],
    ['makes', 'Jack', 'a', 'dull', 'boy', '.'],
]
dict_generator = get_dicts_generator(
    word_min_freq=2,
    char_min_freq=2,
    word_ignore_case=False,
    char_ignore_case=False,
)
for sentence in sentences:
    dict_generator(sentence)
    print(dict_generator(sentence))
word_dict, char_dict, max_word_len = dict_generator(return_dict=True)

for keys,values in word_dict.items():
	print(keys,values)