import asyncio
import signal

import asygpy


async def main() -> None:
    notifier = asygpy.create_notifier()
    channel = (
        notifier.open_channel()
        .add_signal(signal.SIGINT)
        .add_signal(signal.SIGTERM)
    )
    notifier.start_notifying()

    async for signum in channel:
        if signum == signal.SIGINT:
            print("I received SIGINT but I don't care!")
        elif signum == signal.SIGTERM:
            print("I received SIGTERM but I don't care!")


asyncio.run(main())
