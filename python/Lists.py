#1
def select_second(L):
    """Return the second element of the given list. If the list has no second
    element, return None.
    """
    if len(L)>1:
        return L[1]
    else:
        return None
# Check your answer
q1.check()

#2
def losing_team_captain(teams):
    """Given a list of teams, where each team is a list of names, return the 2nd player (captain)
    from the last listed team
    """
    # lastTeam = (teams.pop)
    # name = lastTeam[1]
    return teams[-1][1]

# Check your answer
q2.check()

#3
def purple_shell(racers):
    """Given a list of racers, set the first place racer (at the front of the list) to last
    place and vice versa.
    
    >>> r = ["Mario", "Bowser", "Luigi"]
    >>> purple_shell(r)
    >>> r
    ["Luigi", "Bowser", "Mario"]
    """
    racers[0], racers[-1] = racers[-1], racers[0]
    # a,b = b, a

# Check your answer
q3.check()

#4
a = [1, 2, 3]
b = [1, [2, 3]]
c = []
d = [1, 2, 3][1:]

# Put your predictions in the list below. Lengths should contain 4 numbers, the
# first being the length of a, the second being the length of b and so on.
lengths = [3, 2, 0, 2]

# Check your answer
q4.check()

# Put your predictions in the list below. Lengths should contain 4 numbers, the
# first being the length of a, the second being the length of b and so on.
lengths = [2, 1, None, d]

# Check your answer
q4.check()


#5
def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    index = arrivals.index(name)
    half = (len(arrivals) - 1) // 2
    return index > half and index != len(arrivals) - 1
    
# Check your answer
q5.check()