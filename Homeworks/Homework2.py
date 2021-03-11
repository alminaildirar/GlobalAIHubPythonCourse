#CV application
#Create 5 dictionaries.Each dictionary should represent a CV.
#Create a CV containing the information of the 5 created people.

CVs = [{"Cv_no":1,
       "Name":"Almina",
       "Surname":"Ildırar",
       "City":"Adana",
       "Contact_number":"234565324",
       "Graduation_school":"Kocaeli_University",
       "Job_title":"Computer Engineer",
       "Skills":["Java","Python","C++"],
       "English_level":"upper_indermediate"
       
       },{"Cv_no":2,
       "Name":"Egemen",
       "Surname":"Senturk",
       "City":"Konya",
       "Contact_number":"598598943",
       "Graduation_school":"Marmara_University",
       "Job_title":"Software Engineer",
       "Skills":["JavaScript","PHP","Java"],
       "English_level":"advanced"
       
       },{"Cv_no":3,
       "Name":"Melisa",
       "Surname":"Can",
       "City":"Kocaeli",
       "Contact_number":"43873456573",
       "Graduation_school":"Cukurova_University",
       "Job_title":"Database Administrator",
       "Skills":["Apache","HTML","Java","SQL"],
       "English_level":"indermediate"
       
       },{"Cv_no":4,
       "Name":"Okan",
       "Surname":"Tepecik",
       "City":"Mersin",
       "Contact_number":"7578474683",
       "Graduation_school":"Mersin_University",
       "Job_title":"Computer Engineer",
       "Skills":["Linux","MySQL","CSS","Python"],
       "English_level":"advanced"
       
       },{"Cv_no":5,
       "Name":"Berra",
       "Surname":"Han",
       "City":"Ankara",
       "Contact_number":"8475489302",
       "Graduation_school":"Gazi_University",
       "Job_title":"Web Developer",
       "Skills":["HTML/CSS","JavaScript","PHP.NET"],
       "English_level":"advanced"
       
       }]
          

for i in range(len(CVs)):
    print("----------------------")
    for key,value in CVs[i].items():
        print(str(key)+ ": " + str(value) )       
        

          
          
          
          
          
          
          
          
          
          
          
          
          
          
          