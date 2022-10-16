class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def helper(i, n):

            # If i becomes equal to N , it means we have safely placed all the N Queens in N Rows such that no one attacks one another
            if i == n:

                # string temp will store the current configuration of the chessBoard which we can later put inside our ans[][]
                temp = []

                for j in range(n):

                    # currRow will contain the configuration of the CurrentRow which we are traversing

                    currRow = ""

                    for k in range(n):

                        currRow += chessBoard[j][k]

                    # After traversing one row, we need to push it inside our temp vector

                    temp.append(currRow)

                # After temp is ready, we put it inside our ans and simply return back to explore other possible configurations
                ans.append(temp.copy())
                return

            for j in range(n):

                # We need to first check if we can place a Queen in (i , j) position by calling isSafe() function

                if ( col[j] == 0 ) and ( topLeft[i - j + n - 1] == 0 ) and ( topRight[i + j] == 0 ):

                    # If isSafe() returns true, then we defintely can place a Queen in (i , j) cell

                    chessBoard[i][j] = "Q"

                    col[j] = 1
                    topLeft[i - j + n -1] = 1
                    topRight[i + j] = 1

                    # We ask recursion to do rest of the task

                    helper(i+1, n)

                    # Before leaving, we need to backtrack & undo the change we have done

                    chessBoard[i][j] = "."

                    col[j] = 0
                    topLeft[i - j + n - 1] = 0
                    topRight[i + j] = 0


        # solveNQueens function scope

        ans = []

        # We create the chessBoard which has dimmensions N * N
        # Any cell inside chessBoard will have either '.' or 'Q' as a Character
        # If chessBoard[i][j] = '.' , indicates that the cell is vacant and we can place a Queen
        # If chessBoard[i][j] = 'Q' , indicates that the cell is occupied by a Queen

        chessBoard = [["." for i in range(n)] for j in range(n)]

        # col[] vector will help us determine if any Queen is already placed in that particular column or not in O(1) Time Complexity

        col = [0 for i in range(n)]

        # topLeft[] vector will help us to check in the Top Left / Upper Left Direction in O(1) Time Complexity
        # We use the formula (i - j + n - 1) for mapping any index in topLeft with it's corresponding (i , j) in our ChessBoard

        topLeft = [0 for i in range(2*n)]

        # topRight[] vector will help us to check in the Top Right / Upper Right Direction in O(1) Time Complexity
        # We use the formula (i + j) for mapping any index in topRight with it's corresponding (i , j) in our ChessBoard

        topRight = [0 for i in range(2*n)]

        helper(0, n)

        return ans

"""
Time Complexity:  O(N!)
Space Complexity: O(N) {For Recursive Stack and For the 3 arrays col[] , topLeft[] , topRight[] we are using in place of isSafe() function } & O(N^2) {For our ans}
"""