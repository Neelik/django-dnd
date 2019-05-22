#!/usr/bin/env bash

case "$1" in
	character)
		# GET REQUESTS
		echo
		echo '----------------------------------'
		echo 'GET for all Characters'
		echo && curl -X GET localhost:8000/api/characters && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by name, successful'
		echo && curl -X GET localhost:8000/api/characters?name=Character && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Query by name that does not exist'
		echo && curl -X GET localhost:8000/api/characters?name=None && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by player, successful'
		echo && curl -X GET localhost:8000/api/characters?player=Player && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Query by player that does not exist'
		echo && curl -X GET localhost:8000/api/characters?player=Me && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by class, successful'
		echo && curl -X GET localhost:8000/api/characters?class=Paladin && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Query by class that does not exist'
		echo && curl -X GET localhost:8000/api/characters?class=Priest && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by race, successful'
		echo && curl -X GET localhost:8000/api/characters?race=Dwarf && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Query by race that does not exist'
		echo && curl -X GET localhost:8000/api/characters?race=Elf && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by level_above, successful'
		echo && curl -X GET localhost:8000/api/characters?level_above=9 && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Query by level_above that does not exist'
		echo && curl -X GET localhost:8000/api/characters?level_above=11 && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by level_below, successful'
		echo && curl -X GET localhost:8000/api/characters?level_below=11 && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Query by level_below that does not exist'
		echo && curl -X GET localhost:8000/api/characters?level_below=9 && echo
		sleep 1
		echo
		echo '----------------------------------'

		# PUT REQUESTS

		echo 'Updating "level" field of Character'
		echo && curl -X PUT -H "Content-Type: application/json" -d '{"level": 11, "alignment": "Chaotic Good", "race": "Dwarf", "name": "Character 1", "player_name": "Player 1", "character_class": "Paladin"}' localhost:8000/api/characters/put-delete/1/ && echo
		sleep 1
		echo
		echo '----------------------------------'

		echo 'Updating "alignment" field of Character'
		echo && curl -X PUT -H "Content-Type: application/json" -d '{"level": 11, "alignment": "Chaotic Evil", "race": "Dwarf", "name": "Character 1", "player_name": "Player 1", "character_class": "Paladin"}' localhost:8000/api/characters/put-delete/1/ && echo
		sleep 1
		echo
		echo '----------------------------------'

		echo 'Updating "race" and "name" field of Character'
		echo && curl -X PUT -H "Content-Type: application/json" -d '{"level": 11, "alignment": "Chaotic Evil", "race": "Half Elf", "name": "Beezelbub", "player_name": "Player 1", "character_class": "Paladin"}' localhost:8000/api/characters/put-delete/1/ && echo
		sleep 1
		echo
		echo '----------------------------------'
		;;

	abilities)

		# GET REQUESTS
		echo 'GET all AbilityScores'
		echo && curl -X GET localhost:8000/api/ability-scores && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by exact strength score, successful'
		echo && curl -X GET localhost:8000/api/ability-scores?strength=15 && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by exact strength score, unsuccessful'
		echo && curl -X GET localhost:8000/api/ability-scores?strength=16 && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by strength_above successful'
		echo && curl -X GET localhost:8000/api/ability-scores?strength_above=14 && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by strength_above unsuccessful'
		echo && curl -X GET localhost:8000/api/ability-scores?strength_above=16 && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by strength_below successful'
		echo && curl -X GET localhost:8000/api/ability-scores?strength_below=16 && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by strength_below unsuccessful'
		echo && curl -X GET localhost:8000/api/ability-scores?strength_below=14 && echo
		sleep 1
		echo
		echo '----------------------------------'

		echo 'Query by exact dexterity, successful'
		echo && curl -X GET localhost:8000/api/ability-scores?dexterity=15 && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Query by exact dexterity, unsuccesful'
		echo && curl -X GET localhost:8000/api/ability-scores?dexterity=16 && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by dexterity_above successful'
		echo && curl -X GET localhost:8000/api/ability-scores?dexterity_above=14 && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by dexterity_above unsuccessful'
		echo && curl -X GET localhost:8000/api/ability-scores?dexterity_above=16 && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by dexterity_below successful'
		echo && curl -X GET localhost:8000/api/ability-scores?dexterity_below=16 && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by dexterity_below unsuccessful'
		echo && curl -X GET localhost:8000/api/ability-scores?dexterity_below=14 && echo
		sleep 1
		echo
		echo '----------------------------------'

		echo 'Querying by exact constitution, successful'
		echo && curl -X GET localhost:8000/api/ability-scores?constitution=15 && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by exact constitution, unsuccessful'
		echo && curl -X GET localhost:8000/api/ability-scores?constitution=16 && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by constitution_above successful'
		echo && curl -X GET localhost:8000/api/ability-scores?constitution_above=14 && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by constitution_above unsuccessful'
		echo && curl -X GET localhost:8000/api/ability-scores?constitution_above=16 && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by constitution_below successful'
		echo && curl -X GET localhost:8000/api/ability-scores?constitution_below=16 && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by constitution_below unsuccessful'
		echo && curl -X GET localhost:8000/api/ability-scores?constitution_below=14 && echo
		sleep 1
		echo
		echo '----------------------------------'

		echo 'Querying by exact intelligence, successful'
		echo && curl -X GET localhost:8000/api/ability-scores?intelligence=8 && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by exact intelligence, unsuccessful'
		echo && curl -X GET localhost:8000/api/ability-scores?intelligence=9 && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by intelligence_above successful'
		echo && curl -X GET localhost:8000/api/ability-scores?intelligence_above=7 && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by intelligence_above unsuccessful'
		echo && curl -X GET localhost:8000/api/ability-scores?intelligence_above=9 && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by intelligence_below successful'
		echo && curl -X GET localhost:8000/api/ability-scores?intelligence_below=9 && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by intelligence_below unsuccessful'
		echo && curl -X GET localhost:8000/api/ability-scores?intelligence_below=7 && echo
		sleep 1
		echo
		echo '----------------------------------'

		echo 'Querying by exact wisdom, successful'
		echo && curl -X GET localhost:8000/api/ability-scores?wisdom=8 && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by exact wisdom, unsuccessful'
		echo && curl -X GET localhost:8000/api/ability-scores?wisdom=9 && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by wisdom_above successful'
		echo && curl -X GET localhost:8000/api/ability-scores?wisdom_above=7 && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by wisdom_above unsuccessful'
		echo && curl -X GET localhost:8000/api/ability-scores?wisdom_above=9 && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by wisdom_below successful'
		echo && curl -X GET localhost:8000/api/ability-scores?wisdom_below=9 && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by wisdom_below unsuccessful'
		echo && curl -X GET localhost:8000/api/ability-scores?wisdom_below=7 && echo
		sleep 1
		echo
		echo '----------------------------------'

		echo 'Querying by exact charisma, successful'
		echo && curl -X GET localhost:8000/api/ability-scores?charisma=8 && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by exact charisma, unsuccessful'
		echo && curl -X GET localhost:8000/api/ability-scores?charisma=9 && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by charisma_above successful'
		echo && curl -X GET localhost:8000/api/ability-scores?charisma_above=7 && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by charisma_above unsuccessful'
		echo && curl -X GET localhost:8000/api/ability-scores?charisma_above=9 && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by charisma_below successful'
		echo && curl -X GET localhost:8000/api/ability-scores?charisma_below=9 && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by charisma_below unsuccessful'
		echo && curl -X GET localhost:8000/api/ability-scores?charisma_below=7 && echo
		sleep 1
		echo
		echo '----------------------------------'


		# PUT REQUESTS

		echo 'Updating "strength" field of AbilityScore'
		echo && curl -X PUT -H "Content-Type: application/json" -d '{"strength": 17, "dexterity": 15, "constitution": 15, "intelligence": 8, "wisdom": 8, "charisma": 8}' localhost:8000/api/ability-scores/put-delete/1/ && echo
		sleep 1
		echo
		echo '----------------------------------'

		echo 'Updating "intelligence" and "wisdom" field of AbilityScore'
		echo && curl -X PUT -H "Content-Type: application/json" -d '{"strength": 17, "dexterity": 15, "constitution": 15, "intelligence": 9, "wisdom": 9, "charisma": 8}' localhost:8000/api/ability-scores/put-delete/1/ && echo
		sleep 1
		echo
		echo '----------------------------------'
		;;

	*)
		echo $"Usage: $0 {character|abilities}"
		exit 1
esac
