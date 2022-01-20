"""
parameter: type is a type hint indicating what type the parameter will be.
function()-> type is a type hint indicating what return value the function will have
"""

class ChessPiece:
    #remember that this is a member function, so there is only one board shared by all ChessPiece objects.
    board = [[], [], [], [], [], [], [], []]
    
    def __init__(self, color: string, type: string, position: tuple)-> ChessPiece:
      pass
    
    def move(self, destination: tuple)-> bool:
      """ Validates and then executes a move
      
      move() should first check if a move is legal. If it is an illegal move (trying to move to a position
      that piece cannot reach, trying to move to a position occupied by a piece of the same color) then
      move() will return false. If the move is legal, move() will return true, and move the piece the
      function was called on and remove a piece if one was taken. This way, moves can be easily validated
      in the main function with an if statement like if(piece.move())
      """
      pass
    
    
