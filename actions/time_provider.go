package main

import (
	"context"
	"fmt"
	"time"
)

// TimeProvider is a custom action that provides the current time to an LLM
// It implements the three required functions: Run, Definition, and RequiredFields

// Run executes the action and returns the current time
func Run(config map[string]interface{}) (string, map[string]interface{}, error) {
	// Get the current time in RFC3339 format
	currentTime := time.Now().Format(time.RFC3339)
	
	// Return the current time as a string
	return fmt.Sprintf("Current time: %s", currentTime), map[string]interface{}{}, nil
}

// Definition returns the parameters required for this action
func Definition() map[string][]string {
	return map[string][]string{}
}

// RequiredFields returns the list of required parameters
func RequiredFields() []string {
	return []string{}
}