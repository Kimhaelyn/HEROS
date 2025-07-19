import random
import string

def generate_moblie_number():
    return f"010-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}"

def mask_mobile_number(number):
    return number[:4] + "****" + number[-5:]

def generate_IMSI():
    return ''.join(random.choices(string.digits, k=17))

def get_age_group(age):
    
    if age< 20:
        if age < 20:
            return f"{'early' if age < 15 else 'mid'}_10"
        elif age < 30:
            return f"{'early' if age < 25 else 'mid'}_20"
        elif age < 40:
            return f"{'early' if age < 35 else 'mid'}_30"
        elif age < 50:
            return f"{'early' if age < 45 else 'mid'}_40"
        elif age < 60:
            return f"{'early' if age < 55 else 'mid'}_50"
        elif age < 70:
            return f"{'early' if age < 65 else 'mid'}_60"
        else:
            return f"{'early' if age < 75 else 'mid'}_70"

def generate_person(index):
    #사람 객체 생성 
    age = random.randint(10, 90)
    gender = random.choice(["male", "female"])
    mobile = generate_moblie_number()
    
    return {
        "peopleID": f"person_{index:03d}",
        "gender": gender,
        "age": age,
        "age_group": get_age_group(age),
        "movement_direction": [
            round(random.uniform(-3, -5), 1),    # x
            round(random.uniform(21, 50), 3),    # y
            round(random.uniform(300, 500), 3)   # z
            ],
        "movement_speed": round(random.uniform(0.5, 2.0), 1),
        "location": {
            "latitude": round(random.uniform(37.514, 37.523), 6),
            "longitude": round(random.uniform(127.124, 127.132), 6)
        },
        "mobile_number": mobile,
        "mobile_number_masking": mask_mobile_number(mobile),
        "IMSI": generate_IMSI()
    }
    
    

