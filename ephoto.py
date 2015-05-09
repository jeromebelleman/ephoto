def sibling(tag, key): # Duplicate from
    '''
    Return a key's sibling
    '''

    for i, child in enumerate(tag):
        if child.tag == 'key' and child.text == key:
            return tag[i + 1]
