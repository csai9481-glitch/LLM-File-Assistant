import os
from docx import Document
from PyPDF2 import PdfReader


def read_file(filepath):
    try:

        if filepath.endswith(".txt"):

            with open(filepath, "r", encoding="utf-8") as file:
                content = file.read()

        elif filepath.endswith(".docx"):

            doc = Document(filepath)

            content = "\n".join(
                [para.text for para in doc.paragraphs]
            )

        elif filepath.endswith(".pdf"):

            reader = PdfReader(filepath)

            content = ""

            for page in reader.pages:
                content += page.extract_text()

        else:

            return {
                "success": False,
                "error": "Unsupported file type"
            }

        return {
            "success": True,
            "content": content
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }


def list_files(directory):

    try:

        files = []

        for file in os.listdir(directory):

            filepath = os.path.join(directory, file)

            if os.path.isfile(filepath):

                files.append({
                    "name": file,
                    "size": os.path.getsize(filepath)
                })

        return files

    except Exception as e:

        return {"error": str(e)}


def search_in_file(filepath, keyword):

    result = read_file(filepath)

    if not result["success"]:
        return result

    matches = []

    lines = result["content"].split("\n")

    for line in lines:

        if keyword.lower() in line.lower():

            matches.append(line)

    return {
        "success": True,
        "matches": matches
    }


def write_file(filepath, content):

    try:

        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)

        return {
            "success": True,
            "message": "File written successfully"
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }