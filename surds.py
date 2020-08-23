def to_full_form(number_of_root, root_of, return_as_square_root=True):
    if type(number_of_root) != int or type(root_of) != int:
        raise ValueError("Both values must be integers.")
    if root_of < 0 or number_of_root < 0:
        raise ValueError("Root of and number of root cannot be negative.")

    answer_in_root = number_of_root ** 2 * root_of
    if return_as_square_root:
        return answer_in_root
    return (number_of_root ** 2 * root_of) ** 0.5


class SurdSimplifier:
    filtered = []

    def __init__(self):
        unfiltered = open("perfects.txt", "r").readlines()
        unfiltered.pop(0)
        for line in unfiltered:
            self.filtered.append(int(line.split(",")[1].split(",")[0].strip()))

    def to_simple_form(self, root_of):
        if root_of < 0:
            raise ValueError("root_of cannot be negative.")
        if type(root_of) != int:
            raise ValueError("root_of must be an integer.")
        perfect_squares = self.filtered
        index = 2
        current_sq_num = 0
        divided = 0
        for square in perfect_squares:
            if root_of <= square:
                if current_sq_num == 0 and divided == 0:
                    return 1, root_of
                return int(current_sq_num ** 0.5), int(divided)
            if root_of % square == 0:
                current_sq_num = square
                divided = root_of/square
            index += 1


ss = SurdSimplifier()
print(ss.to_simple_form(50))
print(to_full_form(5, 3))

