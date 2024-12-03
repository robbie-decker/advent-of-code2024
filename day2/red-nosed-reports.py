# Get input
# Transition input to lists
# Check to make sure lists are either decreasing or increasing
# Can only increase/ decrease by a value of 1-3

# Return: how many reports are safe?

class ListNode:
    def __init__(self, x):
        self.val = int(x)
        self.next = None

def list2link(lst):
    cur = dummy = ListNode(0)
    for e in lst:
        cur.next = ListNode(e)
        cur = cur.next
    return dummy.next

total = 0
with open("input.txt", 'r') as file:
    for line in file:
        report = line.split()
        linked_list_report = list2link(report)

        isSafe = True

        # while linked_list_report:
        #     print(linked_list_report.val)
        #     linked_list_report = linked_list_report.next

        if sorted(report) != report:
            isSafe = False

        cur = linked_list_report
        while cur.next and isSafe:
            # Checking if the list is increasing or decreasing by 1-3
            largerValue = max(cur.val, cur.next.val)
            smallerValue = min(cur.val, cur.next.val)
            # print(f'larger: {largerValue}      smaller: {smallerValue}')
            if not (largerValue - smallerValue) <= 3 or (largerValue - smallerValue) == 0:
                isSafe = False

            cur = cur.next
        
        if isSafe:
            print(report)
            total += 1

print(total)
            
            

            



