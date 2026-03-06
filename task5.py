good = r"""
   \/
 _\_\/\/_/_
  _\_\/_/_
 __/_/\_\__
  / /\/\ \
     /\
"""
bad = r"""
 __/\__
 \_\/_/
 /_/\_\
   \/
"""

escaped = True
if escaped:
    outcome = "Legend: You escaped! You're a true legend."
    print(good)
else:
    outcome = "Doom: uh oh! You're doomed."
    print(bad)

print(outcome)