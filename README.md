# pokemon-stadium-randomizer
Randomizer for the N64 game Pokémon Stadium.

0.1.1
 - Base stats being randomized
 - Displayed stats when selecting rentals match their battle stats
 
0.1.2
 - EVs and IVs being randomized for Gym Tower Rentals
 - Moves are being randomized for Gym Tower Rentals
 - Individual base stat caps adjusted
	- Like the minimum values, the max values are tied to the max for each stat in the game
	- HP is the exception. Chansey has a HP BST of 250, so instead Snorlax's HP value is used. (The 2nd highest HP stat)

0.3
 - Gym Castle Pokémon are being randomized the same way rentals are

0.3.1
 - Reworked how base stats are randomized. Base stats are calculated using percentages now, percentage values are not set in stone.

0.3.2
 - Attacks are not fully random anymore.
 - Lower BST Pokémon have a better chance at better moves, higher BST means a lower chance
 - 2 slots are reserved for physical moves, 1 for special, and 1 for status.
 - Need to address a bug where duplicate moves can show up. (e.g. I genereated Moltres that knew Mega Punch twice)

0.3.3
 - changed how move slots are assigned
	- Slot 1: Matches higher base stat between ATK and SPC
	- Slot 2: Either a ATK or SPC move
	- Slot 3: A STA move
	- Slot 4: Any of the 3 categories
 - possible bug in how the BSTs are being written after being randomized, needs investigation to confirm existence and cause