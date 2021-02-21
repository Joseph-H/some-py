import asyncio

async def compute_square(x):
    # await can only be used from async functions
    await asyncio.sleep(1)
    return x * x

async def square(x):
    print('Square', x)
    res = await compute_square(x)
    print('End square', x)
    return res
  
async def when_done(tasks):
    # as the tasks complete then print the results
    for res in asyncio.as_completed(tasks):
        print('Result:', await res)

# Create event loop
loop = asyncio.get_event_loop()
loop.run_until_complete(when_done([
    square(1),
    square(2),
    square(3)
]))
