# Test Vectors

This repo maintains Test Vectors-based test cases for testing Stratum enabled switches.

## What are Test Vectors

Test Vectors offer a compact way of defining test input/output. A Test Vector is defined as a set of Test Cases where each test case is defined as a set of Actions and Expectations. Actions are operations run on the switch sequentially, in parallel, or in random sequence. Expectations are expected behavior and start after all actions are triggered. The assumption here is the switch is a blackbox, so an action or an expectation is basically a set of Open API access or external stimulus.

Detailed description of Test Vectors structure can be found in the [docs](docs/testvectors_overview.md).

## Structure of this Repo

Currently Stratum supports Barefoot Tofino and Broadcom Tomahawk devices, as well as the bmv2 software switch. At this point Test Vectors for different switch targets are maintained separately under `tofino`, `bcm` and `bmv2` folders.

Take `tofino` as an example, Test Vectors under `tofino` folder are organized into three test suites i.e. `gnmi`, `p4runtime` and `e2e`, each of which contains several Test Vector files with `.pb.txt`  extension.

> Note: please always use `.pb.txt` as filename extension when creating new Test Vectors. Files with other extensions might be ignored by a Test Vectors runner.

There are three other files under the same folder i.e. `PipelineConfig.pb.txt`, `target.pb.txt` and `port-map.json`.
* `PipelineConfig.pb.txt` is normally executed first to push a pipeline configuration to the switch under test.
* `target.pb.txt` stores the IP and port of the switch under test which could be used by a Test Vectors runner to connect to the switch. E.g. `address: "127.0.0.1:28000"`
* `port-map.json` stores a mapping between the switch port numbers used in Test Vectors and physical or virtual interface names connected to the switch ports.  E.g. `{ "176": "ens6f0", "160": "ens6f1" }` means interface `ens6f0` is connected to switch port `176` and interface `ens6f1` is connected to switch port `160`. The interfaces could be used by a Test Vectors runner to send or receive packets when Test Vectors contain Actions/Expectations that involve packets sending/receiving in the data plane.

## Run Test Vectors-based Tests

Reference implementation of Test Vectors Runner and commands to run example tests can be found [here](https://github.com/opennetworkinglab/testvectors-runner)
