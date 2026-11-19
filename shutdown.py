import subprocess


def stop_worker(worker: subprocess.Popen, timeout: float) -> None:
    """Wait for the worker to shut down within the caller's deadline."""
    if worker.stdin is not None:
        worker.stdin.close()
    worker.wait(timeout=timeout)
