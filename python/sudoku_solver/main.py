import numpy as np

def print_board(board):
    for i in board:
        for j in i:
            print(j, end="  ")
        print()

def insert_num(board, num, x, y):
    b_l = 3
    b_x = (int(x/len(board))) * b_l
    b_y = (int(y/len(board))) * b_l

    if (num in board[b_x:b_x+b_l, b_y:b_y+b_l] or
        num in board[x, :] or
        num in board[:, y]):
        return False

    board[x, y] = num
    return True

def inc_mov(m):
    return (m % 9) + 1

def setup_boards(s)


def main():
    board_len = 9
    block_len = 3
    s_board = np.zeros((board_len,board_len), dtype=int)
    m_board = np.zeros((board_len,board_len), dtype=int)

    row, col = 0
    mov = 1
    while row < board_len:
        while col < board_len:
            if s_board[row,col] != 0:
                if #there is a valid, make it:

                else #otherwise, go back a move:
                    if col

            


if __name__ == "__main__":
    main()