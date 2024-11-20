# Open the file using an absolute pathname
with open("C:\\Users\\lambertk\\parent\\current\\child\\myfile.txt", 'r') as f:
    content = f.read()
    print(content)
