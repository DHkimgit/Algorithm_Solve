def solution(my_string, queries):
    for i in queries:
        sub_string = my_string[i[0]:i[1] + 1]
        reverse = sub_string[::-1]
        my_string_list = list(my_string)

        for k in range(i[0], i[1]+1):
            my_string_list[k] = reverse[k - i[0]]

        my_string = ''.join(my_string_list)
    return my_string

print(solution("rermgorpsam", [[2, 3], [0, 7], [5, 9], [6, 10]]))