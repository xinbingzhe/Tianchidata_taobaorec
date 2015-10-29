def count_term_match(test_term,match_term):
    count = 0
    for tt in test_term:
        if tt!='':
            count = count + match_term.count(tt)
    return count
