package infomap

import (
	"io/ioutil"
	"os"

	protov1 "github.com/golang/protobuf/proto"
	p4_config_v1 "github.com/p4lang/p4runtime/go/p4/config/v1"
)

// InfoMap provides the core table/action name to id mapping methods
type InfoMap struct {
	p4Info *p4_config_v1.P4Info
}

// NewInfoMap instantiates the implementing data structure of InfoMap interface
// requires the filesystem path to the text encoded p4info file
// best place to start as a consumer of the infomap library
func NewInfoMap(p4InfoFilePath string) (*InfoMap, error) {
	info, err := unMarshalP4Info(p4InfoFilePath)
	if err != nil {
		return nil, err
	}
	return &InfoMap{
		p4Info: info,
	}, nil
}

// Table finds the requested table ID
// returns tableName and a fieldId indexed map of the match field names
func (i *InfoMap) Table(id uint32) (tableName string, matchFields map[uint32]string) {
	for _, table := range i.p4Info.Tables {
		if table.Preamble.Id == id {
			tableName = table.Preamble.Alias
			matchFields = make(map[uint32]string)
			for _, match := range table.MatchFields {
				matchFields[match.Id] = match.Name
			}
			return
		}
	}
	return
}

// TableID ...
func (i *InfoMap) TableID(name string) uint32 {
	for _, table := range i.p4Info.Tables {
		switch name {
		case table.Preamble.Alias:
			return table.Preamble.Id
		case table.Preamble.Name:
			return table.Preamble.Id
		}
	}
	return 0
}

// TableName ...
func (i *InfoMap) TableName(id uint32) string {
	for _, table := range i.p4Info.Tables {
		if table.Preamble.Id == id {
			return table.Preamble.Alias
		}
	}
	return ""
}

// ActionID ...
func (i *InfoMap) ActionID(name string) uint32 {
	for _, action := range i.p4Info.Actions {
		switch name {
		case action.Preamble.Alias:
			return action.Preamble.Id
		case action.Preamble.Name:
			return action.Preamble.Id
		}
	}
	return 0
}

// ActionName ...
func (i *InfoMap) ActionName(id uint32) string {
	for _, action := range i.p4Info.Actions {
		if action.Preamble.Id == id {
			return action.Preamble.Alias
		}
	}
	return ""
}

// unMarshalP4Info reads p4info encoding/text
func unMarshalP4Info(fileName string) (*p4_config_v1.P4Info, error) {
	var err error
	if _, err = os.Stat(fileName); !os.IsNotExist(err) {
		// path/to/whatever exists
		sb, err := ioutil.ReadFile(fileName)
		if err != nil {
			return nil, err
		}
		ret := &p4_config_v1.P4Info{}
		if err = protov1.UnmarshalText(string(sb), ret); err != nil {
			return nil, err
		}

		return ret, nil

	}

	return nil, err
}
