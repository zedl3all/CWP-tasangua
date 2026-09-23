from checkmate import checkmate

def main():
    board = """\
....K
.....
.....
.Q...
.....\
"""
    checkmate(board.upper())

if __name__ == "__main__":
    main()
