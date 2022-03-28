import sys
read = sys.stdin.readline


def solution(n, board):
    ans = max(1, max([max(check_row(n, board, r, c), check_col(n, board, r, c))
                      for r in range(n) for c in range(n)]))
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for r in range(n):
        for c in range(n):
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < n and 0 <= nc < n and \
                        board[r][c] != board[nr][nc]:
                    board[r][c], board[nr][nc] = board[nr][nc], board[r][c]
                    ans = max(ans, check_row(n, board, r, c),
                              check_col(n, board, r, c))
                    board[r][c], board[nr][nc] = board[nr][nc], board[r][c]
    return ans


def check_row(n, board, r, c):
    color = board[r][c]
    res = 1
    nr = r - 1
    # 위쪽 탐색
    while nr >= 0 and board[nr][c] == color:
        nr -= 1
        res += 1
    nr = r + 1
    # 아래쪽 탐색
    while nr < n and board[nr][c] == color:
        nr += 1
        res += 1
    return res


def check_col(n, board, r, c):
    color = board[r][c]
    res = 1
    nc = c - 1
    # 왼쪽 탐색
    while nc >= 0 and board[r][nc] == color:
        nc -= 1
        res += 1
    nc = c + 1
    while nc < n and board[r][nc] == color:
        nc += 1
        res += 1
    return res


if __name__ == "__main__":
    n = int(read())
    board = [[c for c in read().strip("\n")] for _ in range(n)]
    print(solution(n, board))
