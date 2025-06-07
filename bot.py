
fro
previous_price = {}
previous_open_interest = {}
en_interest(category=MARKET, symbol=symbol, intervalTime=OPEN_INTEREST_INTERVAL)
            if open_interest_data and open_interest_data["retCode"] == 0 and open_interest_data["result"]["list"]:
                open_interes["result"]["list"][0]["openInterest"])
            else:
                print(f"Ошибка при получении открытого интереса для {symbol}: {open_interest_data}")
                open_interest = None
        else:
            open_interest = None

        return volume, open_interest, None, None, last_price # Убрал лишнее возвращаемое значение
    except Exception as e:
        prinNone, None, None, None # Убрал лишнее None

async def analyze_market_data(client, symbol):
    print(f"Запрос данных для {symbol}...")    
