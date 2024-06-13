# Write your solution here
def read_input(string,pre,post):
    while 1:
        user_input = input(string)
        try:
            number = int(user_input)
            if pre <= number <= post:
                return number
            else:
                print(f"You must type in an integer between {pre} and {post}")
        except ValueError:
            print(f"You must type in an integer between {pre} and {post}")

