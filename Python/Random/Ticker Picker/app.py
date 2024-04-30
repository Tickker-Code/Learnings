import yfinance as yf

tickker = yf.Ticker(input(str("Ticker: $")))
#tickker = yf.Ticker('AAPL')



class Flee():
    
    def get_div():
        #div = tickker.info.get('dividend')
        try:
            div = tickker.dividends.iloc[-1]
        except:
            div = 0
        return div
    
    def get_pric():
        price = tickker.info.get('currentPrice')
        return price
    
    def amount_to_one():
        price = Flee.get_pric()
        div = Flee.get_div()
        try:
            amount = price / div
        except:
            amount = float(0)
        return amount
    
    def price_for_one():
        price = Flee.get_pric()
        amount = Flee.amount_to_one()
        try:
            money_needed = price * amount
        except:
            money_needed = 0
        return money_needed
    
divedend_amount = Flee.get_div()
stock_price = Flee.get_pric()
div_for_one_stock = Flee.amount_to_one()
total_money_for_one_stock_per_dividend = Flee.price_for_one()

if div_for_one_stock > 0:
    print(f'{tickker.ticker}\nStock Price: ${stock_price}\nDividend Amount: ${divedend_amount}\nTo buy one stock with dividends, you will need {div_for_one_stock} stocks for a total amount of ${total_money_for_one_stock_per_dividend}.')
else:
    print(f'{tickker.ticker}\nStock Price:${stock_price}\nNo dividends found.')