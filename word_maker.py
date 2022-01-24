def word_maker(board, list_):
    make_words = []
    
    for item in list_:
        board_look_up(board, item)
        
    
    for item in board:
        print(item) 




    
    
def board_look_up(board, word):
    start_points = []
    for row_id, row in enumerate(board):
        for col_id, col in enumerate(row):
            if board[row_id][col_id] == word[0]:
                start_points.append( (row_id, col_id) )
    
                
    for point in start_points:
        if check_letters(board, point, word): 
            return True 

    return False
              
            
    print(start_points)
    
def check_letters(board, point, word):

    res = ''
    res += word[0] 

    """ 
    for letter in word[1:]:
        # check right,
        i.e. if right from word == letter:
                res += lett 
        # check diagonal etc ..

    if res equals the word , return True!

    """
    
    r_point,c_pont = start_points
    
​
    # upper left
    if i == 0 and j == 0:
        return False 
​
    # bottom right 
    if i == (N - 1) and j == (N - 1):
        return False	
​
    # bottom left  
    if i == (N - 1) and j == 0:
        return False
    	
    # upper right
    if i == 0 and j == (N - 1):
        return False	
    return True         
    #     for id,col in enumerate(row):
    #         #if all(elm in row for elm in look):
    #         if all(elm in look for elm in row):
    #             temp=row.pop(id)
    #             make_words.append(temp)
    #             print(make_words)
    #             return True
    #         else:
    #             return False
                     
if __name__ == "__main__":
    board = [['C','A','P'],['A','N','D'],['T','I','E']]
    list_ = ["CAT"]
    r,c = 3,3 
    print(word_maker(board, list_))
    
 