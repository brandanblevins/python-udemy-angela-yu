print("Welcome to Treasure Island! Your mission is to find the treasure.")

left_or_right = str(input("Do you want to take the left path or the right path? Type left or right: "))

if left_or_right == "left":
    swim_or_wait = str(input("Good choice! Now, do you want to swim across the lake or wait here? Type swim or wait: "))
else:
    print("You fell into a hole! GAME OVER!")

if swim_or_wait == "wait":
    choose_door = str(input("Another good choice! Very wise. Now, which door do you want to take? Type red, blue, yellow: "))
else:
    print("You've been attacked by a giant killer trout! GAME OVER")

if choose_door == "red":
    print("You've been roasted by the flaming fire of doom! GAME OVER")
elif choose_door == "blue":
    print("You've been eaten by the beasts of the dark forest! GAME OVER" '''                                             ___.-----.______
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
elif choose_door == "yellow":
    print("You are the wisest player yet! Congratulations on successfully completing your noble quest!")
else:
    print("You don't understand the game! GAME OVER")
