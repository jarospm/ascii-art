from typing import Optional

def greet(name: Optional[str] = None) -> str:
    return f"Hello, {name.upper()}!"

print(greet())
