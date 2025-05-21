import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    BACKGROUND_MAGENTA = '\033[105m'
    BACKGROUND_WHITE = '\033[47m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    ORANGE = '\033[38;5;208m'

def outputFile(root, file, extension):
    filePath = os.path.join(root, file)
    filePath = filePath.replace(file, f"{bcolors.FAIL}"+file+f"{bcolors.ENDC}").replace(extension, f"{bcolors.RED}"+extension+f"{bcolors.ENDC}")
    filePath = filePath.replace(directory, "").replace("\\","/")
    print(f" 📄 {bcolors.RED}" + filePath + f"{bcolors.ENDC}")
    return filePath

def scan(folder_path):
    numberScanned = 0
    foundFiles = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            numberScanned += 1
            if file in sensitiveFiles:
                foundFiles.append(outputFile(root, file, file.split(".")[-1]))
            for extension in sensitiveExtensions:
                if file.lower().endswith(extension) and file not in exceptions:
                    foundFiles.append(outputFile(root, file, extension))

    return (foundFiles, numberScanned)

sensitiveExtensions = [
    ".aws",
    ".bash_history",
    ".db",
    ".dockercfg",
    ".dockerconfigjson",
    ".env",
    ".ffs_db",
    ".history",
    ".key",
    ".keys",
    ".keystore",
    ".jks",
    ".p12",
    ".pem",
    ".pfx",
    ".pypirc",
]
sensitiveFiles = [
    "PASSWORD.txt",
    "PASSWORDS.txt",
    "password.txt",
    "passwords.txt",
    "secret.txt",
    "secrets.txt",
]
exceptions = [
    "Thumbs.db",
]
directories = [
    "C:/Users/Public",
]
for directory in directories:
    print(f"📁 {bcolors.WARNING}"+directory+f"{bcolors.ENDC}")    
    files, numberScanned = scan(directory)
    if not files:
        print(f"  ✅ {bcolors.OKGREEN}Nothing found.{bcolors.ENDC} ({bcolors.WARNING}{numberScanned:,} files checked{bcolors.ENDC})")
    else:
        print(f"  ☣️ {bcolors.OKGREEN}Some files found.{bcolors.ENDC} ({bcolors.WARNING}{numberScanned:,} files checked{bcolors.ENDC})")