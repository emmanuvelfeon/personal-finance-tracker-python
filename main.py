import pandas as pd  
import csv      
from datetime import datetime

class CSV:            # define a class named CSV
    CSV_FILE = "finance_data.csv"  
    COLUMNS = ["date","amount","category","description"]

    @classmethod    # this is a decorator
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)  #this code checks if a csv file is present
        except FileNotFoundError:  #we expect an error so that we can create a new CSV file
            df = pd.DataFrame(columns = cls.COLUMNS) #we create a dataframe(df) using pd  method in pandas to create a columns with these values
            df.to_csv(cls.CSV_FILE, index=False) #the data frame is converted to csv file with the name we gave aboev
                                   #data frame allows us to access these columns
    @classmethod
    def add_entry(cls, date, amount, category, description):  #we need to add things to the csv file so we use another classmethod
        new_entry = {           #we use a csv writer in pandas to write into the csv file
            "date": date,       #so we create a python dictionary
            "amount": amount,
            "category": category,
            "description": description
        }    
        with open(cls.CSV_FILE,"a", newline="") as csvfile:   #"a" means pending to the end of the file(adding to the end)
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS) #we take a dictionary and pass it to the csv file with these filed name
            writer.writerow(new_entry) #using this to write a new entry into csv file
        print("Entry added successfully")

    
    

CSV.initialize_csv() # this is to initilize the file
CSV.add_entry("20-07-2024", 12.65, "income", "salary") # to add into the csv file