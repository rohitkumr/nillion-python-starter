from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    
    # Inputs from different parties
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party2))
    
    # Perform an addition operation between two secret integers from different parties
    new_int = my_int1 + my_int2
    
    # Return outputs for both parties
    output_for_party1 = Output(new_int, "result_for_party1", party1)
    output_for_party2 = Output(new_int, "result_for_party2", party2)
    
    return [output_for_party1, output_for_party2]

# This program demonstrates inter-party computation where two different parties
# input their secret integers and get the result of their sum without revealing
# their inputs to each other.

