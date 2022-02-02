import asyncio
import signal

import asygpy


async def main() -> None:
    print("hello")

    notifier = asygpy.create_notifier()
    channel = (
        notifier.open_channel()
        .add_signal(signal.SIGINT)
        .add_signal(signal.SIGTERM)
    )
    notifier.start_notifying()

    signum = await channel.receive()
    if signum == signal.SIGINT:
        print("I received SIGINT but I don't care!")
    elif signum == signal.SIGTERM:
        print("I received SIGTERM but I don't care!")

    notifier.stop_notifying()


asyncio.run(main())
