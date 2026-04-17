import time
from threading import Lock

cache = {}
cache_lock = Lock()


def get_from_cache(key, expiration):
    """
    Obtiene datos del caché si no han expirado.
    """

    with cache_lock:
        entry = cache.get(key)

        if not entry:
            return None

        data = entry.get("data")
        timestamp = entry.get("timestamp")

        # Validar estructura
        if data is None or timestamp is None:
            cache.pop(key, None)
            return None

        # Validar expiración
        if time.time() - timestamp < expiration:
            return data

        # Expirado → eliminar
        cache.pop(key, None)
        return None


def save_to_cache(key, data):
    """
    Guarda datos válidos en caché.
    """

    if data is None:
        return

    with cache_lock:
        cache[key] = {
            "data": data,
            "timestamp": time.time()
        }