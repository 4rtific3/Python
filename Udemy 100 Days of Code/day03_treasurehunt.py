print('''
                            __          .gp.__/                            
                       .ssSSSSSs.__    d$P^^^"                             
                    .sSSSSSSS$$$$$$$p.dP                                   
                  .SSSSSS$$$$$SSSSSSSS$bs+._                               
                .SSSS$$$$$SSSSS$$$$$$$SS$$$$b__                       /"-. 
                SSS$$$SSSSS$$$$$$$$SSSS$$$SSSS$b                   _/"-. / 
               :S$$$SSSSS$$$$$$$SSSSS$$$SSSS$$SSb                 //   /"-.
               $$SSSSS$$$$$$SSSSS$$$$$$S$$$$S$$$Sb.               ;   /   /
               SSSSS$$$$$SSSSS$$$$$$$SS'P   SS$$S`^b._.'         /:  :   / 
               :S$$$$$SSSSS$$$$$$$SSSP      :$SS$b              / ;  +-./  
                $$$$SSSS$$$$$$$SSSSSP        S$SS$;            / /  / / ;  
               d$$SSS$$$$$SSSSSSSSS' ,=._    :S':S$           / /  / / /   
              :$SSS$$$$SSSSSSSSS^"  '  _ ";  ;   S$          / /  / / /    
              SSS$$$SSSP.-TSS^"     .="$;   /    S;         / /  / / /     
             :SS$$$SSS$$ (;            "    \    P         / /  / : :      
             :S$$$SS$$$$b :                  \ .'         / /  /  :  \     
              T$$SS$$$$$j`-,    .          ,  \         /"-(  /   ;_-.\    
               `TSS$$$$P   ;    `.         `.-'        /  /\\/   .'/_ ;;   
                 TS$$$P    :             _.-;         /  /\\(   / /-" ;;   
                  SSS'      \           :-t"         : .-\\/ "-/":   //    
                .SS$$        `.          `-;  bug    )Y   y   /  ;  J/     
               :S$$$;          "-.        (          '"; j_.-/-./.-" \_    
               $S$SS              "j.     :            :/  ':    `-..' \   
              d$$SS;     :        /  "-._.'             `.  ;       `-./;  
            _S$$$SP       \      :                        \: :"-.      \;  
          ,$$$SSSj       , `.    ;                         : ;   "-,   /   
          S$$SS'"^-...___       : "-.                      ;/      ;  t    
      __.-`SS'---. `T$$$$$$q._       "-.                  / `.    /   ;    
  .-""__ `.'      `. `T$$$$$$$$b.       `.               :    "--"   /     
 /.-""  \/          `. T$$$$$$$$$$p.     .`._            /"-.  _   .'      
::      /             \ T$$$$$SS$$$$$b._  `.T$p.        /    "" ;-'        
;;     :               \ T$$$S$$$$$$$$$$$p._L$$$$p.    /       ,           
;;     ;                \ $$$$$$$$$$$$$$$$$$$SS$$$$$. /                    
::     ;                 ;:$$$$$$$$$$$$$$SSSSSSSSS$$$y        '            
 ;;    :                  "^$$$$$$$$$$$$$$$$$SSSS$$$P        /             
 ;;     b.                   "^$$$$$$$$$$$$$$$$$S$$'        /              
 ::     :$$p.  -._              "^$$$$$$$$$$$$$$$'         /               
  ;;     $$$$$p.                   "^$$$$$$$$$$P          /                
  ::     :$$$$$$p.                    "^$$$$$$P          ,                 
   ;;     T$$$$$$$$p.                    "^$$P                             
   ::      T$$$$$$$P "-.                    "           '                  
   s;;      $$$$$$P   d$$p._                     /     /                   
  S$$:      $$$$$t   d$$$$$$$p._          "-.  .'     /                    
  SS$;;     :P^"\ \.d$$$$$$$$$$$$p._         ""      /                     
   TS::      \   d$$$$$$$$$$$$$$$$$$$p._            /                      
    SS.\     .jq$$$$$$$$$$$$$$$$$$^^^^^""-._      .';                      
   $$$$.tsssj' `T$$$$$$$^^^^^"""            "-._.'  ;                      
   $$$SSS         \                 /            \ :                       
   '^SSS_          \               :          :    :                       
     $$$SS.         \              ;          :    ;                       
     '$$$SS          \            :           ;   :                        
       "^S$.          \           ;          :    :                        
         S$$b.         \                     ;    ;                        
         S$$$$          ;                   :    :                         
         'TSS$$$s.      :                   ;    ;                         
             TS$$Ss_    ;                   ;   :                          
              `SSS$$$p./                   :    ;                          
                  TS$$'            ;       ;    :                          
                   "S              :       ;     ;                         
                   /                ;      :     :                         
                  /                 :            :                         
                 /"-.                          .' ;                        
                /    ""--..__          __..--""   :                        
                             """"""""""
''')

print('You are esteemed treasure hunter Lara Croft, and your mission is to find the treasure before the baddies do.\nYour journey brings you to the infamous bermuda triangle, and you are flying in by helicopter when you are surrounded by a storm and your radar and systems start malfunctioning.\nType your responses within the "" to choose your path')
option1 = input('You can either "turn" around or "press" onward.\n').lower()

if option1 == "press":
    print('You barely make it past the storm alive and crash land on a beach.\nAs you try to get your bearings, you see a flowing river leading "north" and a tower far in the distance to the "east".')
    option2 = input("Which way do you go?\n").lower()
    if option2 == "north":
        print('You follow the river and it leads you to a cave. There seems to be a light coming from inside the cave, but a bear is sleeping by the entrance.')
        option3 = input('Do you try to "sneak" past or "ambush" the bear?\n').lower()
        if option3 == "sneak":
            print("You manage to sneak past the bear and enter the cave.\nAs you approach the light, you realise that it is a shining golden monkey idol standing on a pedestal.")
            option4 = input('You can choose to "take" the idol or "explore" the cave more.\n').lower()
            if option4 == "take":
                print("As you take the idol, a white smoke fills the room and you feel yourself falling unconscious...\nYou wake up and find yourself in your bed in the Croft Manor, and you think it was all just a dream.\nBut out of the corner of your eye you see a golden monkey idol staring at you from your bedside table, which you are sure you've never seen before...")
            else:
                print("As you explore the cave you unknowingly step onto a pressure plate trap which fills the room with a transparent and odourless poison gas. You lose.")
        else:
            print("Even though you are Lara Croft, you cannot best a bear bare handed (see what I did there haha). The bear has you for dinner. You lose.")
    else:
        print("You run into a group of bad guys who are not particularly fond of visitors. You are taken hostage. You lose.")
else:
    print("You get lost in the storm and crash into the cold ocean. You lose.")