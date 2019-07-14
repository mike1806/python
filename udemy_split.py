# use for, .split(), and if to create Statement that will print out words that start with 's'

st = 'Print only the words that start with s in this statement'

for word in st.split():
    if word[0] == 's':
        print(word)