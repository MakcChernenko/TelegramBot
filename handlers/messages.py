from aiogram import Router, types

router = Router()

@router.message()
async def echo(message: types.Message):
    if message.text == "Привіт" or message.text == "привіт" or message.text == "ПРИВІТ":
        await message.answer(f"Цвірінь!")
    elif message.text == "Як ти" or message.text == "ЯК ТИ" or message.text == "як ти" or message.text == "Як ти?" or message.text == "ЯК ТИ?" or message.text == "як ти?":
        await message.answer(f"Цвірінь! Добре, цвірінь, а ти як?")
    elif message.text == "Добре" or message.text == "ДОБРЕ" or message.text == "добре" or message.text == "ДОБРЕ":
        await message.answer(f"Цвірінь! Радий, що ти в порядку, як мама?")
    elif message.text == "потихенько" or message.text == "Потихенько" or message.text == "ПОТИХЕНЬКО":
        await message.answer(f"Цвірінь! Шкода стареньких, війна ще ця, вони переживають дуже...")
    elif message.text == "Ох" or message.text == "ох" or message.text == "ОХ":
        await message.answer(f"Цвірінь! Охо-хо...")
    elif message.text == "Що робиш" or message.text == "ЩО РОБИШ" or message.text == "що робиш" or message.text == "Що робиш?":
        await message.answer("Цвірінь! Тримаюся, як завжди, цвірінь 😎")
    elif message.text == "Гарно" or message.text == "ГАРНО" or message.text == "гарно":
        await message.answer("Цвірінь! Що гарно?")
    elif message.text == "Сумно" or message.text == "СУМНО" or message.text == "сумно":
        await message.answer("Цвірінь! Мені теж(")
    elif message.text == "Що по новинах" or message.text == "ЩО ПО НОВИНАХ" or message.text == "що по новинах":
        await message.answer("Цвірінь! Шахіди літають, Ракети падають, новини страшні(")
    elif message.text == "Як твоя мама?" or message.text == "як твоя мама?" or message.text == "ЯК ТВОЯ МАМА?":
        await message.answer("Цвірінь! Я мовна модель створена тобою, у мене не має мами 😢")
    else:
        await message.answer(f"Цвірінь! Ти написав \"{message.text}\", але я не знаю такої команди")
