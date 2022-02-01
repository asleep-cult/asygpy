## asygpy
asyncio signal handlers for Windows and Unix.

### Reveiving Signals
```py
import asygpy
import asyncio
import signal

async def main() -> None:
    notifier = asygpy.create_notifier()
    channel = (
        notifier.open_channel()
        .add_signal(signal.SIGINT)
        .add_signal(signal.SIGTERM)
    )
    notifier.start_notifying()

    signum = await channel.receive()
    if signum == signal.SIGINT:
        print("Shutting down due to SIGINT")
    elif signum == signal.SIGTERM:
        print("Shutting down due to SIGTERM")

asyncio.run(main())
```

### Receiving Multiple Signals
```py
import asygpy
import asyncio
import signal

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
```
