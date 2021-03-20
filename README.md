# Weird Game of Tic-Tac-Toe

This is a game of tic-tac-toe. Except the main rules, there is some modifications:

1. There are 5 different sizes of X's and O's
2. You can put on the board each size only once
3. You can not move the X or O of different size after putting on certain place on the board
4. You can put X on top of O, or other way around as long as size of piece is larger than oponents piece size.
5. You can not put larger piece on top of your own piece.
6. Largest piece (size 5 ) can not be covered by any piece 
7. game is won in normal tic-tac-toe rules: 3 straight pieces (horizontal,vertical,diagonal)


This git repo has several agents that can play the game:

1. genericAgent - very naive random position/piece try
2. humanAgent - you will be asked to place a piece in the order of "<row> <col> <size>"
3. minMaxAgent - agent that uses min-max algorithm
4. dqnAgent - agent that is trained on PyTorch by deep Q-learning
