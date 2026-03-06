good = r"""
         _
         _a/~~~\a_
        /  \___/  \
       @\__/@a@\__/a
      `a/  \@g@/  \@'
        \_   Y   _/'
         ~`=/@\='~
"""
bad = r"""
    ______________
       |':.___________|Z:.
       |  |   o       |  |
       |  |_e-|-e_____|__|
       |,'   / \      |,'
"""

has_key = True
if has_key:
    outcome = "Click: You opened the door!"
    print(good)
else:
    outcome = "Doom: uh oh! You're doomed."
    print(bad)

print(outcome)