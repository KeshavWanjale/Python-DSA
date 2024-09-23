class PetrolPump:
    """
    Description:
        A class that represents a petrol pump.
    Attributes:
        petrol (int): Amount of petrol at the pump.
        distance (int): Distance from this pump to the next pump.
    """
    def __init__(self, petrol, distance):
        self.petrol = petrol
        self.distance = distance


def circular_tour(pumps):
    """
    Description:
        This function determines the first petrol pump index from where the truck can complete the circular tour.
    Parameters:
        pumps (list): A list of PetrolPump objects, each representing the petrol and distance of a petrol pump.
    Returns:
        int: The starting petrol pump index if the tour is possible, otherwise -1.
    """
    n = len(pumps)
    
    # Initialize start, end, and the current petrol in the truck
    start = 0
    current_petrol = 0
    extra_petrol_needed = 0
    
    # Traverse all the petrol pumps
    for i in range(n):
        current_petrol += pumps[i].petrol - pumps[i].distance
        
        # If current petrol goes negative, the current starting point is not valid
        if current_petrol < 0:
            # Store the deficit
            extra_petrol_needed += current_petrol
            # Move the start index to the next pump
            start = i + 1
            # Reset current petrol
            current_petrol = 0

    # After the loop, check if the extra petrol required (negative amount) can be compensated with available petrol
    if current_petrol + extra_petrol_needed >= 0:
        return start
    else:
        return -1


if __name__ == "__main__":
    pumps = [PetrolPump(4, 6), PetrolPump(6, 5), PetrolPump(7, 3), PetrolPump(4, 5)]
    start_pump_index = circular_tour(pumps)
    
    if start_pump_index != -1:
        print(f"The starting pump index is: {start_pump_index}")
    else:
        print("No solution possible, circular tour can't be completed.")
