from checkmate import checkmate

def main():
    board = """\
.K...
.....
.....
.....
.....\
"""
    checkmate(board.upper())

if __name__ == "__main__":
    main()
