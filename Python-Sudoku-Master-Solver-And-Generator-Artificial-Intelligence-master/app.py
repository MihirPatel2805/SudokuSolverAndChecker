import tkinter as tk
import test as t
import tkinter.messagebox       
import copy
import SudokuMaster as sm
class SudokuSolver:
    def __init__(self):
        self.root=tk.Tk()
        self.root.title("Sudoku Solver")
        self.root.geometry("550x400")
        self.root.minsize(550,400)
        self.root.maxsize(550,400)
        self.sudoku_grid = [[tk.StringVar() for _ in range(9)] for _ in range(9)]
        self.board=[[] for _ in range(9) ]
        self.create_widgets(t.puzzle)
        self.root.mainloop()
        

    def create_widgets(self,grid):
        for i in range(3):
            for j in range(3):
                # Creating a frame for each 3x3 box
                box_frame = tk.Frame(self.root, bg="lightblue", width=5, highlightbackground="black", borderwidth=5,highlightthickness=1)
                box_frame.grid(row=i, column=j, padx=1, pady=1)
                # Creating the Sudoku grid within each box frame
                for x in range(3):
                    row=[]
                    for y in range(3):
                        entry = tk.Entry(box_frame, textvariable=self.sudoku_grid[i*3+x][j*3+y], width=4, font=('Helvetica', 16))
                        entry.grid(row=x, column=y, padx=2, pady=2)
                        row.append(entry)
                    self.board[i*3+x].extend(row)
            for i in self.board:
                print(i)
            
        for i in range(9):
            for j in range(9):
                if grid[i][j]==0:
                    pass
                else:
                    self.sudoku_grid[i][j].set(str(grid[i][j]))
        solve_button = tk.Button(self.root, text="Solve", command=self.solve)
        solve_button.grid(row=9, columnspan=9)
        solve_reset = tk.Button(self.root, text="reset", command=self.reset)
        solve_reset.grid(row=10, columnspan=9)
        solve_reset = tk.Button(self.root, text="submit", command=self.check)
        solve_reset.grid(row=11, columnspan=10)
    
    def check(self):
        grid = [[0 for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                value = self.sudoku_grid[i][j].get()
                if value.isdigit():
                    grid[i][j] = int(value)
                else:
                    grid[i][j] = 0
        puzzel=copy.deepcopy(t.puzzle)
        istrue=True
        if sm.solveBoard(puzzel):
            for i in range(9):
                for j in range(9):
                    if grid[i][j]!=puzzel[i][j]:
                        istrue=False
                        self.board[i][j].config(bg='red')
                    else:
                        self.board[i][j].config(bg='white')
        if istrue:
            tkinter.messagebox.askyesno("game Over ","you win")
    def reset(self):
        
        for i in range(9):
            for j in range(9):
                self.sudoku_grid[i][j].set('')
                self.board[i][j].config(bg='white')
        grid1=copy.deepcopy(t.puzzle)
        print(grid1)     
        for i in range(9):
                for j in range(9):
                    if grid1[i][j]==0:
                        pass
                    else:
                        self.sudoku_grid[i][j].set(str(grid1[i][j]))        
                
    def solve(self):
        grid = [[0 for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                value = self.sudoku_grid[i][j].get()
                if value.isdigit():
                    grid[i][j] = int(value)
                else:
                    grid[i][j] = 0
        if sm.solveBoard(grid):
            print("\n\n\nSolved Solution is: ")
            sm.printBoard(grid)
            for i in range(9):
                for j in range(9):
                    if grid[i][j]==0:
                        pass
                    else:
                        self.sudoku_grid[i][j].set(str(grid[i][j]))
        else:
            print("No Solution Exist")  
                    
     
        
    
if __name__ == "__main__":
    app = SudokuSolver()
    
