def matchingStrings(strings, queries):
    
    # Can definitely be done faster with a hash map
    
    result = []
    
    for query in queries:
    
        counter = 0
        
        for string in strings:
            
            if query == string:
                
                counter += 1
            
        result.append(counter)
    
    return result