import asyncio
import time
import telebot

from pybit.unified_trading import HTTP

bot_tekegram_api = '7879448301:AAFZOIA6UWt8muc8h9pBOihcR0ERZliO5Vk'
bot = telebot.TeleBot(bot_tekegram_api)

# === НАСТРОЙКИ ===
BYBIT_API_KEY = "MfKJ3spNBt7g5TfKWG"
BYBIT_API_SECRET = "G2JWH9JN2BrMqlxu9nLOJTs0RQXQuEhK5ksy"
SYMBOLS_TO_TRACK =['AGLDUSDT', 'AGTUSDT', 'AI16ZUSDT', 'AIOZUSDT', 'AIUSDT', 'AIXBTUSDT', 'AKTUSDT', 'ALCHUSDT', 'ALEOUSDT', 'ALGOUSDT', 'ALICEUSDT', 'ALPHAUSDT', 'ALTUSDT', 'AVAAIUSDT', 'AVAILUSDT', 'AVAUSDT', 'AVAXUSDT', 'AVLUSDT', 'AWEUSDT', 'AXLUSDT', 'AXSUSDT', 'B3USDT', 'BABYUSDT', 'BADGERUSDT', 'BAKEUSDT', 'BALUSDT', 'BANANAS31USDT', 'BANANAUSDT', 'BANDUSDT', 'BANKUSDT', 'BANUSDT', 'BATUSDT', 'BBUSDT', 'BCHPERP', 'BCHUSDT', 'BDXNUSDT', 'BEAMUSDT', 'BELUSDT', 'BERAUSDT', 'BICOUSDT', 'BIGTIMEUSDT', 'BIOUSDT', 'BLASTUSDT', 'BLURUSDT', 'BMTUSDT', 'BNBPERP', 'BNBUSDT', 'BNTUSDT', 'BOBAUSDT', 'BOMEUSDT', 'BRETTUSDT', 'BROCCOLIUSDT', 'BRUSDT', 'BSVUSDT', 'BSWUSDT',  'COOKIEUSDT', 'COOKUSDT', 'COREUSDT', 'COSUSDT', 'COTIUSDT', 'COWUSDT', 'CPOOLUSDT', 'CROUSDT', 'CRVPERP', 'DEXEUSDT', 'DGBUSDT', 'DODOUSDT', 'DOGEPERP', 'DOGEUSDT', 'DOGSUSDT', 'DOGUSDT', 'DOODUSDT', 'DOTPERP', 'DOTUSDT', 'DRIFTUSDT', 'DUCKUSDT', 'DUSKUSDT', 'DYDXUSDT', 'DYMUSDT', 'EDUUSDT', 'EGLDUSDT', 'EIGENUSDT', 'ELXUSDT', 'ENAPERP', 'ENAUSDT', 'ENJUSDT', 'ENSUSDT', 'EPICUSDT', 'EPTUSDT', 'ETCPERP', 'ETCUSDT', 'ETH-26DEC25', 'ETH-26SEP25', 'ETH-27JUN25', 'ETHBTCUSDT', 'ETHFIPERP', 'ETHFIUSDT', 'ETHPERP', 'ETHUSDT', 'ETHUSDT-13JUN25', 'ETHUSDT-20JUN25', 'ETHUSDT-25JUL25', 'ETHUSDT-26DEC25', 'ETHUSDT-26SEP25', 'ETHUSDT-27JUN25', 'ETHUSDT-27MAR26', 'ETHUSDT-29AUG25', 'ETHWUSDT', 'FARTCOINUSDT', 'FBUSDT', 'FHEUSDT', 'FIDAUSDT', 'FILUSDT', 'FIOUSDT', 'FLMUSDT', 'FLOCKUSDT', 'FLOWUSDT', 'FLRUSDT', 'FLUXUSDT', 'FORMUSDT', 'FORTHUSDT', 'FTNUSDT', 'FUELUSDT', 'FUSDT', 'GODSUSDT', 'GORKUSDT', 'GPSUSDT', 'GRASSUSDT', 'GRIFFAINUSDT', 'GRTUSDT', 'GTCUSDT', 'GUNUSDT', 'GUSDT', 'HAEDALUSDT', 'HBARUSDT', 'HEIUSDT', 'HFTUSDT', 'HIFIUSDT', 'HIGHUSDT', 'HIPPOUSDT', 'HIVEUSDT', 'HMSTRUSDT', 'HNTUSDT', 'HOOKUSDT', 'HOTUSDT', 'HPOS10IUSDT', 'HUMAUSDT', 'HYPEPERP', 'HYPERUSDT', 'HYPEUSDT', 'ICPUSDT', 'ICXUSDT', 'IDEXUSDT', 'IDUSDT', 'ILVUSDT', 'IMXUSDT', 'INITUSDT', 'INJUSDT', 'IOSTUSDT', 'IOTAUSDT', 'IOTXUSDT', 'IOUSDT', 'IPUSDT', 'JASMYUSDT', 'JELLYJELLYUSDT', 'JOEUSDT', 'JSTUSDT', 'JTOUSDT', 'JUPUSDT', 'JUSDT', 'KAIAUSDT', 'KAITOUSDT', 'KASUSDT', 'KAVAUSDT', 'KDAUSDT', 'KERNELUSDT', 'LEVERUSDT', 'LINKPERP', 'LINKUSDT', 'LISTAUSDT', 'LOOKSUSDT', 'LPTUSDT', 'LQTYUSDT', 'LRCUSDT', 'LSKUSDT', 'LTCPERP', 'LTCUSDT', 'LUMIAUSDT', 'LUNA2USDT', 'MAGICUSDT', 'MAJORUSDT', 'MANAUSDT', 'MANTAUSDT', 'MASAUSDT', 'MASKUSDT', 'MAVIAUSDT', 'MAVUSDT', 'MBLUSDT', 'MBOXUSDT', 'MDTUSDT', 'MELANIAUSDT', 'MEMEUSDT', 'MERLUSDT', 'METISUSDT', 'MEUSDT', 'MEWUSDT', 'MICHIUSDT', 'MILKUSDT', 'MINAUSDT', 'MKRUSDT', 'MLNUSDT', 'MNTPERP', 'MNTUSDT', 'MOBILEUSDT', 'MOCAUSDT', 'MOODENGUSDT', 'MORPHOUSDT', 'MOVEUSDT', 'MOVRUSDT', 'MTLUSDT', 'MUBARAKUSDT', 'MVLUSDT', 'MYRIAUSDT', 'MYROUSDT', 'NCUSDT', 'NEARUSDT', 'NEIROETHUSDT', 'NEOUSDT', 'NFPUSDT', 'NILUSDT', 'NKNUSDT', 'NMRUSDT', 'NOTPERP', 'ONDOPERP', 'ONDOUSDT', 'ONEUSDT', 'ONGUSDT', 'ONTUSDT', 'OPPERP', 'OPUSDT', 'ORBSUSDT', 'ORCAUSDT', 'ORDERUSDT', 'ORDIPERP', 'ORDIUSDT', 'OSMOUSDT', 'OXTUSDT', 'PARTIUSDT', 'PAXGUSDT', 'PEAQUSDT', 'PENDLEUSDT', 'PENGUUSDT', 'PEOPLEUSDT', 'PERPUSDT', 'PHAUSDT', 'PHBUSDT', 'PIPPINUSDT', 'PIXELUSDT', 'PLUMEUSDT', 'PNUTUSDT', 'POLPERP', 'POLUSDT', 'POLYXUSDT', 'PONKEUSDT', 'POPCATPERP', 'POPCATUSDT', 'PORTALUSDT', 'POWRUSDT', 'PRAIUSDT', 'PRCLUSDT', 'PRIMEUSDT', 'PROMPTUSDT', 'PROMUSDT', 'PUFFERUSDT', 'PUMPBTCUSDT', 'PUNDIXUSDT', 'PYRUSDT', 'PYTHUSDT', 'QIUSDT', 'QNTUSDT', 'QTUMUSDT', 'QUICKUSDT', 'RADUSDT', 'RAREUSDT', 'RAYDIUMUSDT', 'RDNTUSDT', 'REDUSDT', 'RENDERUSDT', 'REQUSDT', 'REXUSDT', 'REZUSDT', 'RFCUSDT', 'RIFUSDT', 'RLCUSDT', 'ROAMUSDT', 'RONINUSDT', 'ROSEUSDT', 'RPLUSDT', 'RSRUSDT', 'RSS3USDT', 'RUNEUSDT', 'RVNUSDT', 'SAFEUSDT', 'SAGAUSDT', 'SANDUSDT', 'SAROSUSDT', 'SCAUSDT', 'SCRTUSDT', 'SCRUSDT', 'SCUSDT', 'SDUSDT', 'SEIUSDT', 'SENDUSDT', 'SERAPHUSDT', 'SFPUSDT', 'SHELLUSDT', 'SHIB1000PERP', 'SHIB1000USDT', 'SIGNUSDT', 'SIRENUSDT', 'SKLUSDT', 'SKYAIUSDT', 'SLERFUSDT', 'SLFUSDT', 'SLPUSDT', 'SNTUSDT', 'SNXUSDT', 'SOLAYERUSDT', 'SOLOUSDT', 'SOLPERP', 'SOLUSDT', 'SPELLUSDT', 'SPXUSDT', 'SSVUSDT', 'STEEMUSDT', 'STGUSDT', 'STORJUSDT', 'STOUSDT', 'STRKPERP', 'STRKUSDT', 'STXUSDT', 'SUIPERP', 'SUIUSDT', 'SUNDOGUSDT', 'SUNUSDT', 'SUPERUSDT', 'SUSDT', 'SUSHIUSDT', 'SWARMSUSDT', 'SWEATUSDT', 'SWELLUSDT', 'SXPUSDT', 'SXTUSDT', 'SYNUSDT', 'SYRUPUSDT']
MARKET = "linear"
SLEEP_INTERVAL = 60  # Проверяем секунды
COMPARE_INTERVAL = 120  # Сравниваем цены (в секундах)
PRICE_INCREASE_THRESHOLD = 0.02
# === КОНЕЦ НАСТРОЕК ===

previous_price = {}
last_compared = {}  # Время последнего сравнения для каждого символа


def initialize_client():
    client = HTTP(
        testnet=False,
        api_key=BYBIT_API_KEY,
        api_secret=BYBIT_API_SECRET,
    )
    return client

def get_market_data(client, symbol):
    try:
        ticker = client.get_tickers(category=MARKET, symbol=symbol)
        if ticker and ticker["retCode"] == 0 and ticker["result"]["list"]:
            last_price = float(ticker["result"]["list"][0]["lastPrice"])
        else:
            print(f"Ошибка при получении данных ticker для {symbol}: {ticker}")
            return None

        return last_price

    except Exception as e:
        print(f"Ошибка при получении данных для {symbol}: {e}")
        return None

async def analyze_price_movement(client, symbol):
    print(f'Анализ данных: {symbol}')
    now = time.time()

    last_price = get_market_data(client, symbol)

    if last_price is None:
        return

    if symbol not in previous_price:
        previous_price[symbol] = last_price
        last_compared[symbol] = now
        return  # Нет данных для сравнения в первый запуск

    time_since_last_compare = now - last_compared[symbol]

    if time_since_last_compare >= COMPARE_INTERVAL:
        # Сравниваем цену с ценой, которая была час назад
        price_increase = (last_price - previous_price[symbol]) / previous_price[symbol]

        if price_increase >= PRICE_INCREASE_THRESHOLD:
            bot.send_message(chat_id=1408997023,
                             text=f"📈 Монета: {symbol}: 🚀 Цена выросла на {price_increase:.2f}% | ⏳ за {COMPARE_INTERVAL // 60} минут!")
        # Обновляем значения для следующего сравнения
        previous_price[symbol] = last_price
        last_compared[symbol] = now
    else:
        # Если еще не прошло COMPARE_INTERVAL секунд, просто обновляем last_price
        previous_price[symbol] = last_price


async def main():
    client = initialize_client()
    while True:
        for symbol in SYMBOLS_TO_TRACK:
            await analyze_price_movement(client, symbol)
        print(f"Ждем {SLEEP_INTERVAL} секунд до следующей проверки...")
        await asyncio.sleep(SLEEP_INTERVAL)


if __name__ == "__main__":
    asyncio.run(main())
