def get_details(name, key, ls):
    for contact in ls:
        #Block A, repeated for every item iterable
        if name == contact["name"]:
             return contact[key]       
    #Block B, after iteration ended
    return None

phonebook=[{"name":"Andrew", "mobile_phone": 9477865, " office_phone":6612345, "email":"andrew@sutd.edu.sg"},{"name":"Bobby","mobile_phone": 8123498, "office_phone":6654321, "email": "bobby@sutd.edu.sg"}]
print(get_details("Andrew", "mobile_phone",phonebook))
