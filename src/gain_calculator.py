import yfinance as yf
import pandas as pd

# used venv 3.10.11

 


def gain(tkr_from_usr):
    quotes = yf.download(tkr_from_usr, period = '1mo')
    pd.set_option('display.max_columns', None)

    df = pd.DataFrame(quotes) # , dtype="Int64"
    print(df.columns)
    #return "here is the tkr from usr "+ tkr_from_usr
    adj_close = []
    for i in df['High'][tkr_from_usr.upper()]:
        adj_close.append(int(i))    

    #this gets the individual elements in a pandas tuple
    print(adj_close[0],"type", type(adj_close[0]))

    all_time_hi = 0
    i = 0

    run_sum = 0
    #highest_close = 0 #highest point reached in a 10 day window
    local_max = -50 #highest point reached in a 10 day window
    day_count = 0
    while i < len(adj_close):
        print(adj_close[i]," and type ", type(adj_close[i]))

        if i < len(adj_close) - 1: # don't check passed the list limit
            dif = adj_close[i+1] - adj_close[i]
            print("adj_close [", i + 1, "]", adj_close[i + 1], "-", "adj_close[", i, "]", adj_close[i], " || local_max   ",
                local_max, end='')

            print("         |||    dif", dif)
        if day_count < 10: # days less than the ammount chosen by user, default 10 todo change 10 to variable
            run_sum += dif
            day_count += 1
            if run_sum > local_max:
                local_max = run_sum

        if day_count == 10:
            print("local_max:",local_max)
            if local_max > all_time_hi:
                all_time_hi = local_max
            run_sum, highest_close, day_count = 0, 0, 0
            local_max = 0
        
        i += 1
    
    return str(all_time_hi)
    print("all time max", all_time_hi)

