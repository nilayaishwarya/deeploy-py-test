from typing import Optional

from pydantic import BaseModel
from git import Repo, Remote


class GitServiceOptions(BaseModel):
    """
    Class containing the Git client options

    Attributes:
      local_repository_path: str
        the relative or absolute path to the local git repository
      branch_name: str
        the branch name on which to commit. Defaults to the local 
        active branch
    """
    local_repository_path: str
    branch_name: Optional[str]


class GitService(object):
    """ 
    A class for interacting with a local Git project
    """

    repository: Repo
    remote: Remote

    def __init__(self, options: GitServiceOptions) -> None:
        """Initialise the Git client
        """
        self.repository = Repo(options.branch_name)
        self.remote = self.repository.remote('origin')

        if not self.__is_valid_git_project():
            raise Exception('Not a valid git project')

        return

    def __is_valid_git_project(self) -> bool:
        """Check if the supplied repository is valid
        """
        try:
            assert not self.repository.bare
        except:
            return False

        return True

    def addFolderToStaging(self, relative_folder_path: str) -> None:
        """Add the folder and all its contents to the git staging area

        Parameters
        ----------
          relative_folder_path: str 
            represents the relative path to the folder from the root of 
            the git directory
        """
        self.repository.index.add([relative_folder_path])
        return

    def commit(self, commit_message: str) -> None:
        """Create a new commit on the current branch

        Parameters
        ----------
          commit_message: str
            representing the commit message
        """
        self.repository.index.commit(commit_message)
        return

    def pull(self) -> None:
        """Pull from the default remote repository
        """
        self.remote.pull()
        return

    def push(self) -> None:
        """Push to the default remote repository
        """
        self.remote.push()
        return

    def get_remote_url(self) -> str:
        return self.remote.url
