def finder(files, queries):
    file_dict = {} # {String: [String]}
    result = []
    
    for i in range(len(files)):
        name = ""
        for char in files[i]:
            if char == "/":
                name = ""
            else:
                name += char
        
        if name in file_dict:
            file_dict[name].append(files[i])
        else:
            file_dict[name] = [files[i]]
        
    
    for query in queries:
        if query in file_dict:
            for path in file_dict[query]:
                result.append(path)
    
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz',
        '/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
