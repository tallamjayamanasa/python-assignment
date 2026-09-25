class DebitCard:
    def pay(self): print("Debit card payment")
class CreditCard:
    def pay(self): print("Credit card payment")
def card_payment(card): card.pay()
for x in [DebitCard(), CreditCard()]: card_payment(x)
