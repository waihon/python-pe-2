def valid_sudoku(sudoku: list) -> bool:
    # In Sudoku, The player has to fill the board in a very specific way:
    # - each row of the board must contain all digits from 1 to 9 (the order
    #   doesn't matter)
    # - each column of the board must contain all digits from 1 to 9 (again,
    #   the order doesn't matter)
    # - each of the nine 3x3 "tiles" (we will name them "sub-squares") of the
    #   table must contain all digits from 1 to 9.
    SORTED_DIGITS = "123456789"
    for row in sudoku:
        if not row.isdigit():
            return False
    
    sudoku_list = [ list(row) for row in sudoku ]

    # Each row of the board must contain all digits from 0 to 9
    for row in sudoku:
        sorted_row = "".join(sorted(row))
        if sorted_row != SORTED_DIGITS:
            return False
    
    # Each column of the board must contain all digits from 1 to 9
    for col_index in range(9):
        col = []
        for row_index in range(9):
            col.append(sudoku[row_index][col_index])
        sorted_col = "".join(sorted(col))
        if sorted_col != SORTED_DIGITS:
            return False
    
    # Each of the nine 3x3 "tiles" (we will name them "sub-squares") of the
    # table must contain all digits from 1 to 9.
    offsets: list = [0, 3, 6]
    for row_offset in offsets:
        for col_offset in offsets:
            sub_square = []            
            for row in range(3):
                for col in range(3):
                    sub_square.append(sudoku[row+row_offset][col+col_offset])
        sorted_sub_square = "".join(sorted(sub_square))
        if sorted_sub_square != SORTED_DIGITS:
            return False
    
    return True

if __name__ == "__main__":
    sudoku = [
        "295743861",
        "431865927",
        "876192543",
        "387459216",
        "612387495",
        "549216738",
        "763524189",
        "928671354",
        "154938672"
    ]
    result = "Yes" if valid_sudoku(sudoku) else "No"
    print(result)

    sudoku = [
        "195743862",
        "431865927",
        "876192543",
        "387459216",
        "612387495",
        "549216738",
        "763524189",
        "928671354",
        "254938671"
    ]
    result = "Yes" if valid_sudoku(sudoku) else "No"
    print(result)
