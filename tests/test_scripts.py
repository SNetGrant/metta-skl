from hyperon import MeTTa, E
from pathlib import Path
# from skl import generator
pwd = Path(__file__).parent


def process_exceptions(results):
    for result in results:
        print(result)
        assert result in [[E()], []]


def run_script(fname):
    with open(fname) as f:
        return MeTTa().run(f.read())


def test_scripts():
    process_exceptions(run_script(f"{pwd}/test_hello_world.metta"))
    process_exceptions(run_script(f"{pwd}/test_kmeans.metta"))
