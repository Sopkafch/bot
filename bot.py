import asyncio
import time
import telebot

from pybit.unified_trading import HTTP

bot_tekegram_api = '7879448301:AAFZOIA6UWt8muc8h9pBOihcR0ERZliO5Vk'
bot = telebot.TeleBot(bot_tekegram_api)
# === НАСТРОЙКИ ===
BYBIT_API_KEY = "MfKJ3spNBt7g5TfKWG"  # Замените на свой API ключ
BYBIT_API_SECRET = "G2JWH9JN2BrMqlxu9nLOJTs0RQXQuEhK5ksy"  # Замените на свой API секрет
SYMBOLS_TO_TRACK = ['AVAUSDT', 'AVAXUSDT', 'AVLUSDT', 'AWEUSDT', 'AXLUSDT', 'AXSUSDT', 'B3USDT', 'BABYUSDT',  'ETHWUSDT', 'FARTCOINUSDT', 'FBUSDT', 'FHEUSDT', 'FIDAUSDT', 'FILUSDT', 'FIOUSDT', 'FLMUSDT', 'FLOCKUSDT', 'FLOWUSDT', 'FLRUSDT', 'FLUXUSDT', 'FORMUSDT', 'FORTHUSDT', 'FTNUSDT', 'FUELUSDT', 'FUSDT', 'FWOGUSDT', 'FXSUSDT', 'GALAUSDT', 'GASUSDT', 'GIGAUSDT', 'GLMRUSDT', 'GLMUSDT', 'GMTUSDT', 'GMXUSDT', 'GNOUSDT', 'GOATUSDT', 'GODSUSDT', 'GOMININGUSDT', 'GORKUSDT', 'GPSUSDT', 'GRASSUSDT', 'GRIFFAINUSDT', 'GRTUSDT', 'GTCUSDT', 'GUNUSDT', 'GUSDT', 'HAEDALUSDT', 'HBARUSDT', 'HEIUSDT', 'HFTUSDT', 'HIFIUSDT', 'HIGHUSDT', 'HIPPOUSDT', 'HIVEUSDT', 'HMSTRUSDT', 'HNTUSDT', 'HOOKUSDT', 'HOTUSDT', 'HPOS10IUSDT', 'HUMAUSDT', 'HYPEPERP', 'HYPERUSDT', 'HYPEUSDT', 'ICPUSDT', 'ICXUSDT', 'IDEXUSDT', 'IDUSDT', 'ILVUSDT', 'IMXUSDT', 'INITUSDT', 'INJUSDT', 'IOSTUSDT', 'IOTAUSDT', 'IOTXUSDT', 'IOUSDT', 'IPUSDT', 'JASMYUSDT', 'JELLYJELLYUSDT', 'JOEUSDT', 'JSTUSDT', 'JTOUSDT', 'JUPUSDT', 'JUSDT', 'KAIAUSDT', 'KAITOUSDT', 'KASUSDT', 'KAVAUSDT', 'KDAUSDT', 'KERNELUSDT', 'KMNOUSDT', 'KNCUSDT', 'KOMAUSDT', 'KSMUSDT', 'L3USDT', 'LAUNCHCOINUSDT', 'LAUSDT', 'LDOUSDT', 'LEVERUSDT', 'LINKPERP', 'LINKUSDT', 'LISTAUSDT', 'LOOKSUSDT', 'LPTUSDT', 'LQTYUSDT', 'LRCUSDT', 'LSKUSDT', 'LTCPERP', 'LTCUSDT', 'LUMIAUSDT', 'LUNA2USDT', 'MAGICUSDT', 'MAJORUSDT', 'MANAUSDT', 'MANTAUSDT', 'MASAUSDT', 'MASKUSDT', 'MAVIAUSDT', 'MAVUSDT', 'MBLUSDT', 'MBOXUSDT', 'MDTUSDT', 'MELANIAUSDT', 'MEMEUSDT', 'MERLUSDT', 'METISUSDT', 'MEUSDT', 'MEWUSDT', 'MICHIUSDT', 'MILKUSDT', 'MINAUSDT', 'MKRUSDT', 'MLNUSDT', 'MNTPERP', 'MNTUSDT', 'MOBILEUSDT', 'MOCAUSDT', 'MOODENGUSDT', 'MORPHOUSDT', 'MOVEUSDT', 'MOVRUSDT', 'MTLUSDT', 'MUBARAKUSDT', 'MVLUSDT', 'MYRIAUSDT', 'MYROUSDT', 'NCUSDT', 'NEARUSDT', 'NEIROETHUSDT', 'NEOUSDT', 'NFPUSDT', 'NILUSDT', 'NKNUSDT', 'NMRUSDT', 'NOTPERP', 'NOTUSDT', 'NSUSDT', 'NTRNUSDT', 'NXPCUSDT', 'OBOLUSDT', 'OBTUSDT', 'OGNUSDT', 'OGUSDT', 'OLUSDT', 'OMNIUSDT', 'OMUSDT', 'ONDOPERP', 'ONDOUSDT', 'ONEUSDT', 'ONGUSDT', 'ONTUSDT', 'OPPERP', 'OPUSDT', 'ORBSUSDT', 'ORCAUSDT', 'ORDERUSDT', 'ORDIPERP', 'ORDIUSDT', 'OSMOUSDT', 'OXTUSDT', 'PARTIUSDT', 'PAXGUSDT', 'PEAQUSDT', 'PENDLEUSDT', 'PENGUUSDT', 'PEOPLEUSDT', 'PERPUSDT', 'PHAUSDT', 'PHBUSDT', 'PIPPINUSDT', 'PIXELUSDT', 'PLUMEUSDT', 'PNUTUSDT', 'POLPERP', 'POLUSDT', 'POLYXUSDT', 'PONKEUSDT', 'POPCATPERP',
'POPCATUSDT', 'PORTALUSDT', 'POWRUSDT', 'PRAIUSDT', 'PRCLUSDT', 'PRIMEUSDT', 'QUICKUSDT', 'RADUSDT', 'RAREUSDT', 'RAYDIUMUSDT', 'RDNTUSDT', 'REDUSDT', 'RENDERUSDT', 'REQUSDT', 'REXUSDT', 'REZUSDT', 'RFCUSDT', 'RIFUSDT', 'RLCUSDT', 'ROAMUSDT', 'RONINUSDT', 'ROSEUSDT', 'RPLUSDT', 'RSRUSDT', 'RSS3USDT', 'RUNEUSDT', 'RVNUSDT', 'SAFEUSDT', 'SAGAUSDT', 'SANDUSDT', 'SAROSUSDT', 'SCAUSDT', 'SCRTUSDT', 'SCRUSDT', 'SCUSDT', 'SDUSDT', 'SEIUSDT', 'SENDUSDT', 'SERAPHUSDT', 'SFPUSDT', 'SHELLUSDT', 'SHIB1000PERP', 'SHIB1000USDT', 'SIGNUSDT', 'SIRENUSDT', 'SKLUSDT', 'SKYAIUSDT', 'SLERFUSDT', 'SLFUSDT', 'SLPUSDT', 'SNTUSDT', 'SNXUSDT', 'SOLAYERUSDT', 'SOLOUSDT', 'SOLPERP', 'SOLUSDT', 'SOLUSDT-06JUN25', 'SOLUSDT-13JUN25', 'SOLUSDT-20JUN25', 'SOLUSDT-27JUN25', 'SOLVUSDT', 'SONICUSDT', 'SOONUSDT', 'SOPHUSDT', 'SPECUSDT', 'SPELLUSDT', 'SPXUSDT', 'SSVUSDT', 'STEEMUSDT', 'STGUSDT', 'STORJUSDT', 'STOUSDT', 'STRKPERP', 'STRKUSDT', 'STXUSDT', 'SUIPERP', 'SUIUSDT', 'SUNDOGUSDT', 'SUNUSDT', 'SUPERUSDT', 'SUSDT', 'SUSHIUSDT', 'SWARMSUSDT', 'SWEATUSDT', 'SWELLUSDT', 'SXPUSDT', 'SXTUSDT', 'SYNUSDT', 'SYRUPUSDT', 'SYSUSDT', 'TAIKOUSDT', 'TAIUSDT', 'TAOUSDT', 'THETAUSDT', 'THEUSDT', 'TIAPERP', 'TIAUSDT', 'TLMUSDT', 'TNSRUSDT', 'TOKENUSDT', 'TONPERP', 'TONUSDT', 'TRBUSDT', 'TRUMPPERP', 'TRUMPUSDT', 'TRUUSDT', 'TRXUSDT', 'TSTBSCUSDT', 'TUSDT', 'TUTUSDT', 'TWTUSDT', 'UMAUSDT', 'UNIPERP', 'UNIUSDT', 'USDCUSDT', 'USDEUSDT', 'USTCUSDT', 'USUALUSDT', 'UXLINKUSDT', 'VANAUSDT', 'VANRYUSDT', 'VELODROMEUSDT', 'VELOUSDT', 'VETUSDT', 'VICUSDT', 'VINEUSDT', 'VIRTUALUSDT', 'VOXELUSDT', 'VRUSDT', 'VTHOUSDT', 'VVVUSDT', 'WALUSDT', 'WAVESUSDT', 'WAXPUSDT', 'WCTUSDT', 'WIFPERP', 'WIFUSDT', 'WLDPERP', 'WLDUSDT', 'WOOUSDT', 'WUSDT', 'XAIUSDT', 'XAUTUSDT', 'XCHUSDT', 'XCNUSDT', 'XDCUSDT', 'XEMUSDT', 'XIONUSDT', 'XLMPERP', 'XLMUSDT', 'XMRUSDT', 'XNOUSDT', 'XRDUSDT', 'XRPPERP', 'XRPUSDT', 'XTERUSDT', 'XTZUSDT', 'XVGUSDT', 'XVSUSDT', 'YFIUSDT', 'YGGUSDT', 'ZBCNUSDT', 'ZECUSDT', 'ZENTUSDT', 'ZENUSDT', 'ZEREBROUSDT', 'ZETAUSDT', 'ZEUSUSDT', 'ZILUSDT', 'ZKJUSDT', 'ZKUSDT', 'ZORAUSDT', 'ZRCUSDT', 'ZROUSDT', 'ZRXUSDT']  # Список пар для отслеживания
VOLUME_INCREASE_THRESHOLD = 2.5  # Порог увеличения объема (в разах)
OI_INCREASE_THRESHOLD = 1.5  # Порог увеличения открытого интереса (в разах)
DELTA_THRESHOLD = 5000000  # Порог дельты между покупками и продажами
MARKET = "linear"  # Тип рынка: "spot", "linear", "inverse"
SLEEP_INTERVAL = 600  # Интервал между проверками в секундах
# === КОНЕЦ НАСТРОЕК ===


