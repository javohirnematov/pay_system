from pydantic import BaseModel


# Добавить транзакцию
class CreateTransactionModel(BaseModel):
    card_from: int
    card_to: int
    amount: float


# Изменить транзакцию
class CancelTransferModel(BaseModel):
    card_from: int
    card_to: int
    amount: float
    transfer_id: int
