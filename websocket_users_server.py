import asyncio

import websockets
from websockets import ServerConnection


# Обработчик входящих сообщений
async def echo(websocket: ServerConnection):
    async for message in websocket:
        print(f"Получено сообщение от пользователя: {message}")

        # Отправляем 5 нумерованных ответов
        for num in range(1, 6):  # 1, 2, 3, 4, 5
            response = f"{num} Сообщение пользователя: {message}"
            await websocket.send(response)
            print(f"Отправлен ответ #{num}: {response}")


# Запуск WebSocket-сервера на порту 8765
async def main():
    server = await websockets.serve(echo, "localhost", 8765)
    print("WebSocket сервер запущен на ws://localhost:8765")
    await server.wait_closed()


asyncio.run(main())
