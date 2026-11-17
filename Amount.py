# target sum backtracking algorithm
def amount(nums_list, target_sum):
    result = []
    current = []

    amount_builder(nums_list, target_sum, result,
                   current, 0, 0)

    return result



def amount_builder(nums_list, target_sum, result,
                   current, start, current_sum):

    # Base case: found a valid combination
    if current_sum == target_sum:
        result.append(current.copy())
        return

    # Base case: exceeded the target
    if current_sum > target_sum:
        return

    for i in range(start, len(nums_list)):

        if i > start and nums_list[i] == nums_list[i - 1]:
            continue

        # Choose a number
        current.append(nums_list[i])

        # Recursively explore
        amount_builder(nums_list, target_sum, result,
                       current, i + 1,
                       current_sum + nums_list[i])

        # Backtrack
        current.pop()








#nums_list = [11,1,3,2,6,1,5]
#target_sum = 8

#print(amount(nums_list,target_sum))
