def strategy_round_2(opponent_id: int, my_history: dict[int, list[int]], opponents_history: dict[int, list[int]]) -> tuple[int, int]:
    """Enhanced strategy for Round 2 with updated opponent selection"""
    # Get current histories
    current_my = my_history.get(opponent_id, [])
    current_op = opponents_history.get(opponent_id, [])
    
    # Calculate move using original logic
    if len(current_my) == 0: move = 0
    elif len(current_my) == 1: move = 1
    elif len(current_my) == 2: move = 1
    elif len(current_my) == 3: move = 1
    elif len(current_my) == 4: move = 0
    else:
        move_number = len(current_my)
        cycle_pos = ((move_number - 5) // 5) % 4
        pos_in_sit = (move_number - 5) % 5
        
        if cycle_pos == 0:
            opp_idx = move_number - 5
            move = 1 - current_op[opp_idx] if opp_idx < len(current_op) else 0
        elif cycle_pos == 1:
            opp_idx = move_number - 5
            move = current_op[opp_idx] if opp_idx < len(current_op) else 1
        elif cycle_pos == 2:
            move = 1 if pos_in_sit == 4 else (current_op[move_number-5] if move_number-5 < len(current_op) else 1)
        else:
            seed = move_number
            if current_op: seed += current_op[-1] * 2
            if len(current_op) > 3: seed += sum(current_op[-3:]) * 3
            move = 1 if (seed * 1337 + 42) % 100 > 50 else 0

    # Classify opponents based on their first 4 moves (updated categories)
    categories = {
        'best': [],    # 1111
        'good': [],    # 1110, 1011, 1101, 0111
        'normal': [],  # 0011, 0101, 0110, 1001, 1010, 1100
        'bad': [],     # 0001, 0100, 0010, 1000
        'worst': []    # 0000
    }
    
    for opp_id in opponents_history:
        # Skip if we've played 200 rounds with this opponent
        if len(my_history.get(opp_id, [])) >= 200:
            continue
            
        # Get first 4 moves (pad with 1 if needed)
        first_four = opponents_history[opp_id][:4]
        if len(first_four) < 4:
            first_four = first_four + [1]*(4-len(first_four))
        
        # Classify based on the new specifications
        if first_four == [1,1,1,1]:
            categories['best'].append(opp_id)
        elif first_four in [[1,1,1,0], [1,0,1,1], [1,1,0,1], [0,1,1,1]]:
            categories['good'].append(opp_id)
        elif first_four in [[0,0,1,1], [0,1,0,1], [0,1,1,0], [1,0,0,1], [1,0,1,0], [1,1,0,0]]:
            categories['normal'].append(opp_id)
        elif first_four in [[0,0,0,1], [0,1,0,0], [0,0,1,0], [1,0,0,0]]:
            categories['bad'].append(opp_id)
        elif first_four == [0,0,0,0]:
            categories['worst'].append(opp_id)
        else:
            # Default classification based on cooperation count
            coop_count = sum(first_four)
            if coop_count == 4: categories['best'].append(opp_id)
            elif coop_count == 3: categories['good'].append(opp_id)
            elif coop_count == 2: categories['normal'].append(opp_id)
            elif coop_count == 1: categories['bad'].append(opp_id)
            else: categories['worst'].append(opp_id)
    
    # Select next opponent by priority (best → good → normal → bad → worst)
    for category in ['best', 'good', 'normal', 'bad']:
        if categories[category]:
            # Within category, prefer opponents we've played less with
            sorted_opp = sorted(categories[category], key=lambda x: len(my_history.get(x, [])))
            
            # Stick with current opponent if they're in this category and under 200 rounds
            if opponent_id in sorted_opp and len(my_history.get(opponent_id, [])) < 200:
                return (move, opponent_id)
                
            # Otherwise pick the least played opponent in this category
            return (move, sorted_opp[0])
    
    # Only worst opponents available (play them minimally)
    if categories['worst']:
        return (move, min(categories['worst'], key=lambda x: len(my_history.get(x, []))))
    
    # Fallback (shouldn't happen as per tournament rules)
    return (move, opponent_id)
