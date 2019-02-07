"""

"""

def handle_uploaded_file(f):

    with open('/home/myproject/ScienceBlog/text/name.txt', 'wb+') as destination:

        for chunk in f.chunks(): # looping over uploadedFile.chunks instead of read() ensures that large files don't overwhelm your system's memory
            destination.write(chunk)
