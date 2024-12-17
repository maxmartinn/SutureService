from .DeviceStrategy import DeviceStrategy
from Device.Device import Device

class PauseStrategy(DeviceStrategy):
    def execute(self, device: Device) -> dict:
        if device.is_running and not device.is_paused:
            device.pause()
            return {
                "message": "Device paused successfully",
                "metrics": device.getData(),
                "status_code": 200
            }
        return {
            "message": "Device is not running or already paused",
            "status_code": 400
        } 