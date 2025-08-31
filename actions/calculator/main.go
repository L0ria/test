import (
	"encoding/json"
	"log"
	"os"
)

// Input represents the request structure
type Input struct {
	Action  string            `json:"action"`
	Params  map[string]float64 `json:"params"`
}

// Output represents the response structure
type Output struct {
	Result float64 `json:"result"`
}

func main() {
	var input Input
	if err := json.NewDecoder(os.Stdin).Decode(&input); err != nil {
		log.Printf("Error reading input: %v", err)
		ose.Exit(1)
	}

	var result float64

	switch input.Action {
	case "add":
		a, b := input.Params["a"], input.Params["b"]
		result = a + b
	case "subtract":
		a, b := input.Params["a"], input.Params["b"]
		result = a - b
	case "multiply":
		a, b := input.Params["a"], input.Params["b"]
		result = a * b
	case "divide":
		a, b := input.Params["a"], input.Params["b"]
		if b == 0 {
			log.Printf("Division by zero error: %f / %f", a, b)
			ose.Exit(1)
		}
		result = a / b
	default:
		log.Printf("Unknown action: %s", input.Action)
		ose.Exit(1)
	}

	output := Output{Result: result}
	if err := json.NewEncoder(os.Stdout).Encode(output); err != nil {
		log.Printf("Error writing output: %v", err)
		ose.Exit(1)
	}
}