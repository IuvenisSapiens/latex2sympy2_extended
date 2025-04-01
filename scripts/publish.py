import subprocess
import os
import shutil

def run_command(command, message):
    print(message)
    result = subprocess.run(command, shell=True, check=True)
    return result

def clean_builds():
    build_dirs = ['dist', 'build']
    egg_info_dirs = [d for d in os.listdir('.') if d.endswith('.egg-info')]
    
    print("Cleaning previous builds...")
    for dir in build_dirs + egg_info_dirs:
        if os.path.exists(dir):
            shutil.rmtree(dir)

def build_package():
    run_command('python -m build', 'Building package...')

def upload_to_pypi():
    run_command('python -m twine upload dist/*', 'Uploading to PyPI...')

def main():
    print("=== Latex2Sympy2 Extended Package Publisher ===")
    
    # Install publishing dependencies
    run_command('python -m pip install --upgrade pip build twine', 'Installing publishing dependencies...')
    
    # Get the script directory and change to the project root
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.join(script_dir, '..')
    os.chdir(project_root)
    
    # Execute the publishing process
    clean_builds()
    build_package()
    upload_to_pypi()
    
    print("Package successfully published to PyPI!")
    print("You can now install it with: pip install latex2sympy2-extended")

if __name__ == '__main__':
    try:
        main()
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
        exit(1)
