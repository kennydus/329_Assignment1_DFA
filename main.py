states = {'start': [-1],  # Start State
          'k': [0],
          'e': [1],
          'n': [2, 3],
          'y': [4],

          'd': [5],
          'u': [6]
          }


def dfa(input_string):
    curr_state = -1
    for char in input_string:
        # Check if the character in the string is an accepted symbol.
        if char in states and (curr_state + 1 in states[char]):
            curr_state += 1

        # If we didn't get through the full first name...
        elif curr_state < 4:
            # If the sequence was interrupted by 'k', go to state 0.
            if char == 'k':
                curr_state = 0
            # If interrupted by another char, go to start state
            else:
                curr_state = -1

        # If we didn't get through the full last name...
        elif curr_state < 6:
            # If the sequence was interrupted by 'd', go to state 5.
            if char == 'd':
                curr_state = 5
            # If interrupted by another char, go to state 4.
            else:
                curr_state = 4

    # Accept state
    if curr_state == 6:
        return 'accept'
    else:
        return 'reject'


if __name__ == '__main__':
    input_strings = ['kennylasdhjckenduzxkc',   # Accept
                     'kennyxdu',                # Accept
                     'xxkennkennyasddux',       # Accept
                     'xkenkennyaddux',          # Accept
                     '',                        # Reject
                     'duxkenny'                 # Reject
                     ]
    for string in input_strings:
        print(f"'{string}': {dfa(string)}")

