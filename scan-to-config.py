import os


# Get the current working directory
current_dir = os.getcwd()

# Define the path to your Python files
FILES_DIR = os.path.join(current_dir)

# Define the path to your output YAML file
OUTPUT_FILE = os.path.join(current_dir, ".github/workflows/auto-build.txt")


def main():
    filenames = [f for f in os.listdir(FILES_DIR) if f.endswith(".py")]
    steps = generate_steps(filenames)
    write_yaml(steps)

def generate_steps(filenames):
    steps = []
    for filename in filenames:
        step = {
            "name": f"Build executable ({filename})",
            "run": f"pyinstaller --onefile {filename}"
        }
        steps.append(step)
    return steps

def write_yaml(steps):
    with open(OUTPUT_FILE, "w") as f:
        f.write("name: Build and Release Executable\n")
        f.write("\n")
        f.write("on:\n")
        f.write("  push:\n")
        f.write("    branches: [ main ]\n")
        f.write("  workflow_dispatch:\n")
        f.write("\n")
        f.write("jobs:\n")
        f.write("  build:\n")
        f.write("    runs-on: ubuntu-latest\n")
        f.write(f"    steps: {steps}\n")

if __name__ == "__main__":
    main()
