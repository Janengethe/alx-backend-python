#!/usr/bin/env python3
"""
Module test_client
"""
from parameterized import parameterized
import unittest
from unittest.mock import Mock, PropertyMock
from unittest.mock import patch

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test Class"""

    @parameterized.expand([
        ("google"),
        ("abc"),
        ])
    @patch("client.get_json")
    def test_org(self, org, mock_org):
        """Tests GithubOrgClient.org"""
        client_org = GithubOrgClient(org)
        respons = client_org.org
        self.assertEqual(respons, mock_org.return_value)
        mock_org.assert_called_once()

    def test_public_repos_url(self):
        """Tests GithubOrgClient._public_repos_url"""
        with patch.object(GithubOrgClient,
                          "org",
                          new_callable=PropertyMock) as p:
            p.return_value = {"repos_url": "89"}
            client_org = GithubOrgClient("holberton")
            test_repo_url = client_org._public_repos_url
            self.assertEqual(test_repo_url, p.return_value.get('repos_url'))
            p.assert_called_once()


if __name__ == "__main__":
    """Entry point"""
    unittest.main()
