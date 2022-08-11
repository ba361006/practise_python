import asyncio
import shlex
from typing import Optional, Set, Union

EMPTY_OUTPUT = {"", " "}


class CompletedProcess:
    """A process that has finished running.

    This is returned by shell_exec().

    Attributes:
      args: The list or str args passed to shell_exec().
      returncode: The exit code of the process, negative for signals.
      stdout: The standard output (Empty str if not captured).
      stderr: The standard error (Empty str if not captured).
      output: Combined stdout and stderr (Empty str if nothing captured).
    """

    def __init__(
        self,
        args: str,
        returncode: Optional[int] = None,
        stdout: Optional[Union[str, bytes]] = None,
        stderr: Optional[Union[str, bytes]] = None,
    ) -> None:
        self.args = args
        self.stdout = stdout  # type:ignore
        self.stderr = stderr  # type:ignore

        if returncode is None:
            returncode = 0
        self.returncode = returncode

    @property
    def stdout(self) -> str:
        if self._stdout is None:
            return ""
        return self._stdout.decode("utf8") if isinstance(self._stdout, bytes) else self._stdout

    @stdout.setter
    def stdout(self, value: Union[str, bytes, None]) -> None:
        self._stdout = value

    @property
    def stderr(self) -> str:
        if self._stderr is None:
            return ""
        return self._stderr.decode("utf8") if isinstance(self._stderr, bytes) else self._stderr

    @stderr.setter
    def stderr(self, value: Union[str, bytes, None]) -> None:
        self._stderr = value

    @property
    def output(self) -> str:
        """Output returns combined stdout and stderr as a single string."""

        combined_output: Set[str] = set()
        if self.stdout is not None:
            combined_output.add(self.stdout)
        if self.stderr is not None:
            combined_output.add(self.stderr)

        combined_output = combined_output - EMPTY_OUTPUT

        # Will output empty string if the combined_output is empty.
        return ", ".join(combined_output)

    def __str__(self) -> str:
        return str(
            f"Command: {self.args} completed "
            f"with returncode {self.returncode} "
            f"and output: {self.output}"
        )

# async def shell_exec(*cmd: str) -> CompletedProcess:
#     sh_cmd = shlex.join(cmd)
#     print("sh_cmd: ",sh_cmd)
#     process = await asyncio.create_subprocess_shell(
#         sh_cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
#     )

#     stdout, stderr = await process.communicate()

#     return CompletedProcess(sh_cmd, process.returncode, stdout=stdout, stderr=stderr)

def hello(*cmd: str):
    print(cmd)
    print(shlex.join(cmd))

hello("bin", "user", "mkdir", "hello")