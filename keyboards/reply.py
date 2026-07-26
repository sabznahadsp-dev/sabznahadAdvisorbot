from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🌱 مشاوره گیاه")
        ],
        [
            KeyboardButton(text="🛍 فروشگاه"),
            KeyboardButton(text="📦 پیگیری سفارش")
        ],
        [
            KeyboardButton(text="🎁 تخفیف‌ها"),
            KeyboardButton(text="📚 آموزش کشاورزی")
        ],
        [
            KeyboardButton(text="☎️ پشتیبانی"),
            KeyboardButton(text="ℹ️ درباره سبز نهاد")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="یکی از گزینه‌ها را انتخاب کنید..."
)
phone_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="📱 ارسال شماره موبایل",
                request_contact=True
            )
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_register_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="✨ شروع ثبت اطلاعات",
                callback_data="start_register"
            )
        ]
    ]
)