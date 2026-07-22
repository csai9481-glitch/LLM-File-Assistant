from fs_tools import read_file
from fs_tools import list_files
from fs_tools import search_in_file
from fs_tools import write_file


while True:

    query = input("\nAsk me something: ")

    if query.lower() == "exit":

        print("Goodbye!")
        break

    elif "read all resumes" in query.lower():

        files = list_files("resumes")

        for file in files:

            result = read_file(
                f"resumes/{file['name']}"
            )

            print("\n------------------")
            print(file["name"])
            print("------------------")

            if result["success"]:
                print(result["content"])
            else:
                print(result["error"])

    elif "python" in query.lower():

        files = list_files("resumes")

        print("\nResumes mentioning Python:\n")

        for file in files:

            result = search_in_file(
                f"resumes/{file['name']}",
                "Python"
            )

            if result["matches"]:
                print(file["name"])

    elif "summary" in query.lower():

        result = read_file(
            "resumes/resume1.txt"
        )

        if result["success"]:

            summary = result["content"][:100]

            write_file(
                "summaries/summary.txt",
                summary
            )

            print("Summary file created!")

        else:

            print(result["error"])

    else:

        print("Sorry, I don't understand.")