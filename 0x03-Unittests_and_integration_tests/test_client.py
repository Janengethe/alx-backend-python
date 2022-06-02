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

    @patch('client.get_json', return_value=[{'name': 'Holberton'},
                                            {'name': '89'},
                                            {'name': 'alx'}])
    def test_public_repos(self, mock_repo):
        """
        Test GithubOrgClient's public_repos method
        """
        with patch.object(GithubOrgClient,
                          '_public_repos_url',
                          new_callable=PropertyMock,
                          return_value="https://api.github.com/") as m:
            test_client = GithubOrgClient('holberton')
            test_repo = test_client.public_repos()
            for idx in range(3):
                self.assertIn(mock_repo.return_value[idx]['name'], test_repo)
            mock_repo.assert_called_once()
            m.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ])
    def test_has_license(self, repo, license_key, expected):
        """Tests GithubOrgClient.has_license"""
        client_org = GithubOrgClient("holberton")
        licens_e = client_org.has_license(repo, license_key)
        self.assertEqual(licens_e, expected)


if __name__ == "__main__":
    """Entry point"""
    unittest.main()
