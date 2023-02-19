
''' 
Count tax from input amount, interest and purpose.

Args: 
     amount: amount of money to calculate tax
     interest: interest rate to be applied on amount
     purpose: purpose for which tax was applied

Return:
    4 values: amount, interest, tax, purpose.

Raises:
     "TypeError for wrong arg types
'''

def calculateTax(amount, interest, purpose) :
    if type(amount) != float :  
        raise TypeError("Must be float or int") 
    if type(interest) != float : 
        raise TypeError("Must be float or int")
    
    tax = amount * (interest/100)
    result = { 
        "amount"  : amount, 
        "interest": interest, 
        "tax"     : tax,  
        "purpose" : purpose}
    return result
    

# - used dict for better visibility and understanding of the values
# - the posibility to use any key separatly and add more values


