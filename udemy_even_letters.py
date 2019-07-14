# go through the string below and if the lenght of a word is even print "even!:

st = 'Print every word in this sentence that has an even number of letters'

for word in st.split():
    if len(word) % 2 == 0:
        print(word+ ' is even!')
