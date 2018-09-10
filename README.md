# licencecreater
this is a project to automaticaly insert the ® to a txt file which contains some special words that can be added according to your need.
first of all the the txt file is to send using postman to the project address and the project is hosted in pythonanywhere webhosting cloud 
the first url to send to   http://nithinmanuel.pythonanywhere.com/licencecreater/document/create/
the above url will return an id with that id send this url to append the ® after special words , the url is given below
http://nithinmanuel.pythonanywhere.com/licencecreater/document/{}/convert/  please pass the id which you got as return from the first url and with curly braces for ex:http://nithinmanuel.pythonanywhere.com/licencecreater/document/3/convert/
the return format will be in json and it will be the appendeded version .
there is some more api's to perform CRUD operation in the special words which is allready stored in the databse.
create the special words the special words means the words that you want to make changes by appending the  ®  symbol after the words
http://nithinmanuel.pythonanywhere.com/licencecreater/keyword/create/       to create
http://nithinmanuel.pythonanywhere.com/licencecreater/keyword/{}/get   get the word which is allready created using the url in line 10
and please pass the id of the word inside the curly braces and send it without the curly braces
http://nithinmanuel.pythonanywhere.com/licencecreater/keyword/{}/delete/  delete the word that is created before and please put the keyword in the braces position and send it without the braces
http://nithinmanuel.pythonanywhere.com/licencecreater/keyword/{}/edit/ edit a word that is need to be changed perfom this is the above mentioned style

 

 
