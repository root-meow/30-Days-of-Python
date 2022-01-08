#Convert this to a dictionary with 4 keys.
(
 	"The Dark Side of the Moon",
 	"Pink Floyd",
 	1973,
 	(
 		"Speak to Me",
 		"Breathe",
 		"On the Run",
 		"Time",
 		"The Great Gig in the Sky",
 		"Money",
 		"Us and Them",
 		"Any Colour You Like",
 		"Brain Damage",
 		"Eclipse"
 	)
 )

#Q1 Answer

music = {
     "Album_name" : "The Dark Side of the Moon",
     "Artist" : "Pink Floyd",
     "Year" : "1973",
     "Tracks" : (
         "Speak to Me",
 		"Breathe",
 		"On the Run",
 		"Time",
 		"The Great Gig in the Sky",
 		"Money",
 		"Us and Them",
 		"Any Colour You Like",
 		"Brain Damage",
 		"Eclipse"
     )
 }


#Iterate over dict and print key alongide value
for key, value in music.items():
    print(f"{key} : {value}")

#Delete track and year of release. add key 'Date of release' value is March 1st 1973
del music ["Tracks"]
del music ["Year"]
music.update({"Release_date" : "March 1st 1973"})

#print(music)

#Q4 Try to retrieve non existing key. Do it again using get

#print(music["Tracks"])   Brings the key error as it should

print(music.get("Tracks")) #Returns none. 

