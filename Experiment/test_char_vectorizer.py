from CharVectorizer import CharVectorizer
vectorizer = CharVectorizer("abcdefghijklmnopqrstuvwxyz1234567890")

windows = ["miller"] #words to vectorize

target_length = max(len(window) for window in windows) #makes sure we have the max length string, any string less than this length gets padded

matrix = vectorizer.transform(windows,target_length) # give it the strings to vectorize as well as the max length for any padding issues

print((matrix).shape)