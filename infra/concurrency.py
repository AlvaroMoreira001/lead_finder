from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Callable, Iterable, List, Any


def run_in_threads(func: Callable, items: Iterable[Any], max_workers: int = 5) -> List[Any]:
    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_item = {executor.submit(func, item): item for item in items}
        for future in as_completed(future_to_item):
            try:
                results.append(future.result())
            except Exception:
                continue
    return results
