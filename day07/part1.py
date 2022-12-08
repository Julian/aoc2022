from __future__ import annotations
from dataclasses import dataclass, field
import sys


PROMPT = "$ "


def commands(lines):
    command, output = next(lines)[len(PROMPT):-1], []
    for line in lines:
        if line.startswith(PROMPT):
            yield command.split(), output
            command, output = line[len(PROMPT):-1], []
        else:
            output.append(line[:-1])
    if output:
        yield command.split(), output


@dataclass
class Directory:

    name: str = ""
    parent: Directory = field(default=None)  # type: ignore
    _subdirectories: dict[str, Directory] = field(default_factory=dict)
    _files_by_size: dict[str, int] = field(default_factory=dict)

    def __post_init__(self):
        if self.parent is None:
            self.parent = self

    def create_subdirectory(self, name):
        self._subdirectories[name] = Directory(name=name, parent=self)

    def create_file(self, name: str, size: int):
        self._files_by_size[name] = size

    def subdirectory(self, name):
        return self._subdirectories[name]

    @property
    def size(self):
        file_size = sum(self._files_by_size.values())
        return file_size + sum(d.size for d in self._subdirectories.values())

    def walk(self):
        yield self
        for subdirectory in self._subdirectories.values():
            yield from subdirectory.walk()


root = cwd = Directory()

for (command, *args), output in commands(sys.stdin):
    if command == "cd":
        arg, = args
        if arg == "/":
            cwd = parent = root
        elif arg == "..":
            cwd, parent = cwd.parent, cwd.parent.parent
        else:
            cwd, parent = cwd.subdirectory(arg), cwd
        assert output == []
    elif command == "ls":
        for line in output:
            info, _, name = line.partition(" ")
            if info == "dir":
                cwd.create_subdirectory(name=name)
            else:
                cwd.create_file(name=name, size=int(info))

total = sum(
    directory.size
    for directory in root.walk()
    if directory.size <= 100000
)
print(total)
