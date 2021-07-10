package main

import (
	"io/ioutil"

	"html/template"
	"net/http"

	protov1 "github.com/golang/protobuf/proto"
	"github.com/stratum/testvectors/proto/testvector"
	"google.golang.org/protobuf/encoding/protojson"
)

func main() {
	tv, _ := getTVFromFile("bmv2/p4runtime/L3ForwardTest.pb.txt")
	json := protojson.MarshalOptions{Multiline: true}
	sb, _ := json.Marshal(tv)

	tmpl := template.Must(template.ParseFiles("tools/ui/index.gohtml"))
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		tmpl.Execute(w, string(sb))
	})
	http.ListenAndServe(":8080", nil)

}

// getTVFromFile reads Test Vector file with given file name and returns Test Vector
func getTVFromFile(fileName string) (*testvector.TestVector, error) {
	tvdata, err := ioutil.ReadFile(fileName)
	if err != nil {
		return nil, err
	}
	tVec := &testvector.TestVector{}
	if err = protov1.UnmarshalText(string(tvdata), tVec); err != nil {
		return nil, err
	}
	return tVec, nil
}
