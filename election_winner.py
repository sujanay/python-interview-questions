# dictionary of votes
def election_winner(votes):
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

    max_vote = max(counter.values())
    max_counter = {}

    for i in counter:
        if counter[i] == max_vote: max_counter[i] = counter[i]
    
    return counter, sorted(max_counter.keys())[-1]

election_votes = ['mary', 'bill', 'joe', 'bill', 'tim', 'joe', 'mary']

counter, winner = election_winner(election_votes)
print("Votes Count:", counter)
print("Election Winner:", winner)