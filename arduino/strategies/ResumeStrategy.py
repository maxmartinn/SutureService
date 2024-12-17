from .DeviceStrategy import DeviceStrategy
from Device.Device import Device

class ResumeStrategy(DeviceStrategy):
    def execute(self, device: Device) -> dict:
        if device.is_running and device.is_paused:
            device.resume()
            return {
                "message": "Device resumed successfully",
                "metrics": device.getData(),
                "status_code": 200
            }
        return {
            "message": "Device is not running or not paused",
            "status_code": 400
        } 