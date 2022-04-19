#!/usr/bin/env python3
"""
Module 2-measure_runtime
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """
    execute async_comprehension four times in parallel
    using asyncio.gather
    measures the total runtime and return it
    """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension()for i in range(4)))
    ends = time.perf_counter()
    return (ends - start)
