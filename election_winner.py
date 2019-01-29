# dictionary of votes
votes = ['sujan', 'jiya', 'sujan', 'sujan', 'jiya', 'sana', 'sana', 'sana', 'buda', 'buda', 'buda']

def vote_counter():
    """
        returns the vote count of each candidate
    """
    # to count the number of votes for each person
    counter = {}

    # for each vote in votes, if the counter has the person registered then
    # increase the counter by 1 otherwise set the person and have it's count 1
    for vote in votes:
        if vote in counter:
            counter[vote]+= 1
        else: counter[vote] = 1

    print(counter)

    return counter

