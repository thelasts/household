from re import compile
from typing import Union

from aiogram.filters import BaseFilter
from aiogram.types import Message

from Controllers.const import REGEX_PURCHASE


class ValidPurchaseFilter(BaseFilter):
    async def __call__(self, message: Message) -> Union[bool, str]:
        text = message.text or ''
        reg = compile(REGEX_PURCHASE)
        return {"text": f"{message.from_user.first_name}'s purchase:'{text.replace('!', '').strip()}'"} \
            if reg.fullmatch(text) \
            else False
