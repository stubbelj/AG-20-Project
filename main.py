#main file!

# import whatever modules we need
# 
# loading screen
#     print an ASCII graphics picture
#     "Welcome, chess players."
#     "Do you wish to [p]lay, or [q]uit?"
#     if neither p or q is entered:
#         "Please type in p or q."
#     else if p:
#         "Good to see.  :)"
#         load player entry screen
#     else if q:
#         "Oh...bye then."
#         
# player entry screen
#     "Who is playing white?"
#     input the name
#     "And who's playing black?"
#     input that name
#     "All right.  Ready to play!"
#     load chessboard
#     
# chessboard
#     load 8x8 B&W checkered grid
#     place pieces on appropriate squares
#     begin gameplay loop
# 
# gameplay loop
#     start on white
#     
#     if king is in check:
#         restrict valid moves to whatever gets king out of check
#     else:
#         valid moves are what pieces can do, and what isn't obstructed
#         
#     have piece moved when clicked and dragged
#     
#     if move is invalid:
#         it doesn't happen
#     
#     if move is onto opponent's piece:
#         opponent's piece disappears
#         player's piece overtakes it
#
#     if opponent is checkmated:
#         "[color] wins! :D"
#         go to loading screen
#     elif checkmate is impossible:
#         "Stalemate...  :/"
#         go to loading screen
#     else:
#         end turn
#         switch players
    
