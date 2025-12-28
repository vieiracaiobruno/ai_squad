"""
Validation script to check the project structure and code quality
without requiring external dependencies.
"""
import os
import ast
import sys


def validate_python_syntax(filepath):
    """Validate Python file syntax."""
    try:
        with open(filepath, 'r') as f:
            code = f.read()
        ast.parse(code)
        return True, None
    except SyntaxError as e:
        return False, str(e)


def check_file_exists(filepath):
    """Check if a file exists."""
    return os.path.exists(filepath)


def validate_project_structure():
    """Validate the project structure."""
    print("=" * 60)
    print("AI Squad Project Validation")
    print("=" * 60)
    print()
    
    # Required files
    required_files = [
        'README.md',
        'requirements.txt',
        '.env.example',
        'config.py',
        'developer_agent.py',
        'main.py',
        'example_usage.py',
        'test_developer_agent.py',
        '__init__.py',
        'setup.py',
        'LANGCHAIN_GITHUB_INTEGRATION.md',
    ]
    
    print("Checking required files...")
    all_files_exist = True
    for filepath in required_files:
        exists = check_file_exists(filepath)
        status = "✓" if exists else "✗"
        print(f"  {status} {filepath}")
        if not exists:
            all_files_exist = False
    
    if not all_files_exist:
        print("\n✗ Some required files are missing!")
        return False
    
    print("\n✓ All required files exist!")
    
    # Validate Python files syntax
    print("\nValidating Python syntax...")
    python_files = [f for f in required_files if f.endswith('.py')]
    all_syntax_valid = True
    
    for filepath in python_files:
        valid, error = validate_python_syntax(filepath)
        status = "✓" if valid else "✗"
        print(f"  {status} {filepath}")
        if not valid:
            print(f"      Error: {error}")
            all_syntax_valid = False
    
    if not all_syntax_valid:
        print("\n✗ Some Python files have syntax errors!")
        return False
    
    print("\n✓ All Python files have valid syntax!")
    
    # Check README content
    print("\nValidating README.md content...")
    with open('README.md', 'r') as f:
        readme_content = f.read()
    
    required_sections = [
        'Features',
        'Installation',
        'Usage',
        'Available GitHub Tools',
        'Example Tasks',
    ]
    
    all_sections_present = True
    for section in required_sections:
        if section in readme_content:
            print(f"  ✓ Section '{section}' present")
        else:
            print(f"  ✗ Section '{section}' missing")
            all_sections_present = False
    
    if not all_sections_present:
        print("\n✗ README is missing some sections!")
        return False
    
    print("\n✓ README contains all required sections!")
    
    # Check requirements.txt
    print("\nValidating requirements.txt...")
    with open('requirements.txt', 'r') as f:
        requirements = f.read()
    
    required_packages = [
        'langchain',
        'langchain-community',
        'langchain-openai',
        'PyGithub',
        'python-dotenv',
        'pydantic',
    ]
    
    all_packages_present = True
    for package in required_packages:
        if package in requirements:
            print(f"  ✓ Package '{package}' listed")
        else:
            print(f"  ✗ Package '{package}' missing")
            all_packages_present = False
    
    if not all_packages_present:
        print("\n✗ Some required packages are missing!")
        return False
    
    print("\n✓ All required packages listed!")
    
    # Check .env.example
    print("\nValidating .env.example...")
    with open('.env.example', 'r') as f:
        env_content = f.read()
    
    required_env_vars = [
        'OPENAI_API_KEY',
        'GITHUB_TOKEN',
        'GITHUB_REPOSITORY',
    ]
    
    all_vars_present = True
    for var in required_env_vars:
        if var in env_content:
            print(f"  ✓ Variable '{var}' present")
        else:
            print(f"  ✗ Variable '{var}' missing")
            all_vars_present = False
    
    if not all_vars_present:
        print("\n✗ Some environment variables are missing!")
        return False
    
    print("\n✓ All environment variables documented!")
    
    # Summary
    print("\n" + "=" * 60)
    print("✓ PROJECT VALIDATION PASSED!")
    print("=" * 60)
    print()
    print("The AI Squad Developer Agent implementation is complete.")
    print("To use it:")
    print("  1. Install dependencies: pip install -r requirements.txt")
    print("  2. Copy .env.example to .env and fill in your credentials")
    print("  3. Run: python main.py --check-config")
    print("  4. Start using: python main.py 'Your task here'")
    print()
    return True


if __name__ == "__main__":
    try:
        success = validate_project_structure()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n✗ Validation failed with error: {e}")
        sys.exit(1)
