# Write your solution here
def create_tuple(x: int, y: int, z: int):
    smallest = min(x, y, z)
    greatest = max(x, y, z)
    total_sum = x + y + z
    return (smallest, greatest, total_sum)