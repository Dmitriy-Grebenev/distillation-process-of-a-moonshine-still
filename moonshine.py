def distillation(ferment_volume, alcohol_content):
    """
    Simulates the distillation process of a moonshine still.
    
    Parameters:
        ferment_volume (float): The volume of fermented mash to distill in liters.
        alcohol_content (float): The alcohol content of the fermented mash in percent.
        
    Returns:
        float: The volume of distilled alcohol in liters.
    """
    # Constants
    BOILING_POINT = 78.37   # The boiling point of ethanol in degrees Celsius.
    ETHANOL_DENSITY = 0.789 # The density of ethanol in grams per milliliter.
    
    # Convert the alcohol content from percent to fraction.
    alcohol_fraction = alcohol_content / 100
    
    # Calculate the mass of ethanol in the ferment.
    ferment_mass = ferment_volume * alcohol_fraction * ETHANOL_DENSITY
    
    # Calculate the volume of ethanol vapor produced during distillation.
    vapor_volume = ferment_mass / ETHANOL_DENSITY
    
    # Calculate the volume of condensed ethanol.
    condensed_volume = vapor_volume * 0.9
    
    # Calculate the alcohol content of the condensed ethanol.
    condensed_alcohol_fraction = condensed_volume / ferment_volume
    
    # Calculate the volume of distilled alcohol.
    distilled_volume = condensed_volume * (condensed_alcohol_fraction / alcohol_fraction)
    
    return distilled_volume


