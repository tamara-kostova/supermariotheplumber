# You can place the script of your game in this file.

init:

    define r = Character("Journalist")
    define m = Character("Mario")
    define c = Character("Coworker")
    define l = Character("Luigi")
    image bg zgrada = ("zgradivodovod.png")
    image bg office = ("kancelarija.png")
    image mario1 = ("mario1.png")
    image mario2 = ("mario2.png")
    image mario3 = ("mario3.png")
    image luigi = ("luigi.png")
    image luigi1 = ("luigi1.png")
    image joshkata = ("joshi.png")
    image bg podium = ("mariopodium.png")
    image joshkata = ("joshkata.png")
    image mario1mal = ("mario1mal.png")
    image bg office1 = ("kancelarija2.png")
    image bg eternity = ("oneeternitylater.png")
    image bg bsod = ("bsod.jpg")


label start:
    scene bg zgrada
    
    play music "audio/supermario.wav"
    show mario1mal at left  
    voice "audio/1.wav"
    m "It's me Mario."
    voice "audio/2.wav"
    m "And I am the boss of Vodovod Bitola."
    voice "audio/3.wav"
    m "It's not worth saving the same princess forever, y'know."
    voice "audio/4.wav"
    m "She's not very..."
    voice "audio/5.wav"
    m "...grateful, let's put it that way."
    hide mario1mal



    scene bg office
    

    show mario1 at right
    with dissolve
    show joshkata at left
    voice "audio/01-6.wav"
    c "It's a crisis, boss! Someone..."
    voice "audio/02-6.wav"
    m "Not now, dammit."
    voice "audio/03-6.wav"
    m "I'm renewing my Fitness Paljo subscription."
    voice "audio/04-6.wav"
    c "I'm saying our systems..."
    voice "audio/05-6.wav"
    m "A man can't even self-care for a second without Vodovod meddling..."
    voice "audio/06-6.wav"
    c "THE MAP GOT STOLEN BECAUSE SOMEONE HACKED THE SYSTEM!"
    voice "audio/07-6.wav"
    m "What?! Not now...? The elections are round the corner..."
    voice "audio/08-6.wav"
    c "Yes. What are we going to do now? We should retrieve it."
    hide joshkata
    with fade
    with dissolve

    scene bg office

    show mario1 at left
    voice "audio/7.wav"
    m "I have a plan, but what should I do first?"


    menu:
        "What do I do first?"

        
        "Recover the map.":

            jump remap

        "Work as a plumber.":
            jump remap
    hide mario1
            
   



    
        


label remap:
        scene bg office
        show screen keyskip
        show mario1 at left
        with dissolve
        show luigi1 at right
        with fade
        voice "audio/8.wav"
        l "I am here to help repair the map."
        voice "audio/9.wav"
        l "I've quit running Luigi Burger because Vodovod needs me."
        window hide
        voice "audio/10.wav"
        l "I was able to recover all nine pieces of the map, but they're all scrambled."
        voice "audio/11.wav"
        l "All you need to do to repair the map is assemble the nine parts in the correct order."
        voice "audio/12.wav"
        l "Drag the piece you want in order to put it in the right place and click on it in order to rotate it."
        voice "audio/13.wav"
        m "I'd rather deal with Bowser again..."
        "(Press J after you solve the puzzle to continue)"
        jump puzzle
    
label puzzle:
    python:
        k = Puzzle()
        k.set_sensitive(False)
        k.show()


label continue:

    hide cow1
    hide mario1
    with dissolve

label quick_continue:
    
    while True:

        python:
        
            ui.textbutton("Give Up", ui.jumps("giveup"), xalign=.02, yalign=.98)
            k.set_sensitive(True)
            event = k.interact()
            if event:
                renpy.checkpoint()
            
            k.set_sensitive(False)
        # e "[event]"
        if event == "win":
            jump win


label up:

    voice "audio/14.wav"
    l "Nice, you've successfully repaired the map!"
    with dissolve
    

    jump kanc

stop music

label kanc:
    scene bg office1 
    show mario1mal at left
    with dissolve
    voice "audio/15.wav"
    m "Repaired the map,"
    play music "audio/Cane Nikolovski - Zaklina.wav"
    voice "audio/16.wav"
    m "now I can finally chill out with some Cane."
    
        
stop music


label oneeternity:
    scene bg eternity
    voice "audio/One Eternity LaterSpongeBob Time Card #9.mp3"
    "One eternity later..." 


label kradonacalnik:
    
    scene bg podium
    voice "audio/17.wav"
    r "Mario, now that you're Mayor. What's going to happen with Bitola?"
    voice "audio/18.wav"
    m "I will take care of this city and its people and I swear I'm not going to steal!"
    




#label giveup:

    #$ k.set_sensitive(False)
    
    #with dissolve

   # menu:
       # m "Are you sure you want to give up?"

       # "Yes":

           # "Oh well, better luck next time."
            
          #  jump newgame

     #   "No":

      #      jump continue

#label newgame:

   # menu:    
    #    m "Would you like to try again?"

  #      "Yes":
       #     pass

   #     "No":
    #        m "Well, I hope to see you again soon."
     #       return 

  #  m "Okay, here we go!"
    
  #  scene bg table

 #   python:
   #     k = Puzzle()
  #      k.sensitive = False
  #      k.show()

   # jump continue
 #   
