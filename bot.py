import asyncio
import time
import telebot

from pybit.unified_trading import HTTP

bot_tekegram_api = '7879448301:AAFZOIA6UWt8muc8h9pBOihcR0ERZliO5Vk'
bot = telebot.TeleBot(bot_tekegram_api)

# === НАСТРОЙКИ ===
BYBIT_API_KEY = "MfKJ3spNBt7g5TfKWG"
BYBIT_API_SECRET = "G2JWH9JN2BrMqlxu9nLOJTs0RQXQuEhK5ksy"
SYMBOLS_TO_TRACK = ['AGLDUSDT', 'AGTUSDT', 'AI16ZUSDT', 'AIOZUSDT', 'AIUSDT', 'AIXBTUSDT', 'AKTUSDT', 'ALCHUSDT', 'ALEOUSDT', 'ALGOUSDT', 'ALICEUSDT', 'ALPHAUSDT', 'ALTUSDT', 'AVAAIUSDT', 'AVAILUSDT', 'AVAUSDT', 'AVAXUSDT', 'AVLUSDT', 'AWEUSDT', 'AXLUSDT', 'AXSUSDT', 'B3USDT', 'BABYUSDT', 'BADGERUSDT', 'BAKEUSDT', 'BALUSDT', 'BANANAS31USDT', 'BANANAUSDT', 'BANDUSDT', 'BANKUSDT', 'BANUSDT', 'BATUSDT', 'BBUSDT', 'BCHPERP', 'BCHUSDT', 'BDXNUSDT', 'BEAMUSDT', 'BELUSDT', 'BERAUSDT', 'BICOUSDT', 'BIGTIMEUSDT', 'BIOUSDT', 'BLASTUSDT', 'BLURUSDT', 'BMTUSDT', 'BNBPERP', 'BNBUSDT', 'BNTUSDT', 'BOBAUSDT', 'BOMEUSDT', 'BRETTUSDT', 'BROCCOLIUSDT', 'BRUSDT', 'BSVUSDT', 'BSWUSDT',  'COOKIEUSDT', 'COOKUSDT', 'COREUSDT', 'COSUSDT', 'COTIUSDT', 'COWUSDT', 'CPOOLUSDT', 'CROUSDT', 'CRVPERP', 'DEXEUSDT', 'DGBUSDT', 'DODOUSDT', 'DOGEPERP', 'DOGEUSDT', 'DOGSUSDT', 'DOGUSDT', 'DOODUSDT', 'DOTPERP', 'DOTUSDT', 'DRIFTUSDT', 'DUCKUSDT', 'DUSKUSDT', 'DYDXUSDT', 'DYMUSDT', 'EDUUSDT', 'EGLDUSDT', 'EIGENUSDT', 'ELXUSDT', 'ENAPERP', 'ENAUSDT', 'ENJUSDT', 'ENSUSDT', 'EPICUSDT', 'EPTUSDT', 'ETCPERP', 'ETCUSDT', 'ETH-26DEC25', 'ETH-26SEP25', 'ETH-27JUN25', 'ETHBTCUSDT', 'ETHFIPERP', 'ETHFIUSDT', 'ETHPERP', 'ETHUSDT', 'ETHUSDT-13JUN25', 'ETHUSDT-20JUN25', 'ETHUSDT-25JUL25', 'ETHUSDT-26DEC25', 'ETHUSDT-26SEP25', 'ETHUSDT-27JUN25', 'ETHUSDT-27MAR26', 'ETHUSDT-29AUG25', 'ETHWUSDT', 'FARTCOINUSDT', 'FBUSDT', 'FHEUSDT', 'FIDAUSDT', 'FILUSDT', 'FIOUSDT', 'FLMUSDT', 'FLOCKUSDT', 'FLOWUSDT', 'FLRUSDT', 'FLUXUSDT', 'FORMUSDT', 'FORTHUSDT', 'FTNUSDT', 'FUELUSDT', 'FUSDT', 'GODSUSDT', 'GORKUSDT', 'GPSUSDT', 'GRASSUSDT', 'GRIFFAINUSDT', 'GRTUSDT', 'GTCUSDT', 'GUNUSDT', 'GUSDT', 'HAEDALUSDT', 'HBARUSDT', 'HEIUSDT', 'HFTUSDT', 'HIFIUSDT', 'HIGHUSDT', 'HIPPOUSDT', 'HIVEUSDT', 'HMSTRUSDT', 'HNTUSDT', 'HOOKUSDT', 'HOTUSDT', 'HPOS10IUSDT', 'HUMAUSDT', 'HYPEPERP', 'HYPERUSDT', 'HYPEUSDT', 'ICPUSDT', 'ICXUSDT', 'IDEXUSDT', 'IDUSDT', 'ILVUSDT', 'IMXUSDT', 'INITUSDT', 'INJUSDT', 'IOSTUSDT', 'IOTAUSDT', 'IOTXUSDT', 'IOUSDT', 'IPUSDT', 'JASMYUSDT', 'JELLYJELLYUSDT', 'JOEUSDT', 'JSTUSDT', 'JTOUSDT', 'JUPUSDT', 'JUSDT', 'KAIAUSDT', 'KAITOUSDT', 'KASUSDT', 'KAVAUSDT', 'KDAUSDT', 'KERNELUSDT', 'LEVERUSDT', 'LINKPERP', 'LINKUSDT', 'LISTAUSDT', 'LOOKSUSDT', 'LPTUSDT', 'LQTYUSDT', 'LRCUSDT', 'LSKUSDT', 'LTCPERP', 'LTCUSDT', 'LUMIAUSDT', 'LUNA2USDT', 'MAGICUSDT', 'MAJORUSDT', 'MANAUSDT', 'MANTAUSDT', 'MASAUSDT', 'MASKUSDT', 'MAVIAUSDT', 'MAVUSDT', 'MBLUSDT', 'MBOXUSDT', 'MDTUSDT', 'MELANIAUSDT', 'MEMEUSDT', 'MERLUSDT', 'METISUSDT', 'MEUSDT', 'MEWUSDT', 'MICHIUSDT', 'MILKUSDT', 'MINAUSDT', 'MKRUSDT', 'MLNUSDT', 'MNTPERP', 'MNTUSDT', 'MOBILEUSDT', 'MOCAUSDT', 'MOODENGUSDT', 'MORPHOUSDT', 'MOVEUSDT', 'MOVRUSDT', 'MTLUSDT', 'MUBARAKUSDT', 'MVLUSDT', 'MYRIAUSDT', 'MYROUSDT', 'NCUSDT', 'NEARUSDT', 'NEIROETHUSDT', 'NEOUSDT', 'NFPUSDT', 'NILUSDT', 'NKNUSDT', 'NMRUSDT', 'NOTPERP', 'ONDOPERP', 'ONDOUSDT', 'ONEUSDT', 'ONGUSDT', 'ONTUSDT', 'OPPERP', 'OPUSDT', 'ORBSUSDT', 'ORCAUSDT', 'ORDERUSDT', 'ORDIPERP', 'ORDIUSDT', 'OSMOUSDT', 'OXTUSDT', 'PARTIUSDT', 'PAXGUSDT', 'PEAQUSDT', 'PENDLEUSDT', 'PENGUUSDT', 'PEOPLEUSDT', 'PERPUSDT', 'PHAUSDT', 'PHBUSDT', 'PIPPINUSDT', 'PIXELUSDT', 'PLUMEUSDT', 'PNUTUSDT', 'POLPERP', 'POLUSDT', 'POLYXUSDT', 'PONKEUSDT', 'POPCATPERP', 'POPCATUSDT', 'PORTALUSDT', 'POWRUSDT', 'PRAIUSDT', 'PRCLUSDT', 'PRIMEUSDT', 'PROMPTUSDT', 'PROMUSDT', 'PUFFERUSDT', 'PUMPBTCUSDT', 'PUNDIXUSDT', 'PYRUSDT', 'PYTHUSDT', 'QIUSDT', 'QNTUSDT', 'QTUMUSDT', 'QUICKUSDT', 'RADUSDT', 'RAREUSDT', 'RAYDIUMUSDT', 'RDNTUSDT', 'REDUSDT', 'RENDERUSDT', 'REQUSDT', 'REXUSDT', 'REZUSDT', 'RFCUSDT', 'RIFUSDT', 'RLCUSDT', 'ROAMUSDT', 'RONINUSDT', 'ROSEUSDT', 'RPLUSDT', 'RSRUSDT', 'RSS3USDT', 'RUNEUSDT', 'RVNUSDT', 'SAFEUSDT', 'SAGAUSDT', 'SANDUSDT', 'SAROSUSDT', 'SCAUSDT', 'SCRTUSDT', 'SCRUSDT', 'SCUSDT', 'SDUSDT', 'SEIUSDT', 'SENDUSDT', 'SERAPHUSDT', 'SFPUSDT', 'SHELLUSDT', 'SHIB1000PERP', 'SHIB1000USDT', 'SIGNUSDT', 'SIRENUSDT', 'SKLUSDT', 'SKYAIUSDT', 'SLERFUSDT', 'SLFUSDT', 'SLPUSDT', 'SNTUSDT', 'SNXUSDT', 'SOLAYERUSDT', 'SOLOUSDT', 'SOLPERP', 'SOLUSDT', 'SPELLUSDT', 'SPXUSDT', 'SSVUSDT', 'STEEMUSDT', 'STGUSDT', 'STORJUSDT', 'STOUSDT', 'STRKPERP', 'STRKUSDT', 'STXUSDT', 'SUIPERP', 'SUIUSDT', 'SUNDOGUSDT', 'SUNUSDT', 'SUPERUSDT', 'SUSDT', 'SUSHIUSDT', 'SWARMSUSDT', 'SWEATUSDT', 'SWELLUSDT', 'SXPUSDT', 'SXTUSDT', 'SYNUSDT', 'SYRUPUSDT']  # Пример, можно добавить больше монет
VOLUME_INCREASE_THRESHOLD = 2.5  # Снижаем, чтобы быть более чувствительными к росту
PRICE_INCREASE_THRESHOLD = 0.005  # Снижаем до 0.5% за час, чтобы ловить более ранние сигналы
OI_INCREASE_THRESHOLD = 2  #  Оставляем умеренным
DELTA_THRESHOLD = 2000000  # Снижаем порог дельты
MARKET = "linear"
SLEEP_INTERVAL = 936  # Проверяем каждую минуту
OPEN_INTEREST_INTERVAL = '1h'  # Явно указываем интервал для OI
# === КОНЕЦ НАСТРОЕК ===

