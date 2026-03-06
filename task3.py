good = r"""
  .     .
            (>\---/<)
            ,'     `.
           /  q   p  \
          (  >(_Y_)<  )
           >-' `-' `-<-.
          /  _.== ,=.,- \
         /,    )`  '(    )
        ; `._.'      `--<
       :     \        |  )
       \      )       ;_/  hjw
        `._ _/_  ___.'-\\\
           `--\\\
"""
bad = r"""
  o_           
         .-"  ".          
 bmw   ."    _-'-""--o        
      J    ,"" _      ".
   .-",___,)____)___),-'
"""

guard_awake = False
if not guard_awake:
    outcome = "Shadow: Yes! You made it past the guard."
    print(good)
else:
    outcome = "Doom: uh oh! You're doomed."
    print(bad)

print(outcome)