from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from strategies.DeviceStrategyFactory import DeviceStrategyFactory
from Device.Device import Device
import uvicorn

app = FastAPI()
device = Device("123")

class DeviceControl(BaseModel):
    action: str

@app.post("/device/control")
def controlDevice(control: DeviceControl):
    strategy = DeviceStrategyFactory.getStrategy(control.action)
    
    if not strategy:
        raise HTTPException(status="error", detail="Invalid action")
    
    return strategy.execute(device)

if __name__ == "__main__":
    uvicorn.run(app, host="172.16.227.89", port=8080)
