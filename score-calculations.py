### This python script calculates doctor rating scores based on raw data collected

import pandas as pd
import re

doc_details = pd.read_excel('X:\\ISB\\Course\\Term1\\Visit2\\Practicum\\doctor-details-updated.xlsx','Sheet1')

#x = re.sub("\'+|\[+|\'+|\]+","",doc_details.Award[0]).encode("ascii","ignore")


Number_of_Awards = doc_details.apply(lambda x: len(re.sub("\'+|\[+|\'+|\]+","",x.Award).split(',')), axis=1)
Number_of_Qualification = doc_details.apply(lambda x: len(re.sub("\'+|\[+|\'+|\]+","",x.Qualification).split(',')), axis=1)
Number_of_Speciality = doc_details.apply(lambda x: len(re.sub("\'+|\[+|\'+|\]+","",x.Speciality).split(',')), axis=1)

doc_details = doc_details.join(pd.DataFrame(Number_of_Awards, columns=['Number_of_Awards']))
doc_details = doc_details.join(pd.DataFrame(Number_of_Qualification, columns=['Number_of_Qualification']))
doc_details = doc_details.join(pd.DataFrame(Number_of_Speciality, columns=['Number_of_Speciality']))

doc_details.to_excel('X:\\ISB\\Course\\Term1\\Visit2\\Practicum\\doctor-details-updated2.xlsx','Sheet1')