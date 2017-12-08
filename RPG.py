#  File: RPG.py
#  Description: Program simulates an RPG game. Players can equip themselves and attack others. 
#  Each time a player does an action, the output is what the action was and whether or not the players were affected
#  The first person to die, loses
#  Student's Name: Brian Tsai
#  Student's UT EID: byt76
#  Course Name: CS 313E
#  Unique Number: 51465
#
#  Date Created: 9/17/17
#  Date Last Modified: 9/21/17


class Weapon:

    # Weapons can access how much damage they can do
    weaponDict = {"dagger": 4, "axe": 6, "staff": 6, "sword": 10, "none": 1}

    # Initialize a weapon
    def __init__(self, weaponType):
        self.weaponType = weaponType

    # Return this type of weapon used
    def getWeapon(self):
        return self.weaponType

    # Return the amount of damage done by this weapon
    def getWeaponDamage(self):
        return self.weaponDict[self.weaponType]

    # Return this type of weapon used
    def __str__(self):
        return self.weaponType

class Armor:

    # Armors can access what their class level is
    armorDict = {"plate": 2, "chain": 5, "leather": 8, "none": 10}

    # Initialize a piece of armor
    def __init__(self, armorType):
        self.armorType = armorType

    # Return this type of armor 
    def getArmor(self):
        return self.armorType

    # Return this armor's class
    def getArmorClass(self):
        return self.armorDict[self.armorType]

    # Return this type of weapon used
    def __str__(self):
        return self.armorType

class RPGCharacter:

    # Initialize any new character
    def __init__(self, name, maxHealth, maxSpell):
        self.name = name
        self.maxHealth = maxHealth
        self.maxSpell = maxSpell
        self.healthPoints = maxHealth
        self.spellPoints = maxSpell
        self.weapon = Weapon("none")
        self.armor = Armor("none")

    # Equip this character with the weapon and print what the character now wields
    def wield(self, weapon):
        self.weapon = weapon
        print(self.name, "is now wielding a(n)", self.weapon)
    
    # Unequip this character with the current weapon 
    def unwield(self):
        self.weapon = Weapon("none")
        print(self.name, "is no longer wielding anything")

    # Equip this character with the armor
    def putOnArmor(self, armor):
        self.armor = armor
        print(self.name, "is now wearing", self.armor)

    # Unequip this character with the current armor
    def takeOffArmor(self):
        self.armor = Armor("none")
        print(self.name, "is no longer wearing anything.")

    # Fight another character
    def fight(self, opponent):

        # Check if the character has a weapon
        if (self.weapon.getWeapon() != "none"):
            print(self.name, "attacks", opponent.name, "with a(n)", self.weapon)

        # Else, the character attacks with no weapon
        else:
            print(self.name, "attacks", opponent.name, "with a(n) bare hands")

        # Attack damage lowers the opponent's health points
        opponent.healthPoints -= self.weapon.getWeaponDamage()
        print(self.name, "does", self.weapon.getWeaponDamage(), "damage to", opponent.name)
        print(opponent.name, "is now down to", opponent.healthPoints, "health.")
        
        # Check whether the opponent was defeated
        RPGCharacter.checkForDefeat(opponent)

    # Check if a character was defeated    
    def checkForDefeat(character):

        # If the character's health points is less than equal to zero, then they are defeated
        if (character.healthPoints <= 0):
            print(character.name, "has been defeated!")

    # Output this character's status info
    def __str__(self):
        return "\n" + self.name + \
               "\n\tCurrent Health: " + str(self.healthPoints) + \
               "\n\tCurrent Spell Points: " + str(self.spellPoints) + \
               "\n\tWielding: " + str(self.weapon.getWeapon()) + \
               "\n\tWearing: "+ str(self.armor.getArmor()) + \
               "\n\tArmor Class: " + str(self.armor.getArmorClass()) + "\n"


class Fighter(RPGCharacter):

    # Initialize a fighter
    def __init__(self, fighterName):
        super().__init__(fighterName, 40, 0)

    # Equip the fighter with this weapon
    def wield(self, weapon):

        # Fighters can wield any weapon
        super().wield(weapon)



class Wizard(RPGCharacter):

    # The wizard has access to a dictionary of spells
    spellDict = {"Fireball": [3, 5], "Lightning Bolt": [10, 10], "Heal": [6, -6]}
    cost = 0
    effect = 1

    # Initialize a wizard
    def __init__(self, wizardName):
        super().__init__(wizardName, 16, 20)

    # Equip the wizard with this weapon
    def wield(self, weapon):
        
        # Only allow the wizard to be equipped with the dagger, staff, or none
        if (weapon.getWeapon() == "dagger" or weapon.getWeapon() == "staff" or weapon.getWeapon() == "none"):
            super().wield(weapon)
        
        # Else, the wizard cannot wield this weapon
        else:
            print("Weapon not allowed for this character class.")
    
    # Equip the wizard with this armor
    def putOnArmor(self):
        
        # The wizard cannot wear any armor
        print("Armor not allowed for this character class")

    # Cast a spell on the opponent
    def castSpell(self, spellName, opponent):

        print(self.name, "casts", spellName, "at", opponent.name)

        # If the wizard does not know this spell
        if (spellName not in self.spellDict):
            print("Unknown spell name. Spell failed")
            return

        # If the wizard does not have enough spell points
        elif (self.spellPoints < self.spellDict[spellName][self.cost]):
            print("Insufficient spell points")
            return

        # Else, the spell is valid
        else:
            # Subtract the damage from the opponent's health
            opponent.healthPoints -= self.spellDict[spellName][self.effect]

            # Subtract the cost of the spell from the wizard's spell points
            self.spellPoints -= self.spellDict[spellName][self.cost]

            # Check how much health the opponent receives
            if (spellName == "Heal"):

                # Make sure the opponent's health cannot go over their max health
                if (opponent.healthPoints > opponent.maxHealth):
                    opponent.healthPoints = opponent.maxHealth

                print(self.name, "heals", opponent.name, "for", abs(self.spellDict[spellName][self.effect]), "health points")
                print(opponent.name, "is now at", opponent.healthPoints, "health")

            # Else, damage the opponent
            else:
                print(self.name, "does", self.spellDict[spellName][self.effect] , "damage to", opponent.name)
                print(opponent.name, "is now down to", opponent.healthPoints, "health")
                RPGCharacter.checkForDefeat(opponent)

def main():

    # Test cases

    plateMail = Armor("plate")
    chainMail = Armor("chain")
    sword = Weapon("sword")
    staff = Weapon("staff")
    axe = Weapon("axe")

    gandalf = Wizard("Gandalf the Grey")
    gandalf.wield(staff)

    aragorn = Fighter("Aragorn")
    aragorn.putOnArmor(plateMail)
    aragorn.wield(axe)

    print(gandalf)
    print(aragorn)

    gandalf.castSpell("Fireball", aragorn)
    aragorn.fight(gandalf)

    print(gandalf)
    print(aragorn)

    gandalf.castSpell("Lightning Bolt", aragorn)
    aragorn.wield(sword)

    print(gandalf)
    print(aragorn)

    gandalf.castSpell("Heal", gandalf)
    aragorn.fight(gandalf)

    gandalf.fight(aragorn)
    aragorn.fight(gandalf)

    print(gandalf)
    print(aragorn)


main()