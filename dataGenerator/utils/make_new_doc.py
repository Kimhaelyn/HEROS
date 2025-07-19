from utils.make_person_object import * 
from bson import ObjectId
import random
import string
import datetime
import copy 


#사람 나이 통계 데이터 업데이트 
def calculate_statistics(people_list):
    ages = [p["age"] for p in people_list]
    average_age = round(sum(ages) / len(ages), 1)
    median_age = sorted(ages)[len(ages) //2]
    
    return {"average_age": average_age, "median_age": median_age}

#사람 나이 분산 통계 업데이트 
def calculate_age_distribution(people_list):
    dist = {str(age): 0 for age in [10, 20, 30, 40, 50, 60, "70+"]}
    for p in people_list:
        age = p["age"]
        if age < 20:
            dist["10"] += 1
        elif age < 30:
            dist["20"] += 1
        elif age < 40:
            dist["30"] += 1
        elif age < 50:
            dist["40"] += 1
        elif age < 60:
            dist["50"] += 1
        elif age < 70:
            dist["60"] += 1
        else:
            dist["70+"] += 1
            
    return dist

def add_person_to_cell(cell):
    
    current_people = cell["people"]
    new_person = generate_person(len(current_people)+1)
    current_people.append(new_person)
    
    cell["population_size"] += 1
    cell["age_distribution"] = calculate_age_distribution(current_people)
    cell["statistics"] = calculate_statistics(current_people)
    

def create_next_document(prev_doc):
    
    new_doc = copy.deepcopy(prev_doc)
    new_doc["_id"] = ObjectId()
    new_doc["datetime"] = (datetime.datetime.fromisoformat(prev_doc["datetime"]) + datetime.timedelta(minutes=5)).isoformat()
    
    for cell in new_doc["cells"]:
        for person in cell["people"]:
            old_loc = person["location"]
            if "movement_direction" in person:
                person["movement_direction"] = [
                    person["movement_direction"][0]+0.1,  # x
                    person["movement_direction"][1] + 6.9,  # y
                    person["movement_direction"][2] - 13.3   # z
                ]
        add_person_to_cell(cell)
    
    
    return new_doc 
