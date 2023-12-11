def reverseShuffleMerge(s):
    # Total character counts in s
    char_count = Counter(s)
    
    # Character counts we need in our final string
    string_chars = { 
        char: int(count / 2) for char, count in char_count.items() 
    }
        
    # Character counts we need in the shuffled 
    # version of our original string 
    shuffled_chars = { 
        char: int(count / 2) for char, count in char_count.items() 
    }
    
    string = []
		
    for char in reversed(s):
        if string_chars[char] > 0:
            # See if this character should appear before any 
            # previous ones. Basically, if this char is smaller 
            # than the previous char, and the previous char 
            # still occurs in the chars of the shuffled string, 
            # we can the safely replace the previous char 
            # with this one. That's so because we should be 
            # able to still create a valid string which contains
            # both characters although the order will differs.
            while string and string[-1] > char and shuffled_chars[string[-1]] > 0:
                removed = string.pop()
                string_chars[removed] += 1
                shuffled_chars[removed] -= 1
            
            string.append(char)
            string_chars[char] -= 1
        else:
            shuffled_chars[char] -= 1

    return ''.join(string)