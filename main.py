from fastapi import FastAPI
from laptop import Laptop


app = FastAPI()
laptop_list = [
    {
        "id": 1,
        "brand": "Lenovo",
        "capacity": 8,
        "screensize": 8.1
    },
    {
        "id": 2,
        "brand": "HewalettPackard",
        "capacity": 16,
        "screensize": 16.2
    }
]

@app.get("/")
def laptop_shop():
    print(f"inside laptop_shop")
    return {"message": "Welcome to the Laptop Shop"}

@app.post("/new-laptop")
def add_new_laptop(laptop: Laptop):
    laptop_list.append(laptop.dict())
    return laptop_list

@app.get("/laptops")
def get_all_laptops():
    return laptop_list

    

# if __name__ == '__main__': 
#    print(f"startup |")
