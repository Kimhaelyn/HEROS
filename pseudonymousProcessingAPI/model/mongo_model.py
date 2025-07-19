from pydantic import BaseModel
from typing import Optional, List
from typing import Dict

class Location(BaseModel):
    latitude: float
    longitude: float
    
class Person(BaseModel):
    peopleID: str
    gender: str
    age: int
    movement_direction: List[float]
    movement_speed: float
    location: Location
    mobile_number: str
    IMSI: str 
    

class Statistics(BaseModel):
    average_age: float
    median_age: float

class Event(BaseModel):
    name: str
    event_date: str
    event_location: str
    

class Cell(BaseModel):
    cellID: str
    population_size: int
    age_distribution: Dict[str, int]  
    statistics: Statistics
    event: Event
    people: List[Person]
    
    
    
class Data(BaseModel):
    _id:str
    datetime: str
    cells: List[Cell]
    