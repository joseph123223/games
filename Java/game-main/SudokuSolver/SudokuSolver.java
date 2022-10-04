public class SudokuSolver {

    private static final int GRID_SIZE = 9;
    public static void main(String[] args){
         
        int [][] board ={
            {0,0,5,2,0,0,0,0,0},
            {0,0,0,8,0,0,0,0,3},
            {0,7,0,0,3,5,0,9,0},
            {0,8,0,0,0,0,6,0,0},
            {0,0,6,0,5,9,0,0,1},
            {0,0,0,0,0,2,0,0,0},
            {0,0,8,0,1,6,0,0,9},
            {4,0,0,0,0,0,0,7,0},
            {0,0,0,3,0,0,0,0,0}
        };

        printBoard(board);

        if(SolveBoard(board)){
            System.out.println("Sudoku Solved !!!");
        }
        else{
            System.out.println("Unsolvable Sudoku...");
        }

        printBoard(board);
    }

    private static void printBoard(int[][] board) {
        for( int i=0 ; i < GRID_SIZE; i++){
            if(i%3==0&&i!=0){
                System.out.println("------------");
            }
            for( int j=0 ; j < GRID_SIZE; j++){
                if(j%3==0&&j!=0){
                    System.out.print("|");
                }
                System.out.print(board[i][j]);
            }
            System.out.println();
        }
    }

    private static boolean isNumberInRow(int [][] board, int number, int row){
        for(int i =0; i< GRID_SIZE ; i++){
            if(board[row][i]==number){
                return true;
            }
        }
        return false;
    }

    private static boolean isNumberInCol(int [][] board, int number, int col){
        for(int i =0; i< GRID_SIZE ; i++){
            if(board[i][col]==number){
                return true;
            }
        }
        return false;
    }

    private static boolean isNumberInBox(int [][] board, int number, int row , int col){
        int localBoxRow = row - (row % 3); 
        int localBoxCol = col - (col % 3); 

        for(int i =localBoxRow; i< localBoxRow+3 ; i++){
            for(int j =localBoxCol; j< localBoxCol+3 ; j++){
                if(board[i][j]==number){
                    return true;
                }
            }
        }
        return false;
    }

    private static boolean isValidPlace(int [][] board, int number, int row , int col){
        return !isNumberInRow(board,number,row) && !isNumberInCol(board,number,col) && !isNumberInBox(board,number,row,col);
    }

    private static boolean SolveBoard(int [][] board){
        for(int row = 0; row < GRID_SIZE; row++){
            for(int col = 0; col < GRID_SIZE; col++){
                if(board[row][col]==0){
                    for(int TryNumber = 1; TryNumber <= GRID_SIZE; TryNumber++){
                        if(isValidPlace(board, TryNumber, row, col)){
                            board[row][col]= TryNumber;

                            if(SolveBoard(board)){
                                return true;
                            }
                            else{
                                board[row][col]=0;
                            }
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }
}