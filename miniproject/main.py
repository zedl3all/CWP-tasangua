from checkmate import checkmate

def main():
    board = """\
...B.
..P..
.K.PR
.Q...\
"""
    checkmate(board.upper())

if __name__ == "__main__":
    main()
