db = db.getSiblingDB("HEROS");

db.people_data.insertMany([
  {
    _id: ObjectId("6874c7f7567d6f98df083cd1"),
    datetime: "2025-07-14T18:03:51",
    cells: [
      {
        cellID: "cell_01",
        population_size: 3,
        age_distribution: {
          "10": 0,
          "20": 1,
          "30": 1,
          "40": 1,
          "50": 0,
          "60": 0,
          "70+": 0
        },
        statistics: {
          average_age: 33.3,
          median_age: 30
        },
        event: {
          name: "야구 경기 (두산 vs 한화)",
          event_date: "2024-08-26T18:00:00/2024-08-26T22:00:00",
          event_location: "잠실 경기장"
        },
        people: [
          {
            peopleID: "person_001",
            gender: "male",
            age: 25,
            movement_direction: [
              -9.705,
              32.223,
              432.062
            ],
            movement_speed: 1.5,
            location: {
              latitude: 37.514,
              longitude: 127.123
            },
            mobile_number: "010-7516-7530",
            IMSI: "084905900634180422"
          },
          {
            peopleID: "person_002",
            gender: "male",
            age: 34,
            movement_direction: [
              7.473,
              46.037,
              484.169
            ],
            movement_speed: 1.1,
            location: {
              latitude: 37.515,
              longitude: 127.124
            },
            mobile_number: "010-6232-2842",
            IMSI: "084905900681152029"
          },
          {
            peopleID: "person_003",
            gender: "female",
            age: 34,
            movement_direction: [
              -4.902,
              40.274,
              423.107
            ],
            movement_speed: 1.1,
            location: {
              latitude: 37.516,
              longitude: 127.125
            },
            mobile_number: "010-4719-7270",
            IMSI: "084905900629638360"
          }
        ]
      }
    ]
  }
]);
