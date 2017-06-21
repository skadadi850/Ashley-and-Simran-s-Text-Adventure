from random import randint



start = '''
Welcome to Ashley and Simran's text adventure!
You are a little girl going on an adventure.
Hunger level: Medium
'''

forest = '''
A large, hairy hippogriff approaches you!
You are shocked and startled by its grandeur and don't know what to do.
Hunger level: High
'''

candy_house = '''
A glistening, agile phoenix perches on top of your shoulder.
You are in awe of its beauty and presence. You wonder what to do with it.
Do you kill it for food or befriend it?
Hunger level: High
'''

kill_hippogriff = '''
From eating so much protein, you feel rejuvenated and replenished.
You grow big and strong and escape the woods successfully.
Hunger level: Tummy Full
'''

befriend_hippogriff = '''
The hippogriff takes you on this windy route.
The wind is blowing and it is starting to get dark.
You see a faint outline of a rundown shack with cobwebs strewn across the windows.
You enter and the hippogriff flies away from you.
You here the door lock behind you. You hear a voice cackling behind you.
The wind whistles and a green wrinkly hand glides across the back of your neck.
Hunger level: STARVING
'''

befriend_phoenix = '''
The phoenix says, "I can be friends with a human, I guess..."
You look down and see ruby slippers on your feet and yellow bricks appearing in front of you.
As you follow the path, you walk over rocky mountains and winding, rapid rivers.
You heard the rhythmn of a heartbeat.
Bent upon an old tree sat a clunky Tin Man. He smiles a crooked smile and offers you a heart.
You take the heart and continue following the yellow brick road.
'''

meet_prince = '''
You meet a prince dying on his horse. A dagger covered in blood sticks out of his muscular chest.
Your phoenix friend whispers in your ear telling you to save the prince.
'''

kill_phoenix = '''
You try to burn the phoenix with fire, and it seems to work at first.
Just seconds later, the phoenix bursts into flames and re-emerges as a baby phoenix-- it has been reborn!
Unfortunately, you failed to kill the phoenix and instead it kills you. THE END :)
'''

bad_ending = '''
Karma gets you back! HA! You find youself in a boiling pot of chicken broth with toad legs and hickory chips.
The smell of blood perforates and you slowly lose consciousness. THE END
'''

good_ending = '''
You marry the prince and live happily every after in a castle of rainbows. THE END
'''

happy_hippogriff = '''
The hippogriff flies you out of the woods and lands outside a beautiful castle.
You see a handsome prince with flowing locks.
'''


random_number = 5
print (start)
done = False
while not done:
    input_var = input('Do you want to explore the forest or the candy house? ')    # Choose between forest and candy house
    if input_var == 'forest':
        print (forest)
        done = True
    elif input_var == 'candy house':
        print (candy_house)
        done = True
    else:
        print ('Pls input either "forest" or "candy house"')

if input_var == 'forest':
    done = False
    while not done:
        input_var = input('Do you kill the hippogriff for food or befriend the hippogriff? ')
        if input_var == 'kill':
            print (kill_hippogriff)
            print (good_ending)
            done = True
        elif input_var == 'befriend the hippogriff':
            random_number = randint(0,9);
            if random_number <= 5:
                print (happy_hippogriff)
                print (good_ending)
            else:
                print (befriend_hippogriff)
                print (bad_ending)
            done = True
        else:
            print ('Pls input either "kill" or "befriend the hippogriff"')

if input_var == 'candy house':
    done = False
    while not done:
        input_var = input('Do you kill the phoenix for food or befriend it? ')
        if input_var == 'kill':
            print (kill_phoenix)
            done = True
        elif input_var == 'befriend':
            print (befriend_phoenix)
            print (meet_prince)
            done = True
        else:
            print ('Pls input either "kill" or "befriend"')

if input_var == 'befriend':
    done = False
    while not done:
        input_var = input('Do you give him your heart? ')
        if input_var == 'yes':
            print (good_ending)
            done = True
        elif input_var == 'no':
            print (bad_ending)
            done = True
        else:
            print ('Pls input either "yes" or "no"')
