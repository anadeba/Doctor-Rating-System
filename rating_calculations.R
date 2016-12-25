### Import data and replace all NA values with 0

doc_details = read.csv('C:\\Users\\debanjan\\Desktop\\doctor-details-updated2.csv')
doc_details[is.na(doc_details)] = 0

cardiology_doc_details = subset(doc_details, grepl('Cardiologist',doc_details$Speciality) == TRUE)
neurologist_doc_details = subset(doc_details, grepl('Neurologist',doc_details$Speciality) == TRUE)
gynecologist_doc_details = subset(doc_details, grepl('Gynecologist|Infertility Specialist|Obstetrician',doc_details$Speciality) == TRUE)
ent_doc_details = subset(doc_details, grepl('ENT|Otorhinolaryngologist',doc_details$Speciality) == TRUE)


### Define Normalize Function

normalize_func <- function(alist) {
  
  output = lapply(alist, function(x) (x - min(alist, na.rm = TRUE))/(max(alist, na.rm = TRUE) - min(alist, na.rm = TRUE)))
  return(output)
}

doctors = gynecologist_doc_details
  
  ### Normalize Experience, Likes, Polarity, Number of Awards, Number of Qualifications, Number of Specialty
  
  Norm_Experience = normalize_func(doctors$Experience)
  Norm_Likes = normalize_func(doctors$Likes)
  Norm_polarity  = normalize_func(doctors$polarity)
  Norm_Number_of_Awards = normalize_func(doctors$Number_of_Awards)
  Norm_Number_of_Qualification = normalize_func(doctors$Number_of_Qualification)
  
  
  ### Calculate Score and rating (5 point scale)
  
  score = lapply(seq_along(Norm_Experience), function(i) (unlist(Norm_Experience[i]) + unlist(Norm_Likes[i]) + unlist(Norm_polarity[i]) + unlist(Norm_Number_of_Awards[i]) + unlist(Norm_Number_of_Qualification[i])))
  
  rating = lapply(score, function(x) (x*5)/5)
  
  doctors$Norm_Experience<-Norm_Experience
  doctors$Norm_Likes<-Norm_Likes
  doctors$Norm_polarity<-Norm_polarity
  doctors$Norm_Number_of_Awards<-Norm_Number_of_Awards
  doctors$Norm_Number_of_Qualification<-Norm_Number_of_Qualification
  
  doctors$Rating<-rating
  
  

write.xlsx(x = doctors, file = 'C:\\Users\\debanjan\\Desktop\\gynecologist_details.xlsx',
           sheetName = "Sheet1", row.names = FALSE)






