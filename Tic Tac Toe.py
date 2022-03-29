# Tic tac toe in python


import tkinter as tk
import tkinter.font as font


class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        master.title('Tic Tac Toe')
        master.geometry('600x400')
        self.master = master
        self.pack(anchor=tk.W)
        self.create_squares()

    def create_squares(self):
        labelFont = font.Font(size=30, weight='bold')
        for i in range(0, 3):
            for j in range(0, 3):
                tblTxt = i * 3 + j
                square = tk.Label(self, text=tblTxt, bg='white', bd=2,
                                  font=labelFont, relief='groove', width=5, height=2)
                square.grid(column=j, row=i)


root = tk.Tk()
Application(master=root)
root.mainloop()




import tkinter as tk
import tkinter.font as font


class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        master.title('Tic Tac Toe')
        master.geometry('600x400')
        self.master = master
        self.pack(anchor=tk.W)
        self.xIsNext = True
        self.create_squares()

    def create_squares(self):
        labelFont = font.Font(size=30, weight='bold')
        for i in range(0, 3):
            for j in range(0, 3):
                square = tk.Label(self, text='', bg='white', bd=2,
                                  font=labelFont, relief='groove', width=5, height=2)
                square.grid(column=j, row=i)
                square.bind("<1>", self.btnClick)

    def btnClick(self, event):
        label = event.widget
        if label['text'] == '':
            label['text'] = 'X' if self.xIsNext else 'O'
            self.xIsNext = False if self.xIsNext else True


root = tk.Tk()
Application(master=root)
root.mainloop()





import tkinter as tk
import tkinter.font as font


class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        master.title('Tic Tac Toe')
        master.geometry('600x400')
        self.master = master
        self.pack()

        self.lFrame = tk.Frame(self)
        self.lFrame.grid(column=0, row=0)
        self.rFrame = tk.Frame(self)
        self.rFrame.grid(column=1, row=0)

        self.squares = []
        self.stepNumber = 0
        self.history = [{'squares': [''] * 9, 'message':'Next turn ：X'}]

        
        self.message = tk.Label(self.rFrame, text='Next turn ：X')
        self.message.pack(anchor=tk.N)

        # starting button
        button = tk.Button(self.rFrame, text='Go to game start')
        button.bind('<1>', lambda e, args={'index': 0}: self.histBtnClick(e, args))
        button.pack()
        self.buttons = [button]

        # square windo
        self.create_squares()

        # winning line
        self.winnerLines = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ]

    def create_squares(self):
        labelFont = font.Font(size=30, weight='bold')
        for i in range(0, 3):
            for j in range(0, 3):
                square = tk.Label(self.lFrame, text='', bg='white', bd=2,
                                  font=labelFont, relief='groove', width=5, height=2)
                square.grid(column=j, row=i)
                square.bind("<1>", lambda e, args={'index': i * 3 + j}: self.sqClick(e, args))
                self.squares.append(square)

    def sqClick(self, event, args):

        
        current = self.history[self.stepNumber]

        label = event.widget

        if label['text'] == '' and not self.calculateWinner(current['squares']):
            label['text'] = 'X' if self.stepNumber % 2 == 0 else 'O'

            
            squares = current['squares'].copy()
            squares[args['index']] = label['text']

            
            message = 'next turn ：' + ('O' if self.stepNumber % 2 == 0 else 'X')
            if self.calculateWinner(squares):
                message = 'winner　:' + label['text']

            for i in range(len(self.history) - (self.stepNumber + 1)):
                self.history.pop()
                button = self.buttons.pop()
                button.destroy()

            self.stepNumber += 1
            self.message['text'] = message
            self.history.append({'squares': squares, 'message': f'{message}'})
            self.createButton(self.stepNumber)

    def createButton(self, index):
        button = tk.Button(self.rFrame, text=f'Go to move #{index}')
        button.bind('<1>', lambda e, args={'index': index}: self.histBtnClick(e, args))
        self.buttons.append(button)
        button.pack()

    def histBtnClick(self, event, args):
        self.stepNumber = args['index']

        history = self.history[self.stepNumber]
        self.message['text'] = history['message']

        # Write over the boxes
        for i, square in enumerate(history['squares']):
            self.squares[i]['text'] = square

    
    def calculateWinner(self, squares):
        for line in self.winnerLines:
            if squares[line[0]] != '' \
                    and squares[line[0]] == squares[line[1]] \
                    and squares[line[0]] == squares[line[2]]:
                return squares[line[0]]
        return None


root = tk.Tk()
Application(master=root)
root.mainloop()





# {
#     # IntelliSense を使用して利用可能な属性を学べます。
#     // 既存の属性の説明をホバーして表示します。
#     // 詳細情報は次を確認してください: https://go.microsoft.com/fwlink/?linkid=830387
#     "version": "0.2.0",
#     "configurations": [
#         {
#             "name": "Python: Current File",
#             "type": "python",
#             "request": "launch",
#             "program": "${file}",
#             "console": "integratedTerminal"
#         }
#     ]
# }