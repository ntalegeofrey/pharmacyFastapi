# stack = []

# stack.append("a")
# stack.append("b")
# stack.append("c")

# print('inital Stack')

# print(stack)

# print('\nElement Pop from stack')
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())

# print("\nStack after elements are poped")
# print(stack)


# list_co = [5, 4, 3, 2, 1]

# for i in range(len(list_co)):
#     print("[{}]{}".format(i, list_co[i]))

from datetime import datetime, timedelta, date

# print(datetime.now() + timedelta(days=7))

today = date.today()
print(today)
week_ago = today - timedelta(days=7)
print(week_ago)
