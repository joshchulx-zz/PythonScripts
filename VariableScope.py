def word_count(document, search_term):
    """Count how many times search_term appears in document"""
    words = document.split()
    answer = 0
    for word in words:
        if word == search_term:
            answer += 1
    return answer


def nearest_square(limit):
    """Find the largest ssquare number smaller than limit."""
    answer = 0
    while (answer+1)**2 <limit:
        answer += 1
    return answer**2


"""These two functions word_count and nearest_square both include a answer variable, but the are 
distinct variables that only exist within their respective functions"""