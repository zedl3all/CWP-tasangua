from checkmate import checkmate

def main():
    board = """\
.H..
....
K...
.P..\
"""
    checkmate(board.upper())

if __name__ == "__main__":
    main()
