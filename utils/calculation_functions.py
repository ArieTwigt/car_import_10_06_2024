from typing import Union, Tuple
import math

# define the function for pythagoras
def calc_pythagoras(a: Union[float, int], 
                    b: Union[float, int]) -> float:
    """
    Function to calculate Pythagoras theorem

    Input: 
    * a and b

    Output:
    * c
    
    
    """

    # calculate c_sqrd
    c_sqrd = a ** 2 + b ** 2
    c = c_sqrd ** 0.5

    return c


# define the function for the circle
def calc_circle(diameter: Union[float, int]) -> Tuple[float, float]:
    '''
    Function to calculate the size of a circle

    Input:
    * Diameter of the circle


    Output:
    * Area of the circle
    * Radius
    
    '''

    # check for the allowed types
    allowed_types = (int, float)

    if type(diameter) not in allowed_types:
        raise TypeError("Diameter is not of required types.🥞Pannenkoek!")

    # calculate the radius
    radius = diameter / 2

    # calculate the area
    area = math.pow(radius, 2) * math.pi

    return area, radius

