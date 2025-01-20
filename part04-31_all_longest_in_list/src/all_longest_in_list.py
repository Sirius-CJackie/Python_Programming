# Write your solution here
def all_the_longest(strings):
    max_length = max(len(string) for string in strings)
    longest_strings = [string for string in strings if len(string) == max_length]
    return longest_strings

if __name__ == '__main__':
    my_list1 = ["first", "second", "fourth", "eleventh"]
    print(all_the_longest(my_list1))  # Output: ['eleventh']

