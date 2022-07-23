first_line_press_case = [101] * (2 ** 10)
for case in range(2 ** 10):
    tmp_board = [board[i][:] for i in range(10)]  # copy board to tmp board
    cnt = 0

    # set case
    mask = 1
    for j in range(9, -1, -1):
        if case & mask:
            press(tmp_board, 0, j)
            cnt += 1
        mask <<= 1

    for i in range(1, 10):
        for j in range(10):
            if tmp_board[i - 1][j]:  # 현재 위치 위에 전구가 켜져있으면
                press(tmp_board, i, j)  # 현재 위치 press
                cnt += 1

    # 만일 마지막줄 전구 다 꺼져있으면 성공!
    if sum(tmp_board[9]) == 0:
        first_line_press_case[case] = cnt