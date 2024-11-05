print("Welcome to Treasure Island! Your mission is to find the treasure.")

choice1 = input('Do you want to take the left path or the right path? Type "left" or "right": ').lower()

if choice1 == "left":
    # Continue in the game.
    choice2 = input('Good choice! Now, do you want to swim across the lake or wait here? Type "swim" or "wait": ').lower()
    if choice2 == "wait":
        choice3 = input("Another good choice! Very wise. Now, which door do you want to take? Type red, blue, yellow: ").lower()
        if choice3 == "red":
            print("You've been roasted by the flaming fire of doom! GAME OVER" '''
                   (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' ) ''')
        elif choice3 == "blue":
            print("You've been eaten by the beasts of the dark forest! GAME OVER" '''
                                            ___.-----.______
                                   ___.-----'::::::::::::::::`---.___
                _.--._            (:::;,-----'~~~~~`----::::::::::.. `-.
   _          .'_---. `--.__       `~~'                 `~`--.:::::`..  `..
  ; `-.____.-' ' {0} ` `--._`---.____                         `:::::::: : ::
 :_^              ~   `--.___ `----.__`----.____                ~::::::.`;':
  :`--.__,-----.___(         `---.___ `---.___  `----.___         ~|;:,' : |
   `-.___,---.____     _,        ._  `----.____ `----.__ `-----.___;--'  ; :
                  `---' `.  `._    `))  ,  , , `----.____.----.____   --' :|
                        / `,--.\    `.` `  ` ` ,   ,  ,     _.--   `-----'|'
 _.~~~~~~._____    __./'_/'     :   .:----.___ ` ` ` ``  .-'      , ,  :::'
                 ///--\;  ____  :   :'    ____`---.___.--::     , ` ` ::'
                 `'           _.'   (    /______     (   `-._   `-._,-'
    ()  ()                 .-' __.-//     /_______---'       `-._   `.
  * *(o)'      ~~~        /////    `'       ~~~~~~      ~~ ______;   ::.
  `\ )( /*                `'`'                            /_______   _.'
    {()}      ,     ~~~                  ~~~~~~~~           /___.---'  --__
     !|       `                                              ~~~
  ~~~~~~~~
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ''')
        elif choice3 == "yellow":
            print("You are the wisest player yet! Congratulations on successfully completing your noble quest!" '''
                  *
             / \
            /___\
           ( o o )            * *
           )  L  (           /   * *
   ________()(-)()________  /     * * *
 E\| _____ )()()() ______ |/B     * * *
   |/      ()()()(       \|      * * * *
           | )() |
           /     \
          / *  *  \
         /   *  *  \
        / *_  *  _  \   ''')
        else:
            print("You don't understand the game! GAME OVER" '''
         _______________,,.
    /_____________.;;'/|
   |"____  _______;;;]/
   | || //'         ;
   | ||//'          ;
   | |//'           ;
   |  /'            $
   | ||             $
   | ||             $
   | ||            ,^.
   | ||            | |
   | ||            `.'
   | || 
   | || 
   | || 
   | || 
   | ||   _________________________   
   | ||  /                        4
   | || /                        /| 
   | ||/           _____        / /
   | ||           /|___/       / /|
   | ||          / |  /       / /||
   |_|/         / cj /       / / ||
  /             """""       / /| ||
 /                         / / | ||
/                         / /  | ||
""""""""""""""""""""""""""|/   | ||
__________________________f|   | |
| ||                    | ||           
| ||                    | ||    
| ||                    | ||
| ||                    | ||
| ||                    | ||
| |                     | | ''')
    else:
        print("You've been attacked by a giant killer trout! GAME OVER")
else:
    print("You fell into a hole! GAME OVER!")
