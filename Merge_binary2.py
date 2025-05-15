class TuringMachine:
    def __init__(self, tape, transitions, start_state, blank='#'):
        self.tape = list(tape) + [blank] * 2  # Initialize with extra blanks
        self.transitions = transitions
        self.head = 0
        self.state = start_state
        self.blank = blank
        self.direction = ''

    def step(self):
        symbol = self.tape[self.head]
        key = (self.state, symbol)

        if key in self.transitions:
            new_state, new_symbol, self.direction = self.transitions[key]
            self.tape[self.head] = new_symbol
            self.state = new_state
            self.head += 1 if self.direction == 'R' else -1
        else:
            self.direction = 'N'  # No transition found

    def run(self, max_steps=1000):
        steps = 0
        while self.direction != 'N' and steps < max_steps:
            self.print_tape()
            self.step()
            steps += 1
        self.print_tape()
        print(f"Finished in {steps} steps")
        return ''.join([c for c in self.tape if c != self.blank and c != 'x'])

    def print_tape(self):
        tape_str = ''.join(self.tape)
        head_str = ' ' * self.head + '🔻'
        print(f"Tape: {tape_str}")
        print(f"      {head_str}")
        print(f"State: {self.state}\n")


transitions = {

    ('q0', '0'): ('q0', '0', 'R'),
    ('q0', '1'): ('q0', '1', 'R'),
    ('q0', '#'): ('q1', '#', 'R'),
    # important trans
    ('q1', '0'): ('q2', '#', 'L'),
    ('q1', '1'): ('q3', '#', 'L'),
    ('q2', '#'): ('q0', '0', 'R'),
    ('q3', '#'): ('q0', '1', 'R'),
    # accept state
    ('q1', '#'): ('q4', '#', 'Y'),
    # dead state
    ('q2', '0'): ('q5', '0', 'N'),
    ('q2', '1'): ('q5', '1', 'N'),
    ('q3', '0'): ('q5', '0', 'N'),
    ('q3', '1'): ('q5', '1', 'N'),

}


if __name__ == "__main__":
    input_tape = "10101"
    tm = TuringMachine(input_tape, transitions, 'q0')
    result = tm.run()
    print(f"\nFinal merged binary: {result}")
