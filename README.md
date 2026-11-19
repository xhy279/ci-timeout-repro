# CI timeout reproduction

This synthetic regression test models a CI worker that reads stdin until EOF.
The baseline waits for the worker to exit while its input is still open.
The test reports a timeout after three seconds and cleans up the child.
The fix closes the input before waiting so the worker can exit.

Run locally with `python3 -m unittest -v test_shutdown`.
GitHub Actions runs the same test on every push on Ubuntu with Python 3.12.
