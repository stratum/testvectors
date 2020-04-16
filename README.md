# Test Vectors

This repo maintains Test Vectors-based test cases for testing Stratum enabled switches.

## What are Test Vectors

Test Vectors offer a compact way of defining test input/output. A Test Vector is defined as a set of Test Cases where each test case is defined as a set of Actions and Expectations. Actions are operations run on the switch sequentially, in parallel, or in random sequence. Expectations are expected behavior and start after all actions are triggered. The assumption here is the switch is a blackbox, so an action or an expectation is basically a set of Open API access or external stimulus.

Detailed description of Test Vectors structure can be found in the [docs](docs/testvectors_overview.md).

## Structure of this Repo

Currently Stratum supports Barefoot Tofino and Broadcom Tomahawk devices, as well as the bmv2 software switch. At this point Test Vectors for different switch targets are maintained separately under `tofino`, `bcm` and `bmv2` folders.

Take `tofino` as an example, Test Vectors under `tofino` folder are organized into three test suites i.e. `gnmi`, `p4runtime` and `e2e`, each of which contains several Test Vector files with `.pb.txt` extension.

> Note: please always use `.pb.txt` as filename extension when creating new Test Vectors. Files with other extensions might be ignored by a Test Vectors runner.

Other files under the same folder are listed below:
* `PipelineConfig.pb.txt` is normally executed first to push a pipeline configuration to the switch under test.
* `target.pb.txt` stores the IP and port of the switch under test which could be used by a Test Vectors runner to connect to the switch. E.g. `address: "127.0.0.1:28000"`
* `portmap.pb.txt` contains a list of entries, each of which stores infomation related to a specific switch port used in the Test Vectors including port number, port type (see proto/portmap/portmap.proto for definition) and name of physical or virtual interface connected to the switch port. E.g. a portmap entry with `port_number: 58`, `interface_name: "ens6f0"` and `port_type: 0` means interface `ens6f0` is connected to switch port `58` and could be used as both ingress and egress to switch. The interfaces could be used by a Test Vectors runner to send or receive packets when Test Vectors contain Actions/Expectations that involve packets sending/receiving in the data plane.

## Test Vector Templates

As an alternative way of maintaining the tests, `Test Vector templates` were created with the goal of having only one set of tests that works across multiple switch platforms. Test Vector templates use `.tmpl` instead of `.pb.txt` as extension name and are maintained under `templates` folder. They are organized the same way as the platform specific Test Vectors.

In addition to the template files, one `template configuration file` is also needed for each platform. The template configuration file is used for rendering the templates and producing Test Vector files that match your switch target. Examples of template configuration files can be found under switch target specific folders e.g. `bcm/template_config.json`. Also check the [docs](docs/testvectors_template.md) for more details about Test Vector templates.

## Run Test Vectors-based Tests

Reference implementation of Test Vectors Runner and commands to run example tests can be found [here](https://github.com/stratum/testvectors-runner).