previous_volume = {}
previous_price = {}
previous_open_interest = {}

def initialize_client():
    client = HTTP(
        testnet=False,
        api_key=BYBIT_API_KEY,
        api_secret=BYBIT_API_SECRET,
    )
    return client

def get_market_data(client, symbol):
    try:
        # Данные о сделках (убрал, т.к. они не так важны для почасового анализа)
        # trades = client.get_public_trade_history(category=MARKET, symbol=symbol, limit=200)
        # buy_volume = ...  # Удаляем код, связанный с trades

        ticker = client.get_tickers(category=MARKET, symbol=symbol)
        if ticker and ticker["retCode"] == 0 and ticker["result"]["list"]:
            volume = float(ticker["result"]["list"][0]["volume24h"])
            last_price = float(ticker["result"]["list"][0]["lastPrice"])
            # high_price = float(ticker["result"]["list"][0]["high"])  # Добавил high price
            # low_price = float(ticker["result"]["list"][0]["low"])  # Добавил low price
        else:
            print(f"Ошибка при получении данных ticker для {symbol}: {ticker}")
            return None, None, None, None, None # Убрал лишнее None

        if MARKET != "spot":
            open_interest_data = client.get_open_interest(category=MARKET, symbol=symbol, intervalTime=OPEN_INTEREST_INTERVAL)
            if open_interest_data and open_interest_data["retCode"] == 0 and open_interest_data["result"]["list"]:
                open_interest = float(open_interest_data["result"]["list"][0]["openInterest"])
            else:
                print(f"Ошибка при получении открытого интереса для {symbol}: {open_interest_data}")
                open_interest = None
        else:
            open_interest = None

        return volume, open_interest, None, None, last_price # Убрал лишнее возвращаемое значение
    except Exception as e:
        print(f"Ошибка при получении данных для {symbol}: {e}")
        return None, None, None, None, None # Убрал лишнее None

