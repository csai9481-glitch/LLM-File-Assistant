from fs_tools import read_file, list_files, search_in_file, write_file

while True:

    query = input("\nAsk me something: ")

    if query.lower() == "exit":
        print("Goodbye!")
        break

    elif "read all resumes" in query.lower():

        files = list_files("resumes")

        for file in files:

            result = read_file(f"resumes/{file}")

            print("\n------------------")
            print(file)
            print("------------------")
            print(result["content"])

    elif "python" in query.lower():

        files = list_files("resumes")

        print("\nResumes mentioning Python:\n")

        for file in files:

            result = search_in_file(
                f"resumes/{file}",
                "Python"
            )

            if result["matches"]:
                print(file)

    elif "summary" in query.lower():

        result = read_file("resumes/resume1.txt")

        summary = result["content"][:100]

        write_file(
            "summary.txt",
            summary
        )

        print("Summary file created!")

    else:
        print("Sorry, I don't understand.")