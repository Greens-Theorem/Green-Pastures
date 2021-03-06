 /**
 * Side project of game Tic-Tac-Toe
 * @author C.M.H
 * @author E.T.C.
 * @version 1.0 4/5/2020
 */
package game;

public class TTT {

	public char[][] board;
	public char currentPlayer;

	// Create the board

	public TTT() {

		board = new char[3][3];

		currentPlayer = 'x';

		initializeBoard();

	}

	// New board
	public void initializeBoard() {

		for (int i = 0; i < 3; i++) {

			for (int j = 0; j < 3; j++) {

				board[i][j] = '*';

			}

		}

	}

	// Display the board
	public void printBoard() {

		System.out.println("-------------");

		for (int i = 0; i < 3; i++) {

			System.out.print("| ");

			for (int j = 0; j < 3; j++) {

				System.out.print(board[i][j] + " | ");

			}

			System.out.println();

			System.out.println("-------------");
		}
	}

	// Check if row is a winner
	private boolean rowWinner() {
		for (int i = 0; i < 3; i++) {
			if (board[i][0] == currentPlayer && board[i][1] == currentPlayer && board[i][2] == currentPlayer) {
				return true;
			}
		}
		return false;

	}

	// Check if column is a winner
	private boolean columnWinner() {
		for (int i = 0; i < 3; i++) {
			if (board[0][i] == currentPlayer && board[1][i] == currentPlayer && board[2][i] == currentPlayer) {
				return true;
			}
		}
		return false;

	}

	// Check if diagonal (both ways) are winner
	private boolean diagonalWinner() {
		if (board[0][0] == currentPlayer && board[1][1] == currentPlayer && board[2][2] == currentPlayer) {
			return true;
		}
		if (board[0][2] == currentPlayer && board[1][1] == currentPlayer && board[2][0] == currentPlayer) {
			return true;
		}
		return false;

	}

	// End game if winner
	public boolean determineWinner() {
		return (rowWinner() || columnWinner() || diagonalWinner());
	}

	// Determine if a draw
	public boolean boardDraw() {
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				if (board[i][j] == '*') {
					return false;
				}

			}
		}
		System.out.println("We have a draw!");
		return true;
	}

	// Change between 'X' and 'O'
	public void changeUser() {
		if (currentPlayer == 'x') {
			currentPlayer = 'o';
		} else {
			currentPlayer = 'x';
		}
	}

	// Player move
	public void playerMove(int row, int col) {
		boolean validSpot = true;
		while (validSpot) {
			if (row < 0 || row > 3 || col < 0 || col > 3) {
				validSpot = false;
			}
			row = row - 1;
			col = col - 1;
			if (row >= 0 && row <= 2) {
				if (col >= 0 && col <= 2) {
					if (board[row][col] == '*') {
						board[row][col] = currentPlayer;
						changeUser();
						break;
					} else {
						System.out.println("Invalid choice, try again");
						validSpot = false;
					}
				}
			} else {
				System.out.println("Enter a valid row/column between 1 and 3 and not chosen");
			}
		}
	}
}
