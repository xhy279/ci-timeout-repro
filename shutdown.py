import subprocess


def stop_worker(worker: subprocess.Popen, timeout: float) -> None:
    """Wait for the worker to shut down within the caller's deadline."""
    worker.wait(timeout=timeout)
