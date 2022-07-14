# - int n: the number of rows and columns in the board
# - nt k: the number of obstacles on the board
# - int r_q: the row number of the queen's position
# - int c_q: the column number of the queen's position
# - int obstacles[k][2]: each element is an array of  integers, the row and column of an obstacle

def queensAttack(n, k, r_q, c_q, obstacles):
    
    ## Get max distances in all directions relative to the queen's position
    up = n - r_q 
    down = r_q -1
    left = c_q -1
    right = n - c_q
    
    diagonal_left_up = min(left, up)
    diagonal_right_up = min(right, up)
    diagonal_left_down = min(left, down)
    diagonal_right_down = min(right, down)
    
    ## Scan through all obstacles in the obstacles array relative to the queen's position    
    for obstacle in obstacles:
        
        o_r = obstacle[0] ## Obstacle row 
        o_c = obstacle[1] ## Obstacle column
        
        ## Check to see if obstacle column matches queen's column
        if o_c == c_q:
            ## if obstacle row is lesser than queen's row
            ## then it exists below the queen
            if o_r < r_q:
                down = min(down, r_q-1-o_r)
            ## Else, it exsits above the queen
            else:
                up = min (up, o_r-r_q-1)
        
        ## Check to see if obstacle row matches queen's row
        elif o_r == r_q:
            ## If obstacle column is lesser than queen's column
            ## then it exists on the left of the queen
            if o_c < c_q:
                left = min(left, c_q-1-o_c)
            ## Else, it exists to the right of the queen
            else:
                right = min(right, o_c-c_q-1)
        
        ## Check to see if obstacle exists diagonally to the queen
        elif abs(o_r-r_q) == abs(o_c-c_q):
            ## If obstacle column is more than queen's column
            if o_c > c_q:
                ## If obstacle row is more than queen's row
                ## Then it must exist diagonally rightwards up
                if o_r > r_q:
                    diagonal_right_up = min(diagonal_right_up, o_c-c_q-1)
                ## Else, it exists diagonally rightwards down
                else:
                    diagonal_right_down = min(diagonal_right_down, o_c-c_q-1)
            ## If obstacle column is lesser than queen's column
            else:
                ## If obstacle row is more than queen's row
                ## then it must exist diagonally leftwards up
                if o_r > r_q:
                    diagonal_left_up = min(diagonal_left_up, c_q-1-o_c)
                ## Else, it exists diagonally leftwards down
                else:
                    diagonal_left_down = min(diagonal_left_down, c_q-1-o_c)
                    
    ## Add all the distances together for all directions     
    return up + down + left + right + diagonal_left_down + diagonal_left_up + diagonal_right_down + diagonal_right_up