# Глобальные переменные для хранения предыдущих значений
previous_volume = {}
previous_open_interest = {}

# Функция для инициализации API клиента
def initialize_client():
    """
    Инициализирует API клиент для Unified Trading API.
    """
    client = HTTP(
        testnet=False,  # Измените на True для тестовой сети
        api_key=BYBIT_API_KEY,
        api_secret=BYBIT_API_SECRET,
    )
    return client


# Функция для получения данных о рынке

def get_market_data(client, symbol):
    """
    Получает данные о рынке (объем, открытый интерес, данные о сделках)
    используя Unified Trading API.
    """
    try:
        # Получаем данные о последних сделках (trades)
        trades = client.get_public_trade_history(category=MARKET, symbol=symbol, limit=200)

        if trades and trades["retCode"] == 0 and trades["result"]["list"]:
            buy_volume = sum(
                float(trade["size"]) for trade in trades["result"]["list"] if trade["side"] == "Buy"
            )
            sell_volume = sum(
                float(trade["size"])
                for trade in trades["result"]["list"]
                if trade["side"] == "Sell"
            )
        else:
            print(f"Ошибка при получении данных о сделках для {symbol}: {trades}")
            return None, None, None, None
        # Получаем данные ticker (объем за 24 часа)
        ticker = client.get_tickers(category=MARKET, symbol=symbol)
        if ticker and ticker["retCode"] == 0 and ticker["result"]["list"]:
            volume = float(ticker["result"]["list"][0]["volume24h"])
        else:
            print(f"Ошибка при получении данных ticker для {symbol}: {ticker}")
            return None, None, None, None
        # Получаем открытый интерес (только для деривативов)
        if MARKET != "spot":
            open_interest_data = client.get_open_interest(category=MARKET, symbol=symbol, intervalTime='1h') # изза этого может не получать данные о открытом инересе
            if open_interest_data and open_interest_data["retCode"] == 0 and open_interest_data["result"]["list"]:
                open_interest = float(open_interest_data["result"]["list"][0]["openInterest"])
            else:
                print(f"Ошибка при получении открытого интереса для {symbol}: {open_interest_data}")
                open_interest = None  # Важно установить в None если ошибка
        else:
            open_interest = None

        return volume, open_interest, buy_volume, sell_volume
    except Exception as e:
        print(f"Ошибка при получении данных для {symbol}: {e}")
        return None, None, None, None


