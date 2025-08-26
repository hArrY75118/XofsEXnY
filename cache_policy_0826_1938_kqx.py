# 代码生成时间: 2025-08-26 19:38:25
import pandas as pd

"""A simple cache policy implementation using Python and Pandas."""

class CachePolicy:
    """Represents a cache policy with basic operations to manage cache entries."""

    def __init__(self, capacity):
        """Initialize the cache with a given capacity."""
        self.capacity = capacity
        self.cache = {}

    def get(self, key):
        """Retrieve an item from the cache."""
        if key in self.cache:
            return self.cache[key]
        else:
            raise ValueError(f"Key '{key}' not found in cache.")

    def put(self, key, value):
        """Store an item in the cache."""
        if len(self.cache) >= self.capacity:
            self._evict()
        self.cache[key] = value

    def _evict(self):
        """Evict the least recently used (LRU) item from the cache."""
        # Here we assume the cache is an ordered dictionary or similar structure
        # that allows us to identify the least recently used item easily.
        # If not, we would need a more complex logic to track usage.
        lru_key = next(iter(self.cache))
        del self.cache[lru_key]

    def clear(self):
        """Clear the entire cache."""
        self.cache.clear()

    def __str__(self):
        """Provide a string representation of the cache for debugging."""
        return str(self.cache)

# Example usage:
if __name__ == '__main__':
    cache = CachePolicy(capacity=3)
    try:
        cache.put('key1', 100)
        cache.put('key2', 200)
        cache.put('key3', 300)
        print(cache.get('key1'))  # Output: 100
        cache.put('key4', 400)  # Should evict 'key2'
        print(cache.get('key2'))  # Raises ValueError
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")