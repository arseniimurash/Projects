def calculateTax(n,a,t):

    """This function is counting a value of netto summ without tax"""


    """ 1. n - a name of purpouse of payment = m_name (money name, str)
        2. a - amount of money = m_amount (money amount, float)
        3. t - a value of tax = tax (input any number without "%", float)
    """
    
    m_name = n
    m_amount = a
    tax = t
    tax_amount = (tax / 100) * m_amount
    m_netto = m_amount - ((tax / 100) * m_amount)

    """Type dict is chosen because it is more understandable format for work with variables and values"""

    money = {
        "Purpose of payment": m_name, 
        "Amount": m_amount, 
        "Tax": tax, 
        "Tax amount": round(tax_amount,2), 
        "Summ netto": round(m_netto,2)
    }

    """The result of return is a dict with original values and value of counted netto summ + amount of tax"""

    return money



