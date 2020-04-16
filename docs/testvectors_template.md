# Test Vector Templates
Test Vector templates are tokenized Test Vector files. Take `bcm/p4runtime/L3ForwardTest.pb.txt` as an example. This Test Vector file is converted to `templates/p4runtime/L3ForwardTest.tmpl` by replacing some switch specific values with tokens. For instance, port number `port: 58` inside `traffic_stimulus` action is replaced by `port: {{ .Port1 }}`.
> Tokens are delimited by `{{` and `}}` and all text outside is unchanged. Check [Go Templates](https://golang.org/pkg/text/template/) for more details regarding the syntax.

When templates are used in testing, a reversed conversion needs to happen which takes in tokenized strings and produce rendered strings with values in place of the tokens. The actual values are specified in a json file, for example:
```json
{
  "Port1":70,
  "Port2":71
}
```

A template engine takes both a Test Vector template and a configuration file as input and produces Test Vectors that could be directly used for testing. Test Vectors Runner supports running with Test Vector templates with a built-in template engine. Check more details [here](https://github.com/stratum/testvectors-runner).
