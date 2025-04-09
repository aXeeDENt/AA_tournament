def strategy(my_history: list[int], opponent_history: list[int], rounds: int | None) -> int:
    if len(my_history) == 0: return 0 
    elif len(my_history) == 1: return 1  
    elif len(my_history) == 2: return 1 
    elif len(my_history) == 3: return 1  
    elif len(my_history) == 4: return 0  
    
    move_number = len(my_history)
    cycle_position = ((move_number - 5) // 5) % 4 
    position_in_situation = (move_number - 5) % 5 
    
    if cycle_position == 0:
        opponent_index = move_number - 5
        if opponent_index < len(opponent_history):
            return 1 - opponent_history[opponent_index] 
        return 0 
    
    elif cycle_position == 1:
        opponent_index = move_number - 5
        if opponent_index < len(opponent_history):
            return opponent_history[opponent_index]
        return 1  
    
    elif cycle_position == 2:
        if position_in_situation == 4: return 1  
        else:
            opponent_index = move_number - 5
            if opponent_index < len(opponent_history):
                return opponent_history[opponent_index]
            return 1  
    
    else:  
        seed = move_number
        if opponent_history:
            seed += opponent_history[-1] * 2
        
        if len(opponent_history) > 3:
            seed += sum(opponent_history[-3:]) * 3
            
        pseudo_random = (seed * 1337 + 42) % 100
        return 1 if pseudo_random > 50 else 0
