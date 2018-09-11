# licencecreater
# What is it about 
  This is an application to accept only text files as an input and this text files will contain some words , which is need to 
  modify with ® symbol after the words , so appending the '®' after the word . for instance Nithin will change to Nithin®.
# Prerequisites
  need to install postman or any api testing tools to fire the api's
# Why to did it 
 it's just how to learn how to automate simple things using python in webservice
# What it contains
  python 3.5.5, Django 1.8.6, gunicorn 1.9 , whitenoise 4.0, psycopg2-2.7.5. The application hosted in pythonanywhere.
# how to start with 
  1) first of all the user need to install postman to do so visit the link  https://www.getpostman.com/apps and download the 
   application in your machine. In linux open it by entering postman in terminal and in windows just run the exe file. The      in posman first we need to send a POST Request to upload a txt file to make alternatons in the body of the post request 
   attach the txt file and the url need to trigger is http://nithinmanuel.pythonanywhere.com/licencecreater/document/create/ 
  ![alt text] (/home/nithin/Pictures/post_file.png). like in the picture and the response that you will get from the server
  will be the id of the document that is posted . please keep this id .
  
 2) Next step is pass this id a url and fetch the file that is allready uploaded with the id that we pass in the url . To         perform this we need to call GET , choose the GET in the postman and paste the give below url.                http://nithinmanuel.pythonanywhere.com/licencecreater/document/{}/convert/  the curly braces will be replaced by the id 
  of the file which will undergo alternation , so please send it without curly braces for example: http://nithinmanuel.pythonanywhere.com/licencecreater/document/3/convert/ , here we pass 3 as the id of the file . 

see screenshot of postman GET
https://github.com/nithinmanuel/licencecreater/blob/master/get_changed%20document.png  

  the json response will be with the particular words will undergo transformation.
  
  3) The other operations are CRUD on the words, the words subjected to alternation or the words intented to be replaced (append with ® ) needs to write it to database . so that the words needs to call a POST operation in postman with url  http://nithinmanuel.pythonanywhere.com/licencecreater/keyword/create/  , keep the id of the object word which is posted.
   ![alt text]
 4) To get the particular word that is created in database , you need to call GET in postman with url
 http://nithinmanuel.pythonanywhere.com/licencecreater/keyword/{}/get   here you need to pass the id of the keyword  follow the same style in step 2.
 5) To edit a particular word in the databse then call the POST operation in postman with this url http://nithinmanuel.pythonanywhere.com/licencecreater/keyword/{}/edit/ here you need to pass two parameters one is id of the word is need to replace and second one is the new word that is will replace the old one. 
 
 6) The another operation is to delete the object for this call the GET withcorresponding url http://nithinmanuel.pythonanywhere.com/licencecreater/keyword/{}/delete/ pass the id of the object that you no longer want to see it ,same in the case of previous steps.
 
 # Progress
 planing to add some more features and trying to deploye in AWS and heroku and it is on the way . 
 
 
  


 

 
