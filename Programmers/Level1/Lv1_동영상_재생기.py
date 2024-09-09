def solution(video_len, pos, op_start, op_end, commands):
    video_len_min = int(video_len[0:2])
    video_len_sec = int(video_len[3:5])
    current_min = int(pos[0:2])
    current_sec = int(pos[3:5])
    op_start_min = int(op_start[0:2])
    op_start_sec = int(op_start[3:5])
    op_end_min = int(op_end[0:2])
    op_end_sec = int(op_end[3:5])

    for i in commands:
        if(op_start_min * 60 + op_start_sec <=current_min * 60 + current_sec <= op_end_min * 60 + op_end_sec):
            current_min = op_end_min
            current_sec = op_end_sec
        if(i == "prev"):
            if (current_min == 0 and current_sec <= 10):
                current_min = 0
                current_sec = 0
            elif (current_min != 0 and current_sec < 10):
                current_min -= 1
                current_sec = current_sec + 60 - 10
            else:
                current_sec -= 10
        elif(i == "next"):
            if (video_len_min * 60 + video_len_sec - 10 <= current_min * 60 + current_sec <= video_len_min * 60 + video_len_sec):
                current_min = video_len_min
                current_sec = video_len_sec
            elif (current_min != video_len_min and current_sec >= 50):
                current_min += 1
                current_sec = current_sec - 50
            else:
                current_sec += 10
        if(op_start_min * 60 + op_start_sec <=current_min * 60 + current_sec <= op_end_min * 60 + op_end_sec):
            current_min = op_end_min
            current_sec = op_end_sec
    
    if 0 <= current_min < 10:
        answer_min = '0' + str(current_min)
    else:
        answer_min = str(current_min)
    if 0 <= current_sec < 10:
        answer_sec = '0' + str(current_sec)
    else:
        answer_sec = str(current_sec)
    
    return answer_min + ':' + answer_sec