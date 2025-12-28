"""
Tests for the Developer Agent

Note: These tests require valid API credentials to run.
Set up your .env file with OPENAI_API_KEY and GITHUB_TOKEN before running tests.
"""
import unittest
from unittest.mock import Mock, patch, MagicMock
from developer_agent import DeveloperAgent, create_developer_agent
from config import Config


class TestConfig(unittest.TestCase):
    """Tests for the Config class."""
    
    @patch.dict('os.environ', {
        'OPENAI_API_KEY': 'test_openai_key',
        'GITHUB_TOKEN': 'test_github_token',
        'GITHUB_REPOSITORY': 'test/repo'
    })
    def test_config_loads_from_env(self):
        """Test that Config loads from environment variables."""
        # Reload config to pick up mocked env vars
        from importlib import reload
        import config as config_module
        reload(config_module)
        
        self.assertTrue(config_module.Config.is_configured())
    
    @patch.dict('os.environ', {'OPENAI_API_KEY': '', 'GITHUB_TOKEN': ''})
    def test_config_validation_fails_without_keys(self):
        """Test that Config validation fails without required keys."""
        from importlib import reload
        import config as config_module
        reload(config_module)
        
        with self.assertRaises(ValueError):
            config_module.Config.validate()


class TestDeveloperAgent(unittest.TestCase):
    """Tests for the DeveloperAgent class."""
    
    @patch('developer_agent.ChatOpenAI')
    @patch('developer_agent.GitHubAPIWrapper')
    @patch('developer_agent.GitHubToolkit')
    @patch('developer_agent.initialize_agent')
    def test_agent_initialization(self, mock_init_agent, mock_toolkit, 
                                   mock_wrapper, mock_llm):
        """Test that DeveloperAgent initializes correctly."""
        # Setup mocks
        mock_tools = [Mock(name='tool1'), Mock(name='tool2')]
        mock_toolkit_instance = Mock()
        mock_toolkit_instance.get_tools.return_value = mock_tools
        mock_toolkit.from_github_api_wrapper.return_value = mock_toolkit_instance
        
        # Create agent
        agent = DeveloperAgent(
            github_token='test_token',
            github_repository='test/repo'
        )
        
        # Verify initialization
        mock_wrapper.assert_called_once()
        mock_toolkit.from_github_api_wrapper.assert_called_once()
        mock_llm.assert_called_once()
        mock_init_agent.assert_called_once()
        
        self.assertEqual(agent.github_token, 'test_token')
        self.assertEqual(agent.github_repository, 'test/repo')
    
    @patch('developer_agent.ChatOpenAI')
    @patch('developer_agent.GitHubAPIWrapper')
    @patch('developer_agent.GitHubToolkit')
    @patch('developer_agent.initialize_agent')
    def test_agent_run(self, mock_init_agent, mock_toolkit, 
                       mock_wrapper, mock_llm):
        """Test that agent can run a task."""
        # Setup mocks
        mock_tools = [Mock(name='tool1')]
        mock_toolkit_instance = Mock()
        mock_toolkit_instance.get_tools.return_value = mock_tools
        mock_toolkit.from_github_api_wrapper.return_value = mock_toolkit_instance
        
        mock_agent_instance = Mock()
        mock_agent_instance.run.return_value = "Task completed successfully"
        mock_init_agent.return_value = mock_agent_instance
        
        # Create agent and run task
        agent = DeveloperAgent(
            github_token='test_token',
            github_repository='test/repo'
        )
        result = agent.run("Test task")
        
        # Verify
        mock_agent_instance.run.assert_called_once_with("Test task")
        self.assertEqual(result, "Task completed successfully")
    
    @patch('developer_agent.ChatOpenAI')
    @patch('developer_agent.GitHubAPIWrapper')
    @patch('developer_agent.GitHubToolkit')
    @patch('developer_agent.initialize_agent')
    def test_get_available_tools(self, mock_init_agent, mock_toolkit, 
                                  mock_wrapper, mock_llm):
        """Test getting available tools."""
        # Setup mocks
        mock_tool1 = Mock(name='GetIssue')
        mock_tool1.name = 'GetIssue'
        mock_tool2 = Mock(name='CreateIssue')
        mock_tool2.name = 'CreateIssue'
        
        mock_toolkit_instance = Mock()
        mock_toolkit_instance.get_tools.return_value = [mock_tool1, mock_tool2]
        mock_toolkit.from_github_api_wrapper.return_value = mock_toolkit_instance
        
        # Create agent
        agent = DeveloperAgent(
            github_token='test_token',
            github_repository='test/repo'
        )
        
        # Get tools
        tools = agent.get_available_tools()
        
        # Verify
        self.assertEqual(len(tools), 2)
        self.assertIn('GetIssue', tools)
        self.assertIn('CreateIssue', tools)
    
    def test_agent_requires_token(self):
        """Test that agent raises error without GitHub token."""
        with self.assertRaises(ValueError):
            DeveloperAgent(github_token=None)


class TestCreateDeveloperAgent(unittest.TestCase):
    """Tests for the create_developer_agent factory function."""
    
    @patch('developer_agent.DeveloperAgent')
    @patch('developer_agent.Config')
    def test_create_developer_agent(self, mock_config, mock_agent_class):
        """Test the factory function."""
        mock_config.OPENAI_API_KEY = 'test_key'
        mock_config.GITHUB_TOKEN = 'test_token'
        mock_config.GITHUB_REPOSITORY = 'test/repo'
        
        create_developer_agent(github_repository='custom/repo')
        
        mock_config.validate.assert_called_once()
        mock_agent_class.assert_called_once()


if __name__ == '__main__':
    unittest.main()
