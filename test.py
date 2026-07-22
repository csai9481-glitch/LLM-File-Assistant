from fs_tools import *

print("\nFILES:")
print(list_files("resumes"))

print("\nSEARCH:")
print(
    search_in_file(
        "resumes/resume1.txt",
        "Python"
    )
)