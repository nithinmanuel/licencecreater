
from django.conf import settings
from .models import Keyword
from .models import Document
from pathlib import Path

from django.core.files import File


def convert_file(file):
    file_content = file.read().decode("utf-8-sig")

    print(file_content)
    keywords = Keyword.objects.all()
    words = [o.name for o in keywords]
    print(words)

    #replace_word = [s + '®' for s in words]
    #print(replace_word)

    for word in words:

        file_content = file_content.replace(
            word, word + '®')
    print(file_content)
    return (file_content)
    #f = open('/home/nithin/oursite/media/uploaded/ola', 'r+')
    #converted_file = File(f)
    # converted_file.write(file_content)
    # converted_file.closed
    # return (converted_file)

    #obj = Document.objects.get(uploaded="yes")
    # print(obj)
    # filer = open(os.path.join(BASE_DIR, 'media\\uploaded', converted)
    #data_folder = Path("MEDIA_ROOT/uploaded")

    #file_to_open = data_folder / "yes.txt"
    #contents = open(str(yes), "r").read()
    #f = open(file_to_open)

    # f.close()
    # print(data)
    # print(file_content)
    # try:
    # ty = Document.objects.get(id=10, uploaded='converted')
    # except Document.DoesNotExist:
    # ty = None
    # print(ty)
    # obj = Document.objects.get(uploaded = 'converted')

    # print(obj)
    # tye = ty.read().decode("utf-8-sig")
    # tye.write(file_content)
    # print(tye)
    #converted_file = open(file.path, 'converted', 'w')
    # converted_file.write(file_content)
    # file_use = converted_file.read()#.decode("utf-8-sig")
    # print(converted_file)
    # converted_file.close()
    # response = convert_file.read()
    # print(response)
    # return (converted_file)
    # fp = open('file')
    # data = fp.read().decode("utf-8-sig")
    # print(data)

    # file_wse = file.open()
    # rt = open('file_we', 'r')
# print (file_content)
# ss ivide words le word fileisl undo ennu
    # print(keyswords) str(word) + str('®')
    # ds = keywords.values()  + ['®']
    # words = ds.values()
    # print(words)
    # g = bytes('®', encoding="UTF-8")
    # print(g)
