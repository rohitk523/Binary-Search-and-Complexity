# for decreasing order of cards
def locate_card(cards, query):
    lo, hi = 0, len(cards)-1
    count = 0
    while lo<= hi:
        count+=1
        mid = (lo+hi)//2
        mid_number = cards[(lo+hi)//2]
        if  mid_number== query:
            return mid
        elif cards[(lo+hi)//2] < query:
            hi = mid -1
        elif cards[(lo+hi)//2] > query:
            lo = mid +1
    return -1
        