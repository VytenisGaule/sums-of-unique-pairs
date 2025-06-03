# Pairs Finder

Finds and prints all unique pairs in an unsorted array that have equal sums. Supports input as a string in curly-brace format (e.g., `{6, 4, 12, 10}`).

## Project Structure

```
pairs/
├── src/
│   ├── main.py        # Entry point of the application
│   ├── utils.py       # Utility functions for processing the array
│   └── models.py      # JSArray class for parsing curly-brace array strings
├── tests/
│   └── test_pairs.py  # Unit tests for the application
├── requirements.txt   # Project dependencies
└── README.md          # Project documentation
```

## Getting Started

1. **Clone the repository:**
   ```sh
   git clone <repository-url>
   cd pairs
   ```

2. **Create and activate a virtual environment (recommended):**
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```sh
   python src/main.py
   ```

## Example Usage

**Input:**
```
A = '{ 6, 4, 12, 10, 22, 54, 32, 42, 21, 11 }'
```

**Output:**
```
Pairs : ( 4, 12) ( 6, 10) have sum : 16
Pairs : ( 10, 22) ( 21, 11) have sum : 32
Pairs : ( 12, 21) ( 22, 11) have sum : 33
Pairs : ( 22, 21) ( 32, 11) have sum : 43
Pairs : ( 32, 21) ( 42, 11) have sum : 53
Pairs : ( 12, 42) ( 22, 32) have sum : 54
Pairs : ( 10, 54) ( 22, 42) have sum : 64
```

**Input:**
```
A = '{ 4, 23, 65, 67, 24, 12, 86 }'
```

**Output:**
```
Pairs : ( 4, 86) ( 23, 67) have sum : 90
```

## Testing

To run the unit tests:
```sh
pytest tests/test_pairs.py
```

This will execute the tests to ensure the application works as expected.

---