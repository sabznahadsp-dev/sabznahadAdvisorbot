from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards.reply import main_keyboard

router = Router()


@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(
        f"""
🌿 <b>به ربات کارشناس هوشمند سبز نهاد خوش آمدید.</b>

از طریق این ربات می‌توانید:

✅ مشاوره تخصصی کشاورزی
✅ مشاهده محصولات فروشگاه
✅ پیگیری سفارش
✅ دریافت تخفیف‌ها
✅ ارتباط با پشتیبانی

لطفاً یکی از گزینه‌های زیر را انتخاب کنید.
""",
        reply_markup=main_keyboard
    )