
# Data

#Movies
m_title_1 = "Avatar 2"  
m_title_2 = "Terminator 9"
m_title_3 = "Titanic Zombie"

#Tickets cost
m_1_ticket_a_cost = 100
m_1_ticket_b_cost = 120
m_2_ticket_a_cost = 200
m_2_ticket_b_cost = 150
m_3_ticket_a_cost = 100


from os import system
system ('cls')


print(
f"""
1. {m_title_1}:
    a. 18:00
    b. 20:00
    
2. {m_title_2}:
    a. 16:00
    b. 23:00

3. {m_title_3}:
    a. 18:00
"""
)

movie_number = input("Choose a movie: ")

    # Movie 1
if movie_number == '1':
    print(f'You have chosen {m_title_1}')
    time = input('Choose time: ')
    cost = 0
    if time == 'a':
        cost = m_1_ticket_a_cost
        print(f'time: 18:00, ticket cost {m_1_ticket_a_cost}')
        amount_tickets = int(input('How many tickets: '))
        total = amount_tickets * cost
        print(f'Thank you! You choosed {m_title_1}, tickets cost: {amount_tickets} x {cost} = {total}')
    elif time == 'b':
        cost = m_1_ticket_b_cost
        print(f'time: 20:00, ticket cost {m_1_ticket_b_cost}')
        amount_tickets = int(input('How many tickets: '))
        total = amount_tickets * cost
        print(f'Thank you! You choosed {m_title_1}, tickets cost: {amount_tickets} x {cost} = {total}')
    else:
        print('Please, choose the correct film time.')
    

    # Movie 2
elif movie_number == '2':
    print(f'You have chosen {m_title_2}')
    time = input('Choose time: ')
    cost = 0
    if time == 'a':
        cost = m_2_ticket_a_cost
        print(f'time: 18:00, ticket cost {m_2_ticket_a_cost}')
        amount_tickets = int(input('How many tickets: '))
        total = amount_tickets * cost
        print(f'Thank you! You choosed {m_title_2}, tickets cost: {amount_tickets} x {cost} = {total}')
    elif time == 'b':
        cost = m_2_ticket_b_cost
        print(f'time: 20:00, ticket cost {m_2_ticket_b_cost}')
        amount_tickets = int(input('How many tickets: '))
        total = amount_tickets * cost
        print(f'Thank you! You choosed {m_title_2}, tickets cost: {amount_tickets} x {cost} = {total}')
    else:
        print('Please, choose the correct film time.')
    
    # Movie 3   
elif movie_number == '3':
    print(f'You have chosen {m_title_3}')
    time = input('Choose time: ')
    cost = 0
    if time == 'a':
        cost = m_3_ticket_a_cost
        print(f'time: 18:00, ticket cost {m_3_ticket_a_cost}')
        amount_tickets = int(input('How many tickets: '))
        total = amount_tickets * cost
        print(f'Thank you! You choosed {m_title_3}, tickets cost: {amount_tickets} x {cost} = {total}')
    else:
        print('Please, choose the correct film time.')
else:
    print('Please, choose the correct film number.')


