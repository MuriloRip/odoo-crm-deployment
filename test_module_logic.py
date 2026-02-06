
# Simulação da lógica do Odoo para validar os cálculos
class MockPartner:
    def __init__(self):
        self.non_client_transaction_ids = []
        self.total_gains = 0
        self.total_costs = 0
        self.balance = 0

    def _compute_transactions_totals(self):
        gains = sum(t.amount for t in self.non_client_transaction_ids if t.transaction_type == 'gain')
        costs = sum(t.amount for t in self.non_client_transaction_ids if t.transaction_type == 'cost')
        self.total_gains = gains
        self.total_costs = costs
        self.balance = gains - costs

class MockTransaction:
    def __init__(self, amount, transaction_type):
        self.amount = amount
        self.transaction_type = transaction_type

# Teste
partner = MockPartner()
partner.non_client_transaction_ids.append(MockTransaction(1000, 'gain')) # Venda sofá
partner.non_client_transaction_ids.append(MockTransaction(200, 'cost'))  # Entrega sofá
partner._compute_transactions_totals()

print(f"Ganhos: {partner.total_gains}")
print(f"Custos: {partner.total_costs}")
print(f"Saldo: {partner.balance}")

assert partner.total_gains == 1000
assert partner.total_costs == 200
assert partner.balance == 800
print("Lógica de cálculo validada com sucesso!")
