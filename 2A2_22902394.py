
def proper_capitalization(sentence):
    return sentence.lower()

def stop_word_removal(sentence, stop_words):
    tokens = sentence.split()
    stoplist = stop_words.split()
    tokens_filtered = [word for word in tokens if not word in stoplist] 
    return (" ").join(tokens_filtered)

def remove_punc(sentence, punctuation):

    sen_list = sentence.split(" ")
    sentence = ""
    for i in sen_list:
        i = i.rstrip(punctuation)
        i += " "
        sentence += i
    sentence.strip()

    return sentence

def remove_duplicate_words(sentence):
    result = ""
    sen_list = sorted(sentence.split())
    for i in sen_list:
        i += " "
        if i not in result:
            result += i
    return result

def cleaning_noise(sentence):
    
    def replace_amp(sentence):
        new = sentence.replace("&amp", "&").replace("\n", " ")
        return new

    def remove_https(sentence):
        s_lst = sentence.split()
        sent = ""   
        for word in s_lst:
            if "http" not in word:
                word += " "
                sent += word
        return sent

    def remove_hashtag(sentence):
        s_lst = sentence.split()
        sent = ""    
        for word in s_lst:
            if "#" not in word:
                word += " "
                sent += word
        return sent
    
    def odd_atsign(sentence):
        s_lst = sentence.split()
        at_list = []
        sent = ""
        for word in s_lst:
            if "@" in word:
                at_list.append(word)
        del at_list[1::2]
        for word in s_lst:
            if word not in at_list:
                word += " "
                sent += word
        return sent
    
    sentence = replace_amp(sentence)
    sentence = remove_https(sentence)
    sentence = remove_hashtag(sentence)
    sentence = odd_atsign(sentence)
    
    return sentence

def pos(sentence):
    
    if not isinstance(sentence, str):
        return "your input is not a string. Terminating..."
  

    
    s_list = sentence.split()
    
    s = ""

    
    for word in s_list:
        is_done = False
        while not is_done:
            
            if word.endswith("sses"):
                word = word[0: len(word)-2]
            
            elif word.endswith("'s") or word.endswith("s'"):
                word = word[0: len(word)-2]
            
            elif word.endswith("ies") and len(word) >= 5:
                word = word[0: len(word)-2]
            elif word.endswith("ies") and len(word) <= 5:
                word = word[0: len(word)-1]

                    
            elif word.endswith("s"):
                has_vowels = False
                for char in word:
                    if char in ('a', 'e', 'i', 'o', 'u', 'y'):
                        has_vowels = True
                    elif char in ('A', 'E', 'I', 'O', 'U', 'Y'):
                        has_vowels = True
                seclast_vowel = True
                try:
                    if word[-2] not in "aeiouyAEIOUY":
                        seclast_vowel = False
                    else: seclast_vowel = True
                except IndexError:
                    word = word[0:-1]

                if not word.endswith("us") and not word.endswith("ss") and has_vowels is True and seclast_vowel is False:
                    
                    try:
                        word = word[0: len(word)-1]
                    except IndexError:
                        word = word[0: -1]
                else: 
                    pass

    
    
            if word.endswith("ied"):
                word = word[0: len(word)-2]
                if len(word) <= 2:
                    word = word + "e"
                    
            elif word.endswith("ed"):
                word = word[0: len(word)-2]
    
            elif word.endswith("er"):
                word = word[0: len(word)-2]
    
            elif word.endswith("ing") and len(word) >= 6:
                word = word[0: len(word)-3]

    
            elif word.endswith("ly"):
                word = word[0: len(word)-2]
                
            else:
                is_done = True

        word += " "
        s += word
        
    return s

def tweet_analysis():
    
    input_file = str(input('Enter the name of the file to read: '))
    output_filename = str(input('Enter the name of the file to write: '))
    stop_words = str(input('Enter your stopwords: '))
    punctuation = str(input('Enter your punctuations to remove: '))
    
    def load_data(input_file):
        
        result = []
        output_file = open(output_filename, "w", encoding = "utf-8")
        data = open(input_file, encoding = "utf-8")
        for line in data:
            
            line = line.strip(" ")
            line = line[0:-1]
            
            line = proper_capitalization(line)
            line = stop_word_removal(line, stop_words)
            line = remove_punc(line, punctuation)
            line = remove_duplicate_words(line)
            line = cleaning_noise(line)
            line = pos(line)
            
            result.append(line)
            output_file.write(line)
            
        data.close()
        output_file.close()
        return result
            
    return load_data(input_file)


def word_ranking(corpus, n):
    s = ""
    for words in corpus:
        words += " "
        s += words
    
    nodup = remove_duplicate_words(s)
    nodup_list = sorted(nodup.split())
    s_list = s.split()
    freq_list = []
    
    for word in nodup_list:
        num_freq = s_list.count(word)
        freq_list.append(num_freq)
        
    tuple_list = [[nodup_list[i], freq_list[i]] for i in range(0,len(freq_list))]
    
    while len(tuple_list) > n:
        min_freq = min(freq_list)
        freq_list.remove(min_freq)
        for tup in tuple_list:
            if min_freq in tup:
                tuple_list.remove(tup)
                
                
    result = []
    for lst in tuple_list:
        result.append(tuple(lst))
    
    return result


        
    