# Функция для анализа данных и отправки сигналов
async def analyze_market_data(client, symbol):
    
    print(f"Запрос данных для {symbol}...")     
    #volume, open_interest, buy_volume, sell_volume = get_market_data(client, symbol)
    #print(f"Данные для {symbol}: volume={volume}, open_interest={open_interest}, buy_volume={buy_volume}, sell_volume={sell_volume}")

    """
    Анализирует рыночные данные и отправляет сигналы при выполнении условий.
    """
    volume, open_interest, buy_volume, sell_volume = get_market_data(client, symbol)

    if volume is None:  # Проверяем, что volume не None
        return

    delta = buy_volume - sell_volume if buy_volume is not None and sell_volume is not None else 0

    # Инициализация предыдущих значений, если их нет
    if symbol not in previous_volume:
        previous_volume[symbol] = volume
    if open_interest is not None and symbol not in previous_open_interest:
        previous_open_interest[symbol] = open_interest

    # Проверка условий
    volume_increase = volume / previous_volume[symbol] if previous_volume[symbol] != 0 else 0

    oi_increase = (
        open_interest / previous_open_interest[symbol]
        if open_interest is not None and previous_open_interest.get(symbol, 0) != 0
        else 0
    )

    if volume_increase >= VOLUME_INCREASE_THRESHOLD:
        
       bot.send_message(chat_id=1408997023, text= f"СИГНАЛ: {symbol} - Увеличение объема в {volume_increase:.2f} раза!")  


    if open_interest is not None and oi_increase >= OI_INCREASE_THRESHOLD:

        bot.send_message(chat_id=1408997023, text=f"СИГНАЛ: {symbol} - Увеличение открытого интереса в {oi_increase:.2f} раза!")


    if buy_volume is not None and sell_volume is not None and delta > DELTA_THRESHOLD:
        
        bot.send_message(chat_id=1408997023, text=f"СИГНАЛ: {symbol} - Положительная дельта (покупки > продажи): {delta:.2f}")

    # Обновляем предыдущие значения
    previous_volume[symbol] = volume
    if open_interest is not None:
        previous_open_interest[symbol] = open_interest


# Основная функция
async def main():
    """
    Основная функция для запуска анализа рынка.
    """
    client = initialize_client()

    #tickers = client.get_tickers(category="linear")
    #print([item["symbol"] for item in tickers["result"]["list"]])

    while True:
        for symbol in SYMBOLS_TO_TRACK:
            await analyze_market_data(client, symbol)
        await asyncio.sleep(SLEEP_INTERVAL)  # Задержка между проверками


if __name__ == "__main__":
    asyncio.run(main())
    
bot.polling(non_stop=True)