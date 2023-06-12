# for decreasing order of cards
def locate_card(cards, query):
    lo, hi = 0, len(cards)-1
    print(lo, hi , query)
    count = 0
    while lo<= hi:
        count+=1
        mid = (lo+hi)//2
        mid_number = cards[(lo+hi)//2]
        print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number)
        if  mid_number== query:
            return print(f"position :  {mid} , min_attempts : {count}")
        elif cards[(lo+hi)//2] < query:
            hi = mid -1
        elif cards[(lo+hi)//2] > query:
            lo = mid +1
locate_card([13, 11, 10, 7, 4, 3, 1, 0], 13)