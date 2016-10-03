from cuda_lint import Linter, util

class GoVet(Linter):
    syntax = 'Go'
    cmd = ('go', 'vet')
    regex = r'^.+?:(?P<line>\d+):(?P<col>\d+):\s+(?P<message>.+)'
    tempfile_suffix = 'go'
    error_stream = util.STREAM_STDERR
