def measure_time(func):
    def wrapper(*args, **kwargs):
        from time import perf_counter

        start_time = perf_counter()
        result = func(*args, **kwargs)
        print(f"Time (ms): {(perf_counter() - start_time) * 1000}")
        return result

    return wrapper
