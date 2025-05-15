class Turing_Machine:
    def __init__(self, tape, transitions, start_state, blank='#'):
        self.tape = list(tape) + [blank] * 2
        self.transitions = transitions
        self.head = 0
        self.state = start_state
        self.blank = blank
        self.direction = ''

    def print_tape(self):
        tape_str = ''.join(self.tape)
        head_str = ' ' * self.head + '🔻'
        print(f"الشريط: {tape_str}")
        print(f"         {head_str}")
        print(f"الحالة: {self.state}\n")

    def step(self):
        symbol = self.tape[self.head]
        key = (self.state, symbol)

        if key in self.transitions:
            new_state, new_symbol, self.direction = self.transitions[key]
            self.tape[self.head] = new_symbol
            self.state = new_state
            self.head += 1 if self.direction == 'R' else -1
        else:
            self.direction = 'N'

    def run(self, max_steps=1000):
        steps = 0
        while self.direction != 'N' and self.direction != 'Y' and steps < max_steps:
            self.print_tape()
            self.step()
            steps += 1
        self.print_tape()
        return self.direction == 'Y'


transitions = {
    # {1, 0, #} only

    # q0  => start state
    ('q0', '0'): ('q1', '#', 'R'),
    ('q0', '1'): ('q2', '#', 'R'),
    ('q0', '#'): ('q0', '#', 'Y'),

    # q2  reach to last element
    ('q2', '0'): ('q2', '0', 'R'),
    ('q2', '1'): ('q2', '1', 'R'),
    ('q2', '#'): ('q3', '#', 'L'),

    # q3 after reach last decision
    ('q3', '1'): ('q4', '#', 'L'),
    ('q3', '0'): ('q3', '0', 'N'),
    ('q3', '#'): ('q0', '#', 'R'),

    # q4 => to reset head to first element
    ('q4', '0'): ('q4', '0', 'L'),
    ('q4', '1'): ('q4', '1', 'L'),
    ('q4', '#'): ('q0', '#', 'R'),

    # q1  reach to last element
    ('q1', '0'): ('q1', '0', 'R'),
    ('q1', '1'): ('q1', '1', 'R'),
    ('q1', '#'): ('q5', '#', 'L'),

    # q5 after reach last decision
    ('q5', '0'): ('q4', '#', 'L'),
    ('q5', '1'): ('q5', '1', 'N'),
    ('q5', '#'): ('q0', '#', 'R'),

}


def IsBinary_Palindrome(str):
    if (all(x in '01' for x in str)):  # check the string have 0's , 1's only
        tm = Turing_Machine(str, transitions, 'q0')
        return tm.run()
    return False  # if str contain another char


IsBinary_Palindrome("1001")

# *********************************TO TEST***************************************#
# test_cases = [
# ("0", True),
# ("1", True),
# ("00", True),
# ("11", True),
# ("01", False),
# ("10", False),
# ("010", True),
# ("011", False),
# ("1001", True),
# ("1010", False),
# ("11011", True),
# ("11111", True),
# ("101101", True),
# ("101010", False),
# ("", True),  # empty string case  ==> ("#", True)
# ("001100", True),
# ("1011010", False),
# ("1001#", False),
# ("10#01", False)
# ]

# print("Testing binary palindrome checker:")
# for input_str, expected in test_cases:
#     result = IsBinary_Palindrome(input_str)
#     print(f"'{input_str}': {'PASS' if result == expected else 'FAIL'} (Expected: {expected}, Got: {result})")
