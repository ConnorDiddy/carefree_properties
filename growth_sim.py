import matplotlib.pyplot as plt

# CONFIGURATION
SHOW_GRAPH = False


# CONSTANTS
NUMBER_OF_PEOPLE = 17                                           # Number of investors involved
BUYIN_AMOUNT = 25000                                            # Amount each investor contributes to start
YEARS_TO_RUN_SIMULATION_FOR = 25                                # Number of years to run simulation for
HYSA_ANNUAL_INTEREST_RATE = 0.05                                # Annual interest rate of High Yield Savings Account
HOME_APPRECIATION_INTEREST_RATE = 0.04                          # Expected rate at which the homes will appreciate (increases rent by the same amount)
ANNUAL_CONTRIBUTION_RATE_INCREASE_PERCENTAGE = 0.03             # Rate at which the annual contribution grows per member (set to 0 to keep a constant rate)


# INITIAL VALUES
house_count = 0
bank_account_value = NUMBER_OF_PEOPLE * BUYIN_AMOUNT
average_home_price = 425000
annual_property_profit = 25000
annual_contribution_rate = 7500
amount_invested_per_person = BUYIN_AMOUNT


# Graph stuff
portfolio_values = []

for month in range(1, (YEARS_TO_RUN_SIMULATION_FOR + 1) * 12):
    
    '''     Start of month          '''
    # Purchase new home if we have the money
    if bank_account_value >= average_home_price:
        bank_account_value -= average_home_price
        house_count += 1
        
        
    
    '''        End of month         '''
    # Collect rent money
    bank_account_value += (house_count * annual_property_profit / 12)
    
    # Collect contributions
    bank_account_value += ((NUMBER_OF_PEOPLE * annual_contribution_rate) / 12)
    amount_invested_per_person += annual_contribution_rate / 12
    
    # Calculate interest on cash
    bank_account_value *= (1 + (HYSA_ANNUAL_INTEREST_RATE / 12))
    
    # Calculate appreciation on homes
    average_home_price *= (1 + (HOME_APPRECIATION_INTEREST_RATE / 12))
    
    # Calculate rental increase
    annual_property_profit *= (1 + (HOME_APPRECIATION_INTEREST_RATE / 12))
        
    if month % 12 == 0:
        
        annual_contribution_rate *= (1 + ANNUAL_CONTRIBUTION_RATE_INCREASE_PERCENTAGE)
    
        portfolio_values.append(bank_account_value + average_home_price * house_count)
        
        amount_gained_per_person = (bank_account_value + average_home_price * house_count) / NUMBER_OF_PEOPLE
        profit_per_person = amount_gained_per_person - amount_invested_per_person
        total_portfolio_value = bank_account_value + average_home_price * house_count
        average_annual_interest_per_person = round((profit_per_person) / YEARS_TO_RUN_SIMULATION_FOR / amount_invested_per_person * 100, 3)
        
        print(f"======= END OF Year {month // 12} =======")
        print("House count:", house_count)
        print("Cash in bank: ",  "${:.2f}".format(bank_account_value))
        print("Total portfolio value:", "${:.2f}".format(total_portfolio_value))
        print("Average home price:", "${:.2f}".format(average_home_price))
        print("Average monthly rent:", "${:.2f}".format(annual_property_profit / 12))
        print("Annual contribution rate:", "${:.2f}".format(annual_contribution_rate))
        print("Amount gained per person:", "${:.2f}".format(amount_gained_per_person))
        print("Amount invested per person:", "${:.2f}".format(amount_invested_per_person))
        print("Profit per person:", "${:.2f}".format(profit_per_person))
        print("Average annual interest earned per person: " + str(average_annual_interest_per_person) + '%')
        print("\n\n")
        

if SHOW_GRAPH:
    # show y axis in thousands
    plt.yticks([0, 2000000, 4000000, 6000000, 8000000, 10000000, 12000000, 16000000, 20000000, 25000000, 30000000], ['0', '2M', '4M', '6M', '8M', '10M', '12M', '16M', '20M', '25M', '30M'])
    #plt.ylim(0, 10000000)
    plt.plot(portfolio_values)

    # set the title of the graph
    plt.title('Carefree Properties')

    # set the x and y axis labels
    plt.xlabel('Years')
    plt.ylabel('Portfolio Value')
    plt.show()