async def analyze_market_data(client, symbol):
    volume, open_interest, buy_volume, sell_volume, last_price = get_market_data(client, symbol)

    if volume is None:
        return

    # delta = buy_volume - sell_volume if buy_volume is not None and sell_volume is not None else 0 #  Удалил, т.к. больше не получаем buy_volume/sell_volume

    # Инициализация при первом запуске
    if symbol not in previous_volume:
        previous_volume[symbol] = volume
    if symbol not in previous_price:
        previous_price[symbol] = last_price
    if open_interest is not None and symbol not in previous_open_interest:
        previous_open_interest[symbol] = open_interest

    volume_increase = volume / previous_volume[symbol] if previous_volume[symbol] != 0 else 0
    price_increase = (last_price - previous_price[symbol]) / previous_price[symbol] if previous_price[symbol] != 0 else 0

    oi_increase = (
        open_interest / previous_open_interest[symbol]
        if open_interest is not None and previous_open_interest.get(symbol, 0) != 0
        else 0
    )

    # *** ИЗМЕНЕНО: Комбинированный сигнал, более агрессивный ***
    if (volume_increase >= VOLUME_INCREASE_THRESHOLD and
        price_increase >= PRICE_INCREASE_THRESHOLD and
        oi_increase >= OI_INCREASE_THRESHOLD): # Убрал delta, добавил OI
        bot.send_message(chat_id=1408997023,
                         text=f"ВОЗМОЖНЫЙ ПАМП: {symbol} - Резкий рост объема ({volume_increase:.2f}x), "
                              f"цена выросла на {price_increase:.2f}%, "
                              f"OI вырос на {oi_increase:.2f}") # Изменил сообщение

    previous_volume[symbol] = volume
    previous_price[symbol] = last_price
    if open_interest is not None:
        previous_open_interest[symbol] = open_interest

    print('оБЪЕМ: ', volume_increase, 'OI: ', oi_increase,'|', open_interest, '-', previous_open_interest[symbol])
    print('-----------------------------------------------------------')

async def main():
    client = initialize_client()
    while True:
        for symbol in SYMBOLS_TO_TRACK:
            await analyze_market_data(client, symbol)
        print(f"Ждем {SLEEP_INTERVAL} секунд до следующей проверки...")
        await asyncio.sleep(SLEEP_INTERVAL)

if __name__ == "__main__":
    asyncio.run(main())
