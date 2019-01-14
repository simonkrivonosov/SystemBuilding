content = ["#pragma once", "//put code here .. ", "//someting else"]

print("Generating main.h ..")

with open("./main.h", 'w') as file:
    for line in content:
        file.write(line + "\n");
