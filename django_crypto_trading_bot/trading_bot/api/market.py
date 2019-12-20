from django_crypto_trading_bot.trading_bot.models import Market, Currency
from django_crypto_trading_bot.trading_bot.api.client import get_client
from ccxt.base.exchange import Exchange


def get_or_create_market(response: dict) -> Market:
    """
    update or create a market based on the api json
    """
    base, create = Currency.objects.get_or_create(short=response["base"])
    quote, create = Currency.objects.get_or_create(short=response["quote"])

    try:
        market: Market = Market.objects.get(base=base, quote=quote)
        market.active = response["active"]
        market.precision_amount = response["precision"]["amount"]
        market.precision_price = response["precision"]["price"]
        market.save()
        return market

    except Market.DoesNotExist:
        return Market(
            base=base,
            quote=quote,
            active=response["active"],
            precision_amount=response["precision"]["amount"],
            precision_price=response["precision"]["price"],
        )


def update_market(market: Market) -> Market:
    """
    Update Market Order 
    """
    exchange: Exchange = get_client(exchange_id="binance")
    exchange.load_markets()
    market_exchange: dict = exchange.market(market.symbol)
    return get_or_create_market(market_exchange)