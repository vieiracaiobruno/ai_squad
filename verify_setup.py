"""
Setup Verification Script
Run this script to verify your environment is properly configured.
"""

import os
import sys


def check_dependencies():
    """Check if all required packages are installed."""
    print("🔍 Checking dependencies...")
    
    required_packages = [
        ('crewai', 'CrewAI'),
        ('langchain', 'LangChain'),
        ('langchain_openai', 'LangChain OpenAI'),
        ('langchain_community', 'LangChain Community'),
        ('dotenv', 'Python Dotenv')
    ]
    
    missing = []
    for package, name in required_packages:
        try:
            __import__(package)
            print(f"  ✓ {name}")
        except ImportError:
            print(f"  ✗ {name} - NOT INSTALLED")
            missing.append(name)
    
    if missing:
        print(f"\n❌ Missing packages: {', '.join(missing)}")
        print("   Run: pip install -r requirements.txt")
        return False
    
    print("✅ All dependencies installed\n")
    return True


def check_environment():
    """Check if environment variables are configured."""
    print("🔍 Checking environment configuration...")
    
    from dotenv import load_dotenv
    load_dotenv()
    
    openai_key = os.getenv("OPENAI_API_KEY")
    github_token = os.getenv("GITHUB_TOKEN")
    
    if not openai_key:
        print("  ✗ OPENAI_API_KEY - NOT SET")
        print("     Required for running the squad")
        status = False
    else:
        print(f"  ✓ OPENAI_API_KEY - Set ({openai_key[:10]}...)")
        status = True
    
    if not github_token:
        print("  ⚠️  GITHUB_TOKEN - NOT SET")
        print("     Optional: GitHub tools will not be available")
    else:
        print(f"  ✓ GITHUB_TOKEN - Set ({github_token[:10]}...)")
    
    if not status:
        print("\n❌ Missing required environment variables")
        print("   Create a .env file with your credentials")
        print("   See .env.example for template")
        return False
    
    print("✅ Environment configured\n")
    return True


def check_modules():
    """Check if all project modules can be imported."""
    print("🔍 Checking project modules...")
    
    modules = ['tools', 'agents', 'tasks', 'crew', 'main', 'examples']
    
    for module in modules:
        try:
            __import__(module)
            print(f"  ✓ {module}.py")
        except Exception as e:
            print(f"  ✗ {module}.py - ERROR: {str(e)[:50]}...")
            return False
    
    print("✅ All modules valid\n")
    return True


def main():
    """Run all checks."""
    print("=" * 70)
    print("🚀 AI Squad - Setup Verification")
    print("=" * 70)
    print()
    
    checks = [
        ("Dependencies", check_dependencies),
        ("Environment", check_environment),
        ("Project Modules", check_modules)
    ]
    
    results = []
    for name, check_func in checks:
        try:
            result = check_func()
            results.append(result)
        except Exception as e:
            print(f"❌ Error checking {name}: {e}\n")
            results.append(False)
    
    print("=" * 70)
    if all(results):
        print("✅ All checks passed! You're ready to run the squad.")
        print("\nRun: python main.py")
    else:
        print("⚠️  Some checks failed. Please fix the issues above.")
        print("\nFor help, see:")
        print("  - README.md (English)")
        print("  - GUIA_PT.md (Portuguese)")
    print("=" * 70)
    
    return all(results)


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
