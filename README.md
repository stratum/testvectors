# Test Vectors
Repo of Test Vectors-based test cases. To be moved to Stratum repo when ready

Test Vectors offer a compact way of defining test input/output. A Test Vector is defined as a set of Test Cases where each test case is defined as a set of Actions and Expectations. Actions are operations run on the switch sequentially, in parallel, or in random sequence. Expectations are expected behavior and start after all actions are triggered. The assumption here is the switch is a blackbox, so an action or an expectation is basically a set of Open API access or external stimulus.

Detailed description of Test Vectors structure can be found in the [docs](docs/testvectors_overview.md).
