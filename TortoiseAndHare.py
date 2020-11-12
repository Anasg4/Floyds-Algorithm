def algorithm(value):
    try:
        tortoise = value[0]
        hare = value[0]
        while True:
            tortoise = value[tortoise]
            hare = value[value[hare]]
            if tortoise == hare:
                break

        meettortoise = value[0]
        meethare = hare
        while meettortoise != meethare:
            meettortoise = value[meettortoise]
            meethare = value[hare]
        print (f"Hare same position = {meethare} \nTortoise same position = {meettortoise}")
    except:
        print("There arent Duplicate Number in your List")

if __name__ == "__main__":
    print("Tortoise and Hare (Floyd's Algorithm)\n find duplicate number in your list ")
    list = []
    n = int(input("Enter number of list elements : "))
    for i in range(n):
        ele = int(input("input your value : "))
        list.append(ele)
    print(f"\nYour List >> {list}\n")
    algorithm(list)
