import asyncio
import time
import telebot



previous_volume = {}
previous_open_interest = {}


def initialize_client():
    """
    Инициализирует API клиент для Unified Trading API.
м, открытый интерес, данные о сделках)
    используя Unified Trading API.
    """

        trades = client.get_public_trade_history(category=MARKET, symbol=symbol, limit=200)

        if trades and trades["retCode"] == 0 and trades["result"]["list"]:
            buy_volume = sum(
                float(trade["size"]) for trade in trades["result"]["list"] if trade["side"] == "Buy"
            )
           None


# Функция для анализа данных и отправки сигналов
async def analyze_market_data(client, symbol):
    
    print(f"Запрос данных для {symbol}...")     
    #volume, open_interest, buy_volume, sell_volume = get_market_data(client, symbol)
    #print(f"Данные для {symbol}: volume={volume}, open_interest={open_interest}, buy_volume={buy_volume}, sell_volume={sell_volume}")

    """
    Анализиt, symbol)
        await asyncio.sleep(SLEEP_INTERVAL)  # Задержка между проверками


if __name__ == "__main__":
    asyncio.run(main())
    
bot.polling(non_stop=True)
