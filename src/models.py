"""class objects"""

class CArray:
    """C++ array-like string"""

    def __init__(self, c_array_str):
        self.c_array_str = c_array_str
        
    def _is_valid_elements(self, elements: list) -> bool:
        """Check if all elements can be converted to int."""
        for nmb in elements:
            if not nmb.lstrip('-').isdigit():
                return False
        return True

    def to_list(self) -> list:
        """Convert the C++ array-like string to a Python list."""
        if not isinstance(self.c_array_str, str):
            return []
        if not self.c_array_str.startswith('{') or not self.c_array_str.endswith('}'):
            return []
        stripped_str: str = self.c_array_str.strip('{} ')
        elements: list = [nmb.strip() for nmb in stripped_str.split(',') if nmb.strip()]
        if not self._is_valid_elements(elements):
            return []
        return [int(nmb) for nmb in elements]
