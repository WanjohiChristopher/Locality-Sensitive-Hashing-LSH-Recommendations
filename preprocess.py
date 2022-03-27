#Preprocess will split a string of text into individual tokens/shingles based on whitespace.
def preprocess(text):
    text = re.sub(r'[^\w\s]','',text)#remove punctuation and special characters
    tokens = text.lower()
    tokens = tokens.split()
    return tokens

text = 'The devil went down to Georgia'
print('The shingles (tokens) are:', preprocess(text))

 # The shingles (tokens) are: ['the', 'devil', 'went', 'down', 'to', 'georgia']
#Number of Permutations
permutations = 128

#Number of Recommendations to return
num_recommendations = 1

def get_forest(data, perms):
    start_time = time.time()
    
    minhash = []
    
    for text in data['text']:
        tokens = preprocess(text)
        m = MinHash(num_perm=perms)
        for s in tokens:
            m.update(s.encode('utf8'))
        minhash.append(m)
        
    forest = MinHashLSHForest(num_perm=perms)
    
    for i,m in enumerate(minhash):
        forest.add(i,m)
        
    forest.index()
    
    print('It took %s seconds to build forest.' %(time.time()-start_time))
    
    return forest