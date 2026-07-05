import subprocess


def run_crew(customer_request):
    """
    Executes the CrewAI project and returns its output.
    """

    process = subprocess.run(
        ["crewai", "run"],
        input=customer_request,
        capture_output=True,
        text=True,
        shell=True
    )

    if process.returncode == 0:
        return process.stdout
    else:
        return process.stderr 