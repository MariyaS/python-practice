"""Count words."""

def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    
    # Count the number of occurences of each word in s
    words = s.split()
    dic = {}
    for word in words: 
        dic[word] = words.count(word)
    # Sort the occurences in descending order (alphabetically in case of ties)
    # Return the top n words as a list of tuples (<word>, <count>)
    N = int(n)
    top_n = sorted(dic.iteritems(), key = lambda(k,v):(-v,k))[:N]
    return top_n


def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)


if __name__ == '__main__':
    test_run()
