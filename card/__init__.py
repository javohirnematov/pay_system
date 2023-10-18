from pydantic import BaseModel


# Класс для валидации добавления карт
class CardAddModel(BaseModel):
    user_id: int
    card_number: int
    balance: float
    card_name: str
    cvv: int
    exp_date: int


# Класс для валидации изменения дизайна карты
class EditCardModel(BaseModel):
    card_id: int
    design_path: str
