# ---
# # Urban Bike Parking System
# This script provides classes and logic for an urban bike parking solution, including parking spot management, reservations, locker access, notifications, analytics, and transit integration.
# ---

from typing import List, Dict, Optional
from datetime import datetime

# ---
# ## ParkingSpot Class
# Represents a bike parking spot with location, amenities, price, and availability.
# ---
class ParkingSpot:
    def __init__(self, spot_id: str, location: str, amenities: List[str], price: float, available: bool):
        self.spot_id = spot_id
        self.location = location
        self.amenities = amenities
        self.price = price
        self.available = available

# ---
# ## Reservation Class
# Handles reservations for parking spots, including user, time, and payment status.
# ---
class Reservation:
    def __init__(self, user_id: str, spot: ParkingSpot, start_time: datetime, end_time: datetime, paid: bool = False):
        self.user_id = user_id
        self.spot = spot
        self.start_time = start_time
        self.end_time = end_time
        self.paid = paid

# ---
# ## Locker Class
# Represents a smart locker with Bluetooth access for secure bike storage.
# ---
class Locker:
    def __init__(self, locker_id: str, bluetooth_key: str, is_locked: bool = True):
        self.locker_id = locker_id
        self.bluetooth_key = bluetooth_key
        self.is_locked = is_locked

    def unlock(self, key: str) -> bool:
        if key == self.bluetooth_key:
            self.is_locked = False
            return True
        return False

    def lock(self):
        self.is_locked = True

# ---
# ## NotificationService Class
# Sends notifications to users (e.g., reservation confirmations).
# ---
class NotificationService:
    def send_notification(self, user_id: str, message: str):
        # Placeholder for push/in-app notification logic
        print(f"Notify {user_id}: {message}")

# ---
# ## AnalyticsDashboard Class
# Collects and reports usage analytics for the parking system.
# ---
class AnalyticsDashboard:
    def __init__(self):
        self.usage_data = []

    def log_usage(self, data: Dict):
        self.usage_data.append(data)

    def generate_report(self):
        # Placeholder for analytics/reporting logic
        return self.usage_data

# ---
# ## TransitIntegration Class
# Integrates with transit APIs to suggest optimal routes to parking locations.
# ---
class TransitIntegration:
    def get_optimal_route(self, start: str, end: str) -> Dict:
        # Placeholder for transit API integration
        return {"route": [start, "Transit", end], "estimated_time": 30}

# ---
# ## Example Usage
# Demonstrates the workflow: discovering parking, making reservations, accessing lockers, sending notifications, logging analytics, and integrating with transit.
# ---
if __name__ == "__main__":
    # Discover parking
    spots = [ParkingSpot("S1", "Main St", ["covered", "secure"], 2.5, True)]
    available_spots = [s for s in spots if s.available]

    # Reserve and pay
    reservation = Reservation("user123", available_spots[0], datetime.now(), datetime.now(), paid=True)

    # Locker access
    locker = Locker("L1", "bt-key-123")
    if locker.unlock("bt-key-123"):
        print("Locker unlocked!")

    # Notifications
    notifier = NotificationService()
    notifier.send_notification("user123", "Your reservation is confirmed.")

    # Analytics
    analytics = AnalyticsDashboard()
    analytics.log_usage({"spot_id": "S1", "user_id": "user123", "timestamp": datetime.now()})

    # Transit integration
    transit = TransitIntegration()
    route = transit.get_optimal_route("Home", "Main St")
    print("Suggested route:", route)
