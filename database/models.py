from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, declared_attr
from typing import Any


class Base(DeclarativeBase):
    id: Any
    __name__: str

    __allow_unmapped__ = True

    @declared_attr
    def __tablename__(self) -> str:
        return self.__name__.lower()


class Clients(Base):
    __tablename__ = "Clients"

    id: Mapped[int] = mapped_column(primary_key=True)
    rn: Mapped[int]
    pre_since_opened: Mapped[int]
    pre_since_confirmed: Mapped[int]
    pre_pterm: Mapped[int]
    pre_fterm: Mapped[int]
    pre_till_pclose: Mapped[int]
    pre_till_fclose: Mapped[int]
    pre_loans_credit_limit: Mapped[int]
    pre_loans_next_pay_summ: Mapped[int]
    pre_loans_outstanding: Mapped[int]
    pre_loans_total_overdue: Mapped[int]
    pre_loans_max_overdue_sum: Mapped[int]
    pre_loans_credit_cost_rate: Mapped[int]
    pre_loans5: Mapped[int]
    pre_loans530: Mapped[int]
    pre_loans3060: Mapped[int]
    pre_loans6090: Mapped[int]
    pre_loans90: Mapped[int]
    is_zero_loans5: Mapped[int]
    is_zero_loans530: Mapped[int]
    is_zero_loans3060: Mapped[int]
    is_zero_loans6090: Mapped[int]
    is_zero_loans90: Mapped[int]
    pre_util: Mapped[int]
    pre_over2limit: Mapped[int]
    pre_maxover2limit: Mapped[int]
    is_zero_util: Mapped[int]
    is_zero_over2limit: Mapped[int]
    is_zero_maxover2limit: Mapped[int]
    enc_paym_0: Mapped[int]
    enc_paym_1: Mapped[int]
    enc_paym_2: Mapped[int]
    enc_paym_3: Mapped[int]
    enc_paym_4: Mapped[int]
    enc_paym_5: Mapped[int]
    enc_paym_6: Mapped[int]
    enc_paym_7: Mapped[int]
    enc_paym_8: Mapped[int]
    enc_paym_9: Mapped[int]
    enc_paym_10: Mapped[int]
    enc_paym_11: Mapped[int]
    enc_paym_12: Mapped[int]
    enc_paym_13: Mapped[int]
    enc_paym_14: Mapped[int]
    enc_paym_15: Mapped[int]
    enc_paym_16: Mapped[int]
    enc_paym_17: Mapped[int]
    enc_paym_18: Mapped[int]
    enc_paym_19: Mapped[int]
    enc_paym_20: Mapped[int]
    enc_paym_21: Mapped[int]
    enc_paym_22: Mapped[int]
    enc_paym_23: Mapped[int]
    enc_paym_24: Mapped[int]
    enc_loans_account_holder_type: Mapped[int]
    enc_loans_credit_status: Mapped[int]
    enc_loans_credit_type: Mapped[int]
    enc_loans_account_cur: Mapped[int]
    pclose_flag: Mapped[int]
    fclose_flag: Mapped[int]


