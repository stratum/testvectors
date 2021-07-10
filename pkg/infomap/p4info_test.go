package infomap

import (
	"testing"

	p4_config_v1 "github.com/p4lang/p4runtime/go/p4/config/v1"
)

func mockP4info(t *testing.T) *p4_config_v1.P4Info {
	helloworldTable := &p4_config_v1.Table{
		Preamble: &p4_config_v1.Preamble{
			Id:    9999,
			Name:  "fabric.ingress.helloworld",
			Alias: "helloworld",
		},
		MatchFields: []*p4_config_v1.MatchField{
			{Id: 1, Name: "port"},
			{Id: 2, Name: "mac"},
			{Id: 3, Name: "ip"},
		},
	}
	return &p4_config_v1.P4Info{
		Tables: []*p4_config_v1.Table{helloworldTable},
	}

}
func TestInfoMap_TableID(t *testing.T) {
	mockinfo := mockP4info(t)
	type fields struct {
		p4Info *p4_config_v1.P4Info
	}
	type args struct {
		name string
	}
	tests := []struct {
		name   string
		fields fields
		args   args
		want   uint32
	}{
		{
			name:   "helloworld",
			fields: fields{mockinfo},
			args:   args{"helloworld"},
			want:   9999,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			i := &InfoMap{
				p4Info: tt.fields.p4Info,
			}
			if got := i.TableID(tt.args.name); got != tt.want {
				t.Errorf("InfoMap.TableID() = %v, want %v", got, tt.want)
			}
		})
	}
}
