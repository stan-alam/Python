from dataclasses import make_dataclass
Stonk = make_dataclass("Stonk", "symbol", "current", "high", "low")
stonk = Stonk("IBM", 180.00, high = 192.31, low = 68.00)
