import subprocess
import sys
import unittest

from shutdown import stop_worker


class WorkerShutdownTest(unittest.TestCase):
    def test_worker_reading_stdin_exits_on_shutdown(self):
        with subprocess.Popen(
            [sys.executable, "-c", "import sys; sys.stdin.read()"],
            stdin=subprocess.PIPE,
        ) as worker:
            try:
                stop_worker(worker, timeout=3)
                self.assertEqual(worker.returncode, 0)
            finally:
                if worker.poll() is None:
                    worker.kill()
                    worker.wait()
