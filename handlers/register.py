from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, Contact
from aiogram.fsm.context import FSMContext

from keyboards.reply import start_register_keyboard, main_keyboard
from keyboards.reply import phone_keyboard
from states.register import RegisterState
from utils.json_db import user_exists, get_user, save_user

router = Router()


@router.message(CommandStart())
async def register_start(message: Message, state: FSMContext):
    await state.clear()

    if user_exists(message.from_user.id):
        user = get_user(message.from_user.id)

        await message.answer(
            f"🌿 سلام {user['first_name']} عزیز\n\n"
            "به ربات سبز نهاد خوش آمدید.",
            reply_markup=main_keyboard
        )
        return

    await message.answer(
        "🌿 <b>به خانواده سبز نهاد خوش آمدید</b>\n\n"
        "برای استفاده از امکانات ربات، ابتدا اطلاعات خود را تکمیل کنید.\n\n"
        "🔒 اطلاعات شما کاملاً محرمانه خواهد بود.",
        reply_markup=start_register_keyboard
    )


@router.callback_query(F.data == "start_register")
async def start_register(callback: CallbackQuery, state: FSMContext):
    await state.set_state(RegisterState.first_name)

    await callback.message.edit_text(
        "👤 <b>مرحله ۱ از ۳</b>\n\n"
        "لطفاً نام خود را وارد کنید."
    )

    await callback.answer()


@router.message(RegisterState.first_name)
async def get_first_name(message: Message, state: FSMContext):
    await state.update_data(first_name=message.text)

    await state.set_state(RegisterState.last_name)

    await message.answer(
        "🪪 <b>مرحله ۲ از ۳</b>\n\n"
        "لطفاً نام خانوادگی خود را وارد کنید."
    )


@router.message(RegisterState.last_name)
async def get_last_name(message: Message, state: FSMContext):
    await state.update_data(last_name=message.text)

    await state.set_state(RegisterState.phone)

    await message.answer(
        "📱 <b>مرحله ۳ از ۶</b>\n\n"
        "لطفاً با دکمه زیر شماره موبایل خود را ارسال کنید.",
        reply_markup=phone_keyboard
    )


@router.message(RegisterState.phone, F.contact)
async def get_phone(message: Message, state: FSMContext):

    data = await state.get_data()

    save_user(
        message.from_user.id,
        {
            "telegram_id": message.from_user.id,
            "first_name": data["first_name"],
            "last_name": data["last_name"],
            "phone": message.contact.phone_number,
        },
    )

    await state.clear()

    await message.answer(
        "✅ اطلاعات شما با موفقیت ثبت شد.\n\n"
        f"👤 {data['first_name']} {data['last_name']}\n"
        f"📱 {message.contact.phone_number}\n\n"
        "🌿 به خانواده سبز نهاد خوش آمدید.",
        reply_markup=main_keyboard,
    )