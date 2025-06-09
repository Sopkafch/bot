
from pybit.unified_trading import HTTP

    retu

опытка использовать get_recent_trades
            except AttributeError:
                print(f"Ме"
                return volume, open_interest, None # Возвращаем None для buy/sell, чтобы избежать ошибок дальше
            except Exception as e
                print(f"Ошибка при получении данных о сделках для {symbol} (get_recent_trades): {e}")
                return volume, open_inte
            print(f"Ошибка при получении данных о сделках для {symbol} (get_trades): {e}")
            return volume, open_interest, None

        if trades and trades["result"] and trades["result"]["list"]:
    if volume is None:
    delta = buy_volume - sell
    )

    # *** ИЗМЕНЕНО: Комбинированный сигнал, более агрессивный ***
    if (volume_increase >= VOLUME_INCREASE_THRESHOLD and
      
    previous_volume[symbol] = volume
    i
