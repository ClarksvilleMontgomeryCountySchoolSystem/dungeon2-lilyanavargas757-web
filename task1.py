good = r"""
                           ____         ___
                         ,' __ ``.._..''   `.
                         `.`. ``-.___..-.    :
 ,---..____________________>/          _,'_  |
 `-:._,:_|_|_|_|_|_|_|_|_|_|_|.:SSt:.:|-|(/  |
                        _.' )   ____  '-'    ;
                       (    `-''  __``-'    /
                        ``-....-''  ``-..-''
"""
bad = r"""
  _________
  |o^o^o^o^o|
  {   _!_   }
   \   !   /
    `.   .'
      )=(
     ( + )
      ) (
  .--'   `--.
  `---------'
"""

torch_lit = True
if torch_lit:
    outcome = "Flicker: The torch is lit!"
    print(good) 
else:
    outcome = "Doom: uh oh! You're doomed."
    print(bad)

print(outcome)