#!/usr/bin/env python3
import asyncio
import bluetooth  # from pybluez
from bleak import BleakScanner

# --- Classic Bluetooth scan (blocking) ---
def classic_scan():
    print("\n=== Classic Bluetooth Devices ===")
    try:
        devices = bluetooth.discover_devices(duration=8, lookup_names=True, lookup_class=True)
        for addr, name, dev_class in devices:
            print(f"Device: {name}")
            print(f"  Address: {addr}")
            print(f"  Class: {dev_class}")
            print("-" * 40)
    except Exception as e:
        print(f"Classic scan error: {e}")

# --- BLE scan (async) ---
async def ble_scan():
    print("\n=== BLE Devices ===")
    try:
        devices = await BleakScanner.discover(timeout=8)  # 8-second scan
        for d in devices:
            print(f"Device: {d.name or 'Unknown'}")
            print(f"  Address: {d.address}")
            print(f"  RSSI: {d.rssi} dBm")
            if d.metadata:
                for key, value in d.metadata.items():
                    print(f"  {key}: {value}")
            print("-" * 40)
    except Exception as e:
        print(f"BLE scan error: {e}")

# --- Main ---
def main():
    print("Starting hybrid Bluetooth scan...\n")

    # Run classic scan first
    classic_scan()

    # Then run BLE scan
    asyncio.run(ble_scan())

if __name__ == "__main__":
    main()
