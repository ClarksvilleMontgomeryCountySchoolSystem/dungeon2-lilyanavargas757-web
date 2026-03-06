good = r"""
 ,--.
  \  _\_
  _\/_|_\____.'\
-(___.--._____(
     \   \
      \   \
       `--'
"""
bad = r"""
    __      _.._
       .-'__`-._.'.--.'.__.,
      /--'  '-._.'    '-._./
     /__.--._.--._.'``-.__/
     '._.-'-._.-._.-''-..'
"""

drawbridge_raised = False
if not drawbridge_raised:
    outcome = "Thunder: Yes! The drawbridge is down."
    print(good)
else:
    outcome = "Doom: uh oh! You're doomed."
    print(bad)

print(outcome)