define e = Character("Eileen")
define p = Character("Player")

label start:

    # Using the hallway background
    scene bg hallway
    play music "audio/BgMusic.mp3" fadein 1.0 volume 0.5

    # Showing character sprites
    show c2 happy at right
    show c1 default at left

    # choice variables for learnable things
    default path1 = False

    e "Hi! How is it going?"

    menu:
        "It's going great!":
            jump response_happy

        "I'm a bit tired.":
            jump response_tired

label response_happy:
    e "That's wonderful to hear!"
    $ path1 = True
    jump response2

label response_tired:
    # Switching c2 to the default sprite
    show c2 default 
    e "'Tis tuff twin."
    jump response2

label response2:
    p "Bye"
    jump end_game

label end_game:
    if path1:
        e "Bye bye!!"
    else:
        e "Bye...."

    return