
from django.conf import settings
from .models import Keyword
from .models import Document
from pathlib import Path

from django.core.files import File
# the operation starts in another function known as uploaded the follow up is to first to read the file contant from uploaded  
# in the line 12 carry out this task . The line 15 pulls out all the objects in the databse and next line is a for loop iterating
# the keywords containing the words from databse the words only picking up the name of the words not the id which is unwanted 
# so the words will have the name of all words , after this again one more for loop where file_content.replace will replace the 
# word with '®' which will apply to all words in the for loop .last one is to return the edited filecontent will goes up to the
# upldoaded function .
# 

def convert_file(file):
    file_content = file.read().decode("utf-8-sig")

    print(file_content)
    keywords = Keyword.objects.all()
    words = [o.name for o in keywords]
    print(words)

    

    for word in words:

        file_content = file_content.replace(
            word, word + '®')
    print(file_content)
    return (file_content)
    
