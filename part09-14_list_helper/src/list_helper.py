# WRITE YOUR SOLUTION HERE:
class ListHelper:
    @classmethod
    def greatest_frequency(cls, my_list):
        return max(set(my_list), key = my_list.count)
    @classmethod
    def doubles(cls, my_list):
        unique_items = set(my_list)
        count = 0
        for item in unique_items:
            if my_list.count(item) >= 2:
                count += 1
        return count