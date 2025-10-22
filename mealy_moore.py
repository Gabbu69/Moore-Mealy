class MooreState:
    def __init__(self, name, output):
        self.name = name          # State name (A, B, C)
        self.output = output      # Output for this state
        self.transitions = {}     # Transitions (input -> next_state)

    def add_transition(self, input_symbol, next_state):
        self.transitions[input_symbol] = next_state


class MooreMachine:
    def __init__(self):
        self.states = {
            'A': MooreState('A', 'b'),
            'B': MooreState('B', 'b'),
            'C': MooreState('C', 'a')
        }

        self.states['A'].add_transition('0', 'B')
        self.states['A'].add_transition('1', 'A')
        self.states['B'].add_transition('1', 'C')
        self.states['B'].add_transition('0', 'A')
        self.states['C'].add_transition('0', 'B')
        self.states['C'].add_transition('1', 'B')

        self.current_state = self.states['A']

    def process_input(self, input_string):
        print("\n========================")
        print("MOORE MACHINE EXECUTION")
        print("========================")
        output = ''
        print(f"{'Input':<6}{'State':<6}{'Output'}")

        for symbol in input_string:
            print(f"{symbol:<6}{self.current_state.name:<6}{self.current_state.output}")
            output += self.current_state.output
            self.current_state = self.states[self.current_state.transitions[symbol]]

        # Add output from final state
        print(f"{'':<6}{self.current_state.name:<6}{self.current_state.output}")
        output += self.current_state.output

        print(f"\nFinal Output: {output}")
        return output


class MealyState:
    def __init__(self, name):
        self.name = name
        self.transitions = {}  # input -> (next_state, output)

    def add_transition(self, input_symbol, next_state, output):
        self.transitions[input_symbol] = (next_state, output)


class MealyMachine:
    def __init__(self):
        self.states = {
            'A': MealyState('A'),
            'B': MealyState('B')
        }

        self.states['A'].add_transition('0', 'B', 'b')
        self.states['A'].add_transition('1', 'A', 'b')
        self.states['B'].add_transition('0', 'B', 'b')
        self.states['B'].add_transition('1', 'A', 'a')

        self.current_state = self.states['A']

    def process_input(self, input_string):
        print("\n========================")
        print("MEALY MACHINE EXECUTION")
        print("========================")
        output = ''
        print(f"{'Input':<6}{'State':<6}{'Output'}")

        for symbol in input_string:
            next_state, out = self.current_state.transitions[symbol]
            print(f"{symbol:<6}{self.current_state.name:<6}{out}")
            output += out
            self.current_state = self.states[next_state]

        print(f"\nFinal Output: {output}")
        return output


# ------------------------------
# MAIN PROGRAM
# ------------------------------
if __name__ == "__main__":
    print("=== Finite State Machine Simulator ===")
    print("This program detects the pattern '01' using Moore and Mealy Machines.")
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        user_input = input("Enter binary string (e.g. 10101): ").strip()

        if user_input.lower() in ['exit', 'quit']:
            print("Program terminated. Goodbye!")
            break

        if not all(ch in '01' for ch in user_input):
            print("Invalid input! Please enter only 0s and 1s.\n")
            continue

        # Run Moore Machine
        moore = MooreMachine()
        moore.process_input(user_input)

        # Run Mealy Machine
        mealy = MealyMachine()
        mealy.process_input(user_input)

        print("\n-----------------------------------\n")
