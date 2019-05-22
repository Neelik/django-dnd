#!/usr/bin/env bash

case "$1" in
	skills)
	    # POST REQUESTS
	    echo
	    echo '----------------------------------'
	    echo 'Making a successful POST'
	    echo && curl -X POST -H "Content-Type: application/json" -d '{"ability_score": 1}' localhost:8000/api/skills/create/ && echo
	    sleep 1
	    echo
	    echo '----------------------------------'
	    echo 'Making an unsuccessful POST'
	    echo && curl -X POST -H "Content-Type: application/json" -d '{"ability_score": 9999}' localhost:8000/api/skills/create/ && echo
	    sleep 1

		# GET REQUESTS
		echo
		echo '----------------------------------'
		echo 'GET for all Skills'
		echo && curl -X GET localhost:8000/api/skills && echo
		sleep 1
		;;

	saves)
	    # POST Requests
	    echo
	    echo '----------------------------------'
	    echo 'Making a successful POST'
	    echo && curl -X POST -H "Content-Type: application/json" -d '{"ability_score": 1}' localhost:8000/api/save/create/ && echo
	    sleep 1
	    echo
	    echo '----------------------------------'
	    echo 'Making an unsuccessful POST'
	    echo && curl -X POST -H "Content-Type: application/json" -d '{"ability_score": 9999}' localhost:8000/api/save/create/ && echo
	    sleep 1

		# GET REQUESTS
		echo 'GET all Saves'
		echo && curl -X GET localhost:8000/api/ability-scores/1/saves && echo
		sleep 1
		echo
		echo '----------------------------------'
		;;

	char_constraints)
	    echo 'Creating new Character with data "{"level": 11, "alignment": "Chaotic Good", "race": "Dwarf", "name": "Character 2", "player_name": "Player 2", "character_class": "Paladin"}"'
		echo && curl -X POST -H "Content-Type: application/json" -d '{"level": 11, "alignment": "Chaotic Good", "race": "Dwarf", "name": "Character 2", "player_name": "Player 2", "character_class": "Paladin"}' localhost:8000/api/characters/create/ && echo
		sleep 1
		echo
		echo '----------------------------------'

		echo 'Constraint violation with same data "{"level": 11, "alignment": "Chaotic Good", "race": "Dwarf", "name": "Character 2", "player_name": "Player 2", "character_class": "Paladin"}"'
		echo && curl -X POST -H "Content-Type: application/json" -d '{"level": 11, "alignment": "Chaotic Good", "race": "Dwarf", "name": "Character 2", "player_name": "Player 2", "character_class": "Paladin"}' localhost:8000/api/characters/create/ && echo
		sleep 1
		echo
		echo '----------------------------------'

		echo 'Constraint success with new race "{"level": 11, "alignment": "Chaotic Good", "race": "Elf", "name": "Character 2", "player_name": "Player 2", "character_class": "Paladin"}"'
		echo && curl -X POST -H "Content-Type: application/json" -d '{"level": 11, "alignment": "Chaotic Good", "race": "Elf", "name": "Character 2", "player_name": "Player 2", "character_class": "Paladin"}' localhost:8000/api/characters/create/ && echo
		sleep 1
		echo
		echo '----------------------------------'

		echo 'Constraint success with new player "{"level": 11, "alignment": "Chaotic Good", "race": "Dwarf", "name": "Character 2", "player_name": "Player 3", "character_class": "Paladin"}"'
		echo && curl -X POST -H "Content-Type: application/json" -d '{"level": 11, "alignment": "Chaotic Good", "race": "Dwarf", "name": "Character 2", "player_name": "Player 3", "character_class": "Paladin"}' localhost:8000/api/characters/create/ && echo
		sleep 1
		echo
		echo '----------------------------------'

		echo 'Constraint success with new class "{"level": 11, "alignment": "Chaotic Good", "race": "Dwarf", "name": "Character 2", "player_name": "Player 2", "character_class": "Barbarian"}"'
		echo && curl -X POST -H "Content-Type: application/json" -d '{"level": 11, "alignment": "Chaotic Good", "race": "Dwarf", "name": "Character 2", "player_name": "Player 2", "character_class": "Barbarian"}' localhost:8000/api/characters/create/ && echo
		sleep 1
		echo
		echo '----------------------------------'

		echo 'Constraint success with new name "{"level": 11, "alignment": "Chaotic Good", "race": "Dwarf", "name": "Character 3", "player_name": "Player 2", "character_class": "Paladin"}"'
		echo && curl -X POST -H "Content-Type: application/json" -d '{"level": 11, "alignment": "Chaotic Good", "race": "Dwarf", "name": "Character 3", "player_name": "Player 2", "character_class": "Paladin"}' localhost:8000/api/characters/create/ && echo
		sleep 1
		echo
		echo '----------------------------------'

		echo 'GET for all Characters "count" field should read 5'
		echo && curl -X GET localhost:8000/api/characters && echo
		sleep 1
		echo
		echo '----------------------------------'

	    ;;

	*)
		echo $"Usage: $0 {skills|saves|char_constraints}"
		exit 1
esac
