#!/usr/bin/env python3
"""
GitHub Tools Verification Script
Tests the GitHub tools integration without requiring OpenAI API key.
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def test_tools_module():
    """Test that tools module can be imported and initialized."""
    print("🔍 Testing tools module import...")
    try:
        import tools
        print("✓ Tools module imported successfully")
        print(f"  GitHub tools available: {len(tools.github_tools)}")
        return True
    except Exception as e:
        print(f"✗ Failed to import tools: {e}")
        return False


def test_github_credentials():
    """Check if GitHub credentials are configured."""
    print("\n🔍 Checking GitHub credentials...")
    
    github_token = os.getenv("GITHUB_TOKEN")
    github_app_id = os.getenv("GITHUB_APP_ID")
    github_app_key = os.getenv("GITHUB_APP_PRIVATE_KEY")
    
    if github_token:
        print("✓ GITHUB_TOKEN is configured")
        print(f"  Token preview: {github_token[:10]}...")
        return True
    elif github_app_id and github_app_key:
        print("✓ GitHub App credentials are configured")
        print(f"  App ID: {github_app_id}")
        return True
    else:
        print("⚠️  No GitHub credentials found")
        print("  Add GITHUB_TOKEN to .env to enable GitHub tools")
        return False


def test_github_tools_with_credentials():
    """Test GitHub tools creation with actual credentials."""
    print("\n🔍 Testing GitHub tools creation...")
    
    # Reload tools module to pick up any new environment variables
    import importlib
    import tools
    importlib.reload(tools)
    
    if len(tools.github_tools) > 0:
        print(f"✓ GitHub tools initialized successfully")
        print(f"  Total tools available: {len(tools.github_tools)}")
        print("\n  Available tools:")
        for i, tool in enumerate(tools.github_tools, 1):
            print(f"    {i}. {tool.name}")
        return True
    else:
        print("⚠️  No GitHub tools available")
        print("  Configure GITHUB_TOKEN in .env to enable tools")
        return False


def test_tool_descriptions():
    """Show tool descriptions if tools are available."""
    import tools
    
    if len(tools.github_tools) == 0:
        return
    
    print("\n📚 Tool Descriptions:")
    print("=" * 70)
    for tool in tools.github_tools:
        print(f"\n🔧 {tool.name}")
        print(f"   {tool.description}")


def main():
    """Run all verification tests."""
    print("=" * 70)
    print("GitHub Tools Integration - Verification Script")
    print("=" * 70)
    
    tests = [
        test_tools_module(),
        test_github_credentials(),
        test_github_tools_with_credentials(),
    ]
    
    # Show tool descriptions if available
    test_tool_descriptions()
    
    print("\n" + "=" * 70)
    print("Verification Summary")
    print("=" * 70)
    
    if all(tests[:1]):  # At least tools module works
        print("✓ Basic setup is working")
        if tests[1]:  # Credentials configured
            print("✓ GitHub credentials are configured")
            if tests[2]:  # Tools created
                print("✓ GitHub tools are ready to use!")
                print("\n🚀 You can now run the squad with GitHub integration!")
                print("   Try: python main.py")
                print("   Or: python example_github_integration.py")
            else:
                print("⚠️  GitHub tools could not be initialized")
                print("   Check your credentials and try again")
        else:
            print("⚠️  GitHub credentials not configured")
            print("   Add GITHUB_TOKEN to .env to enable GitHub tools")
            print("   See README.md for instructions")
    else:
        print("✗ Setup verification failed")
        print("  Please check the errors above and fix them")
        return 1
    
    print("=" * 70)
    return 0


if __name__ == "__main__":
    sys.exit(main())
