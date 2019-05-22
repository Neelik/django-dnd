#!/usr/bin/env bash


case "$1" in
	demo)
        echo "Beginning creation of 'Therdrin Oreforger' character"
        echo "-----------------------------------------------------"
        sleep 1
        echo "Creating entry in Character table"
        echo && curl -X POST -H "Content-Type: application/json" -d '{"level": 11, "alignment": "Chaotic Good", "race": "Dwarf", "name": "Therdrin Oreforger", "player_name": "Garrett", "character_class": "Barbarian"}' localhost:8000/api/characters/create/ && echo
        echo "-----------------------------------------------------"
        sleep 1
        echo "Create entry in Combat Info table"
        echo && curl -X POST -H "Content-Type: application/json" -d '{"armor_class": 18, "initiative": 3, "speed": 35, "total_hit_points": 185, "current_hit_points": 185, "hit_dice_total": 9, "hit_dice": "d12" }' localhost:8000/api/combat-info/create/ && echo
        echo "-----------------------------------------------------"
        sleep 1
        echo "Create entry in Ability Score table"
        echo && curl -X POST -H "Content-Type: application/json" -d '{"strength": 20, "dexterity": 16, "constitution": 20, "intelligence": 12, "wisdom": 13, "charisma": 10 }' localhost:8000/api/ability-scores/create/ && echo
        echo "-----------------------------------------------------"
        sleep 1
        echo "Creating entry in Skills table"
        echo && curl -X POST -H "Content-Type: application/json" -d '{"ability_score": 3 }' localhost:8000/api/skills/create/ && echo
        echo "-----------------------------------------------------"
        sleep 1
        echo "Creating entry in Save table"
        echo && curl -X POST -H "Content-Type: application/json" -d '{"ability_score": 3 }' localhost:8000/api/save/create/ && echo
        echo "-----------------------------------------------------"
        sleep 1
        echo "Creating entry in PhysicalAttack table"
        echo && curl -X POST -H "Content-Type: application/json" -d '{"ability_score": 3, "name": "Vicious Great Axe", "damage_type": "sl", "dice_type": "d12", "dice_count": 1 }' localhost:8000/api/physical-attack/create/ && echo
        echo "-----------------------------------------------------"
        sleep 1
        echo "Creating entry in Background table"
        echo && curl -X POST -H "Content-Type: application/json" -d '{"name": "Noble", "traits": "If you do me an injury, I will crush you, ruin your name, and salt your fields", "ideals": "I must prove that I can handle myself without the coddling of my family", "bonds": "The common folk must see me as a her of the people.", "flaws": "I too often hear veiled insults and threats in every word addressed me and I am quick anger."}' localhost:8000/api/background/create/ && echo
        echo "-----------------------------------------------------"
        echo "Character 'Therdrin Oreforger COMPLETE!"
        ;;

    background)
        # POST REQUESTS
	    echo
	    echo '----------------------------------'
	    echo 'Making a successful POST'
	    echo && curl -X POST -H "Content-Type: application/json" -d '{"name": "Acolyte", "spec": "Boss", "feature": "Shelter of the Faithful", "traits": "Pompous", "ideals": "Tradition", "bonds": "Owes an unpayable debt to an elder priest", "flaws": "Often considers themselves in the right, even when their not.", "equipment": "Robes"}' localhost:8000/api/background/create/ && echo
	    sleep 1
	    echo

        # GET REQUESTS
        echo
		echo '----------------------------------'
		echo 'GET for all Backgrounds'
		echo && curl -X GET localhost:8000/api/background && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by name, successful'
		echo && curl -X GET localhost:8000/api/background?name=Acolyte && echo
		sleep 1
        echo
		echo '----------------------------------'
		echo 'Query by name that does not exist'
		echo && curl -X GET localhost:8000/api/background?name=Me && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by spec, successful'
		echo && curl -X GET localhost:8000/api/background?spec=Boss && echo
		sleep 1
        echo
		echo '----------------------------------'
		echo 'Query by spec that does not exist'
		echo && curl -X GET localhost:8000/api/background?spec=Noob && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by equipment, successful'
		echo && curl -X GET localhost:8000/api/background?equipment=Robes && echo
		sleep 1
        echo
		echo '----------------------------------'
		echo 'Query by equipment that does not exist'
		echo && curl -X GET localhost:8000/api/background?equipment=dagger && echo
		sleep 1
        
        
        # PUT REQUESTS
        echo
	    echo '----------------------------------'
	    echo 'Updating "name" field of Background'
	    echo && curl -X PUT -H "Content-Type: application/json" -d '{"name": "Noble"}' localhost:8000/api/background/put-delete/8/ && echo
	    sleep 1
	    echo
	    echo '----------------------------------'
	    echo 'Updating "spec" field of Background'
	    echo && curl -X PUT -H "Content-Type: application/json" -d '{"spec": ""}' localhost:8000/api/background/put-delete/8/ && echo
	    sleep 1
	    echo
	    echo '----------------------------------'
	    echo 'Updating "feature" field of Background'
	    echo && curl -X PUT -H "Content-Type: application/json" -d '{"feature": "Rich"}' localhost:8000/api/background/put-delete/8/ && echo
	    sleep 1
	    echo
	    echo '----------------------------------'
	    echo 'Updating "alt_feature" field of Background'
	    echo && curl -X PUT -H "Content-Type: application/json" -d '{"alt_feature": "Mine Owner"}' localhost:8000/api/background/put-delete/8/ && echo
	    sleep 1
	    echo
	    echo '----------------------------------'
	    echo 'Updating "traits" field of Background'
	    echo && curl -X PUT -H "Content-Type: application/json" -d '{"traits": ""}' localhost:8000/api/background/put-delete/8/ && echo
	    sleep 1
	    echo
	    echo '----------------------------------'
	    echo 'Updating "ideals" field of Background'
	    echo && curl -X PUT -H "Content-Type: application/json" -d '{"ideals": ""}' localhost:8000/api/background/put-delete/8/ && echo
	    sleep 1
	    echo
	    echo '----------------------------------'
	    echo 'Updating "bonds" field of Background'
	    echo && curl -X PUT -H "Content-Type: application/json" -d '{"bonds": "Broken"}' localhost:8000/api/background/put-delete/8/ && echo
	    sleep 1
	    echo
	    echo '----------------------------------'
	    echo 'Updating "flaws" field of Background'
	    echo && curl -X PUT -H "Content-Type: application/json" -d '{"flaws": "None"}' localhost:8000/api/background/put-delete/8/ && echo
	    sleep 1
	    echo
	    echo '----------------------------------'
	    echo 'Updating "equipment" field of Background'
	    echo && curl -X PUT -H "Content-Type: application/json" -d '{"equipment": "Rope"}' localhost:8000/api/background/put-delete/8/ && echo
	    sleep 1
	    ;;

    attack)
        # POST REQUESTS
	    echo
	    echo '----------------------------------'
	    echo 'Making a successful POST'
	    echo && curl -X POST -H "Content-Type: application/json" -d '{"ability_score": 4, "name": "Great Axe", "damage_type": "sl", "dice_type": "d12", "dice_count": 1}' localhost:8000/api/physical-attack/create/ && echo
	    sleep 1
	    echo

        # GET REQUESTS
        echo
		echo '----------------------------------'
		echo 'GET for all Physical Attacks'
		echo && curl -X GET localhost:8000/api/physical-attack && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by name, successful'
		echo && curl -X GET localhost:8000/api/physical-attack?name=Great && echo
		sleep 1
        echo
		echo '----------------------------------'
		echo 'Query by name that does not exist'
		echo && curl -X GET localhost:8000/api/physical-attack?name=Blade && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by damage_type, successful'
		echo && curl -X GET localhost:8000/api/physical-attack?damage_type=sl && echo
		sleep 1
        echo
		echo '----------------------------------'
		echo 'Query by damage_type that does not exist'
		echo && curl -X GET localhost:8000/api/physical-attack?damage_type=bl && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by dice_type, successful'
		echo && curl -X GET localhost:8000/api/physical-attack?dice_type=d12 && echo
		sleep 1
        echo
		echo '----------------------------------'
		echo 'Query by dice_type that does not exist'
		echo && curl -X GET localhost:8000/api/physical-attack?dice_type=d6 && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by dice_count, successful'
		echo && curl -X GET localhost:8000/api/physical-attack?dice_count=1 && echo
		sleep 1
        echo
		echo '----------------------------------'
		echo 'Query by dice_count that does not exist'
		echo && curl -X GET localhost:8000/api/physical-attack?dice_count=2 && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by dice_count_above, successful'
		echo && curl -X GET localhost:8000/api/physical-attack?dice_count_above=0 && echo
		sleep 1
        echo
		echo '----------------------------------'
		echo 'Query by dice_count_above that does not exist'
		echo && curl -X GET localhost:8000/api/physical-attack?dice_count_above=2 && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by dice_count_below, successful'
		echo && curl -X GET localhost:8000/api/physical-attack?dice_count_below=2 && echo
		sleep 1
        echo
		echo '----------------------------------'
		echo 'Query by dice_count_below that does not exist'
		echo && curl -X GET localhost:8000/api/physical-attack?dice_count_below=0 && echo
		sleep 1
        ;;

    spellcasting)
        # POST REQUESTS
	    echo
	    echo '----------------------------------'
	    echo 'Making a successful POST'
	    echo && curl -X POST -H "Content-Type: application/json" -d '{"ability_score": 4, "spellcasting_ability": "Int"}' localhost:8000/api/spellcasting/create/ && echo
	    sleep 1

	    # GET REQUESTS
        echo
		echo '----------------------------------'
		echo 'GET for all Spellcasting'
		echo && curl -X GET localhost:8000/api/ability-scores/4/spellcasting && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying for only the spell_attack field'
		echo && curl -X GET localhost:8000/api/ability-scores/4/spellcasting?field=attack && echo
		sleep 1
        echo
		echo '----------------------------------'
		echo 'Querying for only the spell_save field'
		echo && curl -X GET localhost:8000/api/ability-scores/4/spellcasting?field=spell_save && echo
		sleep 1
		echo
        ;;

    combat)
        # POST REQUESTS
	    echo
	    echo '----------------------------------'
	    echo 'Making a successful POST'
	    echo && curl -X POST -H "Content-Type: application/json" -d '{"armor_class": 18, "current_hit_points": 80, "hit_dice": "d10"}' localhost:8000/api/combat-info/create/ && echo
	    sleep 1

	    # GET REQUESTS
        echo
		echo '----------------------------------'
		echo 'GET for all Spellcasting'
		echo && curl -X GET localhost:8000/api/combat-info && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by armor_class, successful'
		echo && curl -X GET localhost:8000/api/combat-info?armor_class=18 && echo
		sleep 1
        echo
		echo '----------------------------------'
		echo 'Querying by armor_class, unsuccessful'
		echo && curl -X GET localhost:8000/api/combat-info?armor_class=17 && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by armor_class_above, successful'
		echo && curl -X GET localhost:8000/api/combat-info?armor_class_above=17 && echo
		sleep 1
        echo
		echo '----------------------------------'
		echo 'Querying by armor_class_above, unsuccessful'
		echo && curl -X GET localhost:8000/api/combat-info?armor_class_above=19 && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by armor_class_below, successful'
		echo && curl -X GET localhost:8000/api/combat-info?armor_class_below=19 && echo
		sleep 1
        echo
		echo '----------------------------------'
		echo 'Querying by armor_class_below, unsuccessful'
		echo && curl -X GET localhost:8000/api/combat-info?armor_class=17 && echo
		sleep 1

		# PUT REQUESTS
		echo
	    echo '----------------------------------'
	    echo 'Updating "armor_class" field of Combat Info'
	    echo && curl -X PUT -H "Content-Type: application/json" -d '{"armor_class": 20, "hit_dice": "d10"}' localhost:8000/api/combat-info/put-delete/7/ && echo
	    sleep 1
	    echo
	    echo '----------------------------------'
	    echo 'Updating "speed" field of Combat Info'
	    echo && curl -X PUT -H "Content-Type: application/json" -d '{"speed": 30, "hit_dice": "d10"}' localhost:8000/api/combat-info/put-delete/7/ && echo
	    sleep 1
	    echo
	    echo '----------------------------------'
	    echo 'Updating "total_hit_points" field of Combat Info'
	    echo && curl -X PUT -H "Content-Type: application/json" -d '{"total_hit_points": 10, "hit_dice": "d10"}' localhost:8000/api/combat-info/put-delete/7/ && echo
	    sleep 1
	    echo
	    echo '----------------------------------'
	    echo 'Updating "current_hit_points" field of Combat Info'
	    echo && curl -X PUT -H "Content-Type: application/json" -d '{"current_hit_points": 10, "hit_dice": "d10"}' localhost:8000/api/combat-info/put-delete/7/ && echo
	    sleep 1
	    echo
	    echo '----------------------------------'
	    echo 'Updating "hit_dice_total" field of Combat Info'
	    echo && curl -X PUT -H "Content-Type: application/json" -d '{"hit_dice_total": 3, "hit_dice": "d10"}' localhost:8000/api/combat-info/put-delete/7/ && echo
	    sleep 1
	    echo
	    echo '----------------------------------'
	    echo 'Updating "hit_dice" field of Combat Info'
	    echo && curl -X PUT -H "Content-Type: application/json" -d '{"hit_dice": "d8"}' localhost:8000/api/combat-info/put-delete/7/ && echo
	    sleep 1
        ;;

    equipment)
        # POST REQUESTS
	    echo
	    echo '----------------------------------'
	    echo 'Making a successful POST'
	    echo && curl -X POST -H "Content-Type: application/json" -d '{"equipment_name": "Sun Blade", "equipment_type": "Weapon", "is_magic": "true"}' localhost:8000/api/equipment/create/ && echo
	    sleep 1

	    # GET REQUESTS
	    echo
		echo '----------------------------------'
		echo 'GET for all Equipment'
		echo && curl -X GET localhost:8000/api/equipment && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by "equipment_name", successful'
		echo && curl -X GET localhost:8000/api/equipment?equipment_name=Sun && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by "equipment_name", unsuccessful'
		echo && curl -X GET localhost:8000/api/equipment?equipment_name=Gun && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by "equipment_type", successful'
		echo && curl -X GET localhost:8000/api/equipment?equipment_type=Weapon && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by "equipment_type", unsuccessful'
		echo && curl -X GET localhost:8000/api/equipment?equipment_type=Armor && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by "is_magic", successful'
		echo && curl -X GET localhost:8000/api/equipment?is_magic=True && echo
		sleep 1
		echo
		echo '----------------------------------'
		echo 'Querying by "is_magic", unsuccessful'
		echo && curl -X GET localhost:8000/api/equipment?is_magic=False && echo
		sleep 1
        ;;

    *)
		echo $"Usage: $0 {demo|background|attack|spellcasting|combat|equipment}"
		exit 1
esac