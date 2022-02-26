from blackfunc import *
from blackfuncplt import *

def main():

    # Define and initialize arguments
    stck_p = 30
    strike_p = 25
    time_to_mat = 0.1
    rf_rate = 0.02
    div_yield = 0.00
    stck_vol = 0.2
   
    # Compute call price
    call_price = call_bs(stck_p, strike_p, time_to_mat, rf_rate, div_yield, stck_vol)
    print(f'Call price: {round(call_price,4)}')
   
    # Compute put price
    put_price = put_bs(stck_p, strike_p, time_to_mat, rf_rate, div_yield, stck_vol)
    print(f'Put price: {round(put_price,4)}')
   
    # Plot call price vs. partial parameter change
    call_des(stck_p, strike_p, time_to_mat, rf_rate, div_yield, stck_vol)
   
    # Plot put price vs. partial parameter change
    put_des(stck_p, strike_p, time_to_mat, rf_rate, div_yield, stck_vol)


if __name__ == '__main__':
    main()
