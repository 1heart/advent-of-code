from d5 import intcode

acs = [3,8,1001,8,10,8,105,1,0,0,21,42,67,84,109,126,207,288,369,450,99999,3,9,102,4,9,9,1001,9,4,9,102,2,9,9,101,2,9,9,4,9,99,3,9,1001,9,5,9,1002,9,5,9,1001,9,5,9,1002,9,5,9,101,5,9,9,4,9,99,3,9,101,5,9,9,1002,9,3,9,1001,9,2,9,4,9,99,3,9,1001,9,2,9,102,4,9,9,101,2,9,9,102,4,9,9,1001,9,2,9,4,9,99,3,9,102,2,9,9,101,5,9,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,99]
def run_acs(phase, input_signal):
    output_signal = intcode(acs.copy(), [phase, input_signal])
    return output_signal

def run_phases(phases):
    output = 0
    for phase in phases:
        output = next(run_acs(phase, output))
    return output
    
def find_max(phases_left, phases_so_far, run_phases_func):
    if not phases_left:
        return run_phases_func(phases_so_far)
    max_so_far = float("-inf")
    for i, phase in enumerate(phases_left):
        max_so_far = max(
            max_so_far,
            find_max(
                phases_left[:i] + phases_left[i+1:],
                phases_so_far + [phase],
                run_phases_func,
            )
        )
    return max_so_far

def run_phases_feedback(phases):
    input_lists = [[phase] for phase in phases]
    generators = [intcode(acs.copy(), input_list) for input_list in input_lists]

    input_lists[0].append(0)

    i = 0
    while True:
        next_i = (i + 1) % len(phases)
        try:
            output = next(generators[i])
        except Exception as e:
            break
        input_lists[next_i].append(output)
        i = next_i
    return output


if __name__ == "__main__":
    # phases = [0,1,2,3,4]
    # print(run_phases(phases))
    print(find_max([0, 1, 2, 3, 4], [], run_phases))

    # phases = [9,7,8,5,6]
    # print(run_phases_feedback(phases))
    print(find_max([5,6,7,8,9], [], run_phases_feedback